<template>
  <div class="page upload-collection">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="is-size-5"><strong>BTM</strong><span class="has-text-info">Upload</span>Collection</div>
              <hr>
            
                <div class="column">
                    <div class="field">
                        <label for="">Select collection (.xls) file</label>
                        <div class="control">
                            <input type="file" class="input" @change="importExcel">
                        </div>
                    </div>
                </div>

                <div class="column" v-if="payment.dataArr.length > 0">
                    <div class="box">
                        <div class="field">
                            <div class="control">
                                <button class="button is-success" @click="uploadData">Upload to database</button>
                            </div>
                        </div>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Mode</th>
                                    <th>Code</th>
                                    <th>Or no</th>
                                    <th>Date</th>
                                    <th>Paid to</th>
                                    <th>Amount</th>

                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="d in payment.dataArr" v-bind:key="d.code">
                                    <td>{{d.payment_mode}}</td>
                                    <td>{{d.code}}</td>
                                    <td>{{d.or_no}}</td>
                                    <td>{{d.payment_date}}</td>
                                    <td>{{d.paid_to}}</td>
                                    <td>{{d.amount_paid}}</td>
                                </tr>
                            </tbody>
                        </table>

                        <!-- Table components -->
                        
                        <!-- <div class="table">
                            <table
                                max-height="600"
                                :data="dataArr"
                                v-loading="tableLoading"
                                border
                                style="width: 100%"
                            >
                                <el-table-column
                                :prop="item.prop"
                                :label="item.label"
                                :width="item.width"
                                v-for="(item, i) in tableColumn"
                                :key="i"
                                ></el-table-column>
                            </el-table>
                        </div> -->
                        <!-- Table components -->
                    </div>
                </div>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import xlsx from 'xlsx'

export default {
    name: 'UploadCollection',
    data() {
        return {
            load: 'false',
            payment: {dataArr: []}, // Table content data array
            pay: {},
            // countArr: {}, // Analyze the table data and header to get a cross reference array for user-defined consolidation. For the time being, this article only writes the basis, and does not introduce the automatic consolidation of cells~~My other articles have custom merge implementation methods~
            tableColumn: [], // Table header szconfiguration array
            tableLoading: false // Whether the table is loading
        }
    },
    methods: {
        sleep(ms){
            return new Promise(resolve => setTimeout(resolve, ms))
        },
        uploadData() {
            this.load=true
            // this.dataArr.forEach(element => {
            //     console.log(element)
            // });
            console.log(this.payment.dataArr.length)
            console.log(this.payment.dataArr[0])
            this.pay.code="0111"
            this.pay.payment_mode="quarter"
            this.pay.payment_date="2014-01-01"
            this.pay.amount_paid="1000"
            this.pay.or_no="0908090"
            this.pay.business="25"
            this.pay.created_by="1"

            console.log(this.pay)
            axios.post("/api/v1/payments/", this.pay)
                 .then(response => {
                     toast ({
                        message: 'New payment was added successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     //this.$router.push(`/dashboard/payments/${businessId}`)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
            // for (let i=0; i < this.payment.dataArr.length; i++){
            //     console.log(this.payment.dataArr[i])
            //     axios.post('/api/v1/payments/', this.payment.dataArr[i])
            //             .then(response => {
            //                 console.log(response.statusText)
            //             })
            // }
            
            this.load=false
        },
        clickLoad(){
            this.load=!this.load
            console.log(this.load)
        },
        formatDate(date) {
            var d = new Date(date),
                month = '' + (d.getMonth() + 1),
                day = '' + d.getDate(),
                year = d.getFullYear();

            if (month.length < 2) 
                month = '0' + month;
            if (day.length < 2) 
                day = '0' + day;

            return [year, month, day].join('-');
        },
        getHeader(sheet) {
            const XLSX = xlsx;
            const headers = [];
            const range = XLSX.utils.decode_range(sheet["!ref"]); // worksheet['!ref'] Is the valid range of the worksheet
            let C;
            /* Get cell value start in the first row */
            const R = range.s.r; //Line / / column C
            let i = 0;
            for (C = range.s.c; C <= range.e.c; ++C) {
                var cell =
                sheet[
                    XLSX.utils.encode_cell({ c: C, r: R })
                ]; /* Get the cell value based on the address  find the cell in the first row */
                var hdr = "UNKNOWN" + C; // replace with your desired default
                // XLSX.utils.format_cell Generate cell text value
                if (cell && cell.t) hdr = XLSX.utils.format_cell(cell);
                if(hdr.indexOf('UNKNOWN') > -1){
                if(!i) {
                    hdr = '__EMPTY';
                }else {
                    hdr = '__EMPTY_' + i;
                }
                i++;
                }
                headers.push(hdr);
            }
            return headers;
        },
        /**
         * Import table
         */
        importExcel(e) {
            const files = e.target.files;
            console.log(files);
            if (!files.length) {
                return ;
            } else if (!/\.(xls|xlsx)$/.test(files[0].name.toLowerCase())) {
                return alert("The upload format is incorrect. Please upload xls or xlsx format");
            }
            const fileReader = new FileReader();
            fileReader.onload = ev => {
                try {
                const data = ev.target.result;
                const XLSX = xlsx;
                const workbook = XLSX.read(data, {
                    type: "binary"
                });
                const wsname = workbook.SheetNames[0]; // Take the first sheet，wb.SheetNames[0] :Take the name of the first sheet in the sheets
                const ws = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]); // Generate JSON table content，wb.Sheets[Sheet名]    Get the data of the first sheet
                const excellist = [];  // Clear received data
                // Edit data
                for (var i = 0; i < ws.length; i++) {
                    var date = new Date(ws[i].payment_date) 
                    ws[i].payment_date = this.formatDate(new Date(Math.round((date - 25569)*86400*1000)))
                    excellist.push(ws[i]);
                    // var date = new Date(ws[i].date) 
                    //console.log(new Date(Math.round((date - 25569)*86400*1000)))
                }
                this.payment.dataArr=excellist
                console.log("Read results", this.payment.dataArr); // At this point, you get an array containing objects that need to be processed
                
                const a = workbook.Sheets[workbook.SheetNames[0]]
                const headers = this.getHeader(a)
                console.log("headers", headers)

                // this.setTable(headers, excellist)

                } 
                catch (e) {
                    return alert(e + " - Read failure!");;
                }
            };
            fileReader.readAsBinaryString(files[0]);
                var input = document.getElementById("upload");
                input.value = "";
            }
        },
        setTable(headers, excellist) {
        const tableTitleData = []; // Store table header data
        const tableMapTitle = {}; // Set table content for Chinese and English
        headers.forEach((_, i) => {
            tableMapTitle[_] = "prop" + i;
            tableTitleData.push({
            prop: "prop" + i,
            label: _,
            width: 100
            });
        });
        console.log("tableTitleData", tableTitleData);
        // Mapping table content attribute name is English
        const newTableData = [];
        excellist.forEach(_ => {
            const newObj = {};
            Object.keys(_).forEach(key => {
            newObj[tableMapTitle[key]] = _[key];
            });
            newTableData.push(newObj);
        });
        console.log('newTableData',newTableData);
        this.tableColumn = tableTitleData;
        this.dataArr = newTableData;
        },
        
}
</script>

<style>

</style>