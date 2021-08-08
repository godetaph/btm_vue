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

                <div class="column" v-if="dataArr.length > 0">
                    <div class="box">
                        <div class="field">
                            <div class="control">
                                <button :class="!load ? 'button is-success is-loading' : 'button is-success'" @click="uploadData">Upload to database</button>
                            </div>
                        </div>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Business</th>
                                    <th>Owner</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="d in dataArr" v-bind:key="d._id">
                                    <td>{{d._1_Enter_Business_Name}}</td>
                                    <td>{{d._7_Name_of_the_Business_Owner}}</td>
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
import xlsx from 'xlsx'
export default {
    name: 'UploadCollection',
    data() {
        return {
            load: 'false',
            dataArr: [], // Table content data array
            // countArr: {}, // Analyze the table data and header to get a cross reference array for user-defined consolidation. For the time being, this article only writes the basis, and does not introduce the automatic consolidation of cells~~My other articles have custom merge implementation methods~
            tableColumn: [], // Table header configuration array
            tableLoading: false // Whether the table is loading
        }
    },
    methods: {
        sleep(ms){
            return new Promise(resolve => setTimeout(resolve, ms))
        },
        async uploadData() {
            this.load=true
            await this.sleep(3000)
            this.dataArr.forEach(element => {
                console.log(element)
            });
            
            this.load=false
        },
        clickLoad(){
            this.load=!this.load
            console.log(this.load)
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
                    excellist.push(ws[i]);
                }
                this.dataArr=excellist
                console.log("Read results", this.dataArr); // At this point, you get an array containing objects that need to be processed
                
                const a = workbook.Sheets[workbook.SheetNames[0]]
                const headers = this.getHeader(a)
                console.log("headers", headers)

                // this.setTable(headers, excellist)

                } catch (e) {
                    return alert("Read failure!");;
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