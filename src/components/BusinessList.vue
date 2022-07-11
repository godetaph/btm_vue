<template>
    <div class="column is-12">
        <form @submit.prevent="submitForm" class="mb-3">
            <div class="field has-addons">
                <div class="control">
                    <input type="text" class="input is-small" style="width:300px;" v-model="query">
                </div>
                <div class="control">
                    <button class="button is-success ml-2 is-small">Search</button>
                </div>
                <div class="control">
                    <button class="button is-light ml-2 is-small" @click="showSearch">Advanced search</button>
                </div>
            </div>
            <div class="columns" v-if="showAdvanced">
                
                <div class="column is-3">
                    <div class="select is-small ">
                        <select name="" id="" class="select" @change="showValue($event)">
                            <option value="">-- Select criteria --</option>
                            <option value="barangay">Barangay</option>
                            <option value="permit">Business permit</option>
                            <option value="status">Permit status</option>
                            <option value="ownership">Ownership type</option>
                            <option value="bus_status">Business status</option>
                            <option value="payment">Payment type</option>
                            <option value="application">Application status</option>
                            <option value="location">Location status</option>
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'barangay'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Select a barangay --</option>
                            <option v-for="barangay in barangays" v-bind:key="barangay.id" v-bind:value="barangay.barangay_name">
                                {{barangay.barangay_name}}
                            </option>
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'permit'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Business permit? [Yes/No] --</option>
                            <option value="yes">Yes</option>
                            <option value="no">No</option>          
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'status'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Select permit notice --</option>
                            <option value="FIRST">First notice</option>
                            <option value="SECOND">Second notice</option>          
                            <option value="FINAL">Third notice</option>          
                            <option value="CLOSURE">Subject for closure</option>          
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'ownership'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Select ownership type --</option>
                            <option value="single">Single Proprietor</option>
                            <option value="partnership">Partnership</option>
                            <option value="corporation">Corporation</option>
                            <option value="cooperative">Cooperative</option>    
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'bus_status'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Select business status --</option>
                            <option value="ACTIVE1">Active w/o extension</option>
                            <option value="ACTIVE2">Active with extension</option>          
                            <option value="INACTIVE">Inactive</option>          
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'payment'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Payment type --</option>
                            <option value="annual">Annually</option>
                            <option value="semi-annual">Semi-annual</option>          
                            <option value="quarterly">Quarterly</option>          
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'application'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Application type --</option>
                            <option value="new">New</option>
                            <option value="renew">Renewal</option>          
                        </select>
                    </div>
                </div>
                <div class="column is-4" v-if="values == 'location'">
                    <div class="select is-small ">
                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                            <option value="">-- Location status --</option>
                            <option value="owned">Owned</option>
                            <option value="rented">Rented</option>          
                        </select>
                    </div>
                </div>
                <div class="column is-4 control" v-if="values != ''">
                    <!-- <router-link to="#" class="button is-success mb-4 is-small" @click="generateReport()">Print | <span class="ml-1">{{this.values}}</span></router-link> -->
                    <button class="button is-success mb-4 is-small" @click="getBusinessesReport()">
                        Print | <span class="ml-1">{{this.values}}</span></button>
                </div>
            </div>
        </form>
        <hr>
        <router-link to="/dashboard/businesses/add" class="button is-dark mb-4 is-small">Add business</router-link>
        
        <table class="table is-striped is-narrow is-hoverable is-fullwidth is-size-7 mt-4">
            <thead>
                <tr>
                    <th>Business name</th>
                    <th>Owner name</th>
                    <th>Contact</th>
                    <th>Barangay</th>
                    <th>Purok</th>
                    <th>Stall no</th>
                    <th>Permit</th>
                    <th>Appln</th>
                    <th class="has-text-right">Capital</th>
                    <th class="has-text-right">Gross</th>
                    <th >Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="business in businesess" v-bind:key="business.id" :class="{'has-text-danger': business.is_business_permit=='no'}">
                    <!-- <td class="is-uppercase">{{business.business_name}}</td> -->
                    <td class="is-uppercase"> <router-link :to="{name: 'Business', params: {id:business.id}}" class="has-text-info">{{business.business_name}}</router-link> </td>
                    <td class="is-uppercase">{{business.business_owner_name}}</td>
                    <td>{{business.business_owner_number}}</td>
                    <td v-if="business.barangay">{{business.bar_name}}</td>
                    <td v-else>-</td>
                    <td>{{business.purok}}</td>
                    <td>{{business.stall_no}}</td>
                    <td>{{business.is_business_permit}}</td>
                    <td>{{business.application_status}}</td>
                    <td class="has-text-right">{{Number(business.capitalization_amount).toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2})}}</td>
                    <td class="has-text-right">{{Number(business.gross_sale_amount).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}}</td>
                    <td>
                        <!-- <router-link :to="{name: 'Business', params: {id:business.id}}" class="has-text-info"><i class="fa fa-info"></i>Info</router-link> |  -->
                        <router-link :to="{name: 'EditBusiness', params: {id:business.id}}" class="has-text-info"><i class="fa fa-pencil-square-o"></i></router-link> | 
                        <router-link :to="{name: 'Payments', params: {id:business.id}}" class="has-text-info"><i class="fa fa-money"></i></router-link> |
                        <router-link :to="{name: 'BusinessCategories', params: {id:business.id}}" class="has-text-info"><i class="fa fa-briefcase"></i></router-link> |
                        <router-link :to="{name: 'AddBusinessPeriod', params: {id:business.id}}" class="has-text-info"><i class="fa fa-plus"></i></router-link>
                        <!-- <router-link to="#" class="has-text-info" @click="$refs.modalName.openModal()"><i class="fa fa-plus"></i></router-link> -->
                        <!-- <button @click="$refs.modalName.openModal()">Open modal</button> -->
                    </td>
                </tr>
            </tbody>
            <tfoot>
                <td><strong>Total count:</strong></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td class="has-text-right"><strong>{{this.noPage}}</strong> of <strong>{{this.counts}}</strong> </td>
            </tfoot>
        </table>
        <div class="buttons">
            <button class="button is-outlined is-dark is-small" @click="loadNext()" v-if="showNext">Next</button>
            <button class="button is-outlined is-dark is-small" @click="loadPrev()" v-if="showPrev">Previous</button>
        </div>
        <!-- <button @click="$refs.modalName.openModal()">Open modal</button> -->

        <modal ref="modalName">
            <template v-slot:header>
                <h1>Modal title</h1>
            </template>

            <template v-slot:body>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc sed velit dignissim sodales ut eu sem integer vitae. Id aliquet lectus proin nibh nisl condimentum. Fringilla urna porttitor rhoncus dolor purus. Nam aliquam sem et tortor. Nisl vel pretium lectus quam id. Cras pulvinar mattis nunc sed. Quis ipsum suspendisse ultrices gravida dictum fusce ut placerat orci. Tristique magna sit amet purus. Fermentum et sollicitudin ac orci phasellus egestas tellus. Erat pellentesque adipiscing commodo elit at imperdiet dui accumsan. Felis eget nunc lobortis mattis aliquam faucibus. Tincidunt eget nullam non nisi est sit amet facilisis. Mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Vitae proin sagittis nisl rhoncus mattis rhoncus urna neque. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. Nec nam aliquam sem et tortor consequat id. Commodo nulla facilisi nullam vehicula ipsum a. Elementum tempus egestas sed sed. Faucibus purus in massa tempor nec feugiat nisl pretium fusce.</p>
                <p>Arcu cursus vitae congue mauris rhoncus aenean. Tempor id eu nisl nunc mi. Pharetra diam sit amet nisl suscipit adipiscing bibendum. Ut faucibus pulvinar elementum integer enim. Odio facilisis mauris sit amet massa vitae tortor condimentum lacinia. Eu non diam phasellus vestibulum lorem sed risus. Porttitor rhoncus dolor purus non enim praesent. Sit amet mauris commodo quis imperdiet. Lobortis feugiat vivamus at augue eget. Nibh tellus molestie nunc non blandit. Tellus mauris a diam maecenas sed enim ut. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Mattis aliquam faucibus purus in massa.</p>
            </template>

            <template v-slot:footer>
                <div class="d-flex align-items-center justify-content-between">
                <button class="btn btn--secondary" @click="$refs.modalName.closeModal()">Cancel</button>
                <button class="btn btn--primary" @click="$refs.modalName.closeModal()">Save</button>
                </div>
            </template>
        </modal>

        
            <vue3-html2pdf
                    :show-layout="false"
                    :float-layout="true"
                    :enable-download="false"
                    :preview-modal="true"
                    :paginate-elements-by-height="800"
                    :pdf-quality="2"
                    :manual-pagination="true"
                    pdf-content-width="800px"
                    :html-to-pdf-options="htmlToPdfOptions"
                    
                    @hasStartedGeneration="hasStartedGeneration()"
                    @hasGenerated="hasGenerated($event)"
                    @beforeDownload="beforeDownload($event)"
                    ref="html2Pdf"
                >
                    <template v-slot:pdf-content>
                        <!-- PDF Content Here -->
                        <h4 class="has-text-centered">Municipality of Midsayap</h4>
                        <h4 class="has-text-centered" style="font-weight: bold;">Municipal Treasurer Office</h4>
                        <h4 class="has-text-centered mt-3">List of Business</h4>
                        <h5 class="has-text-centered"><span class="is-uppercase">{{values}}</span> - <span class="is-uppercase">{{query}}</span></h5>
                            <div style="margin: 10px;">
                                <table class="table is-bordered is-narrow ml-1 mt-3" style="width:100%; border: 1px solid #000;">
                                    <thead>
                                        <tr>
                                            <th class="is-size-7" style="width:5%;">#</th>
                                            <th class="is-size-7" style="width:30%;">Business name</th>
                                            <th class="is-size-7" style="width:30%;">Owner name</th>
                                            <th class="is-size-7" style="width:10%;">Contact</th>
                                            <th class="is-size-7" style="width:15%;">Barangay</th>
                                            <th class="is-size-7" style="width:10%;">Purok</th>
                                            <!-- <th>Stall no</th> -->
                                            <!-- <th>Permit</th>
                                            <th>Appln</th>
                                            <th class="has-text-right">Capital</th>
                                            <th class="has-text-right">Gross</th> -->
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(business, index) in businessReport" v-bind:key="business.id" :class="{'has-text-danger': business.is_business_permit=='no'}">
                                            <!-- <td class="is-uppercase">{{business.business_name}}</td> -->
                                            <td class="is-size-7">{{index + 1}}</td>
                                            <td class="is-uppercase is-size-7"> {{business.business_name}} </td>
                                            <td class="is-uppercase is-size-7">{{business.business_owner_name}}</td>
                                            <td class="is-size-7">{{business.business_owner_number}}</td>
                                            <td class="is-size-7" v-if="business.barangay">{{business.bar_name}}</td>
                                            <td v-else>-</td>
                                            <td class="is-size-7">{{business.purok}}</td>
                                            <!-- <td>{{business.stall_no}}</td> -->
                                            <!-- <td>{{business.is_business_permit}}</td>
                                            <td>{{business.application_status}}</td>
                                            <td class="has-text-right">{{Number(business.capitalization_amount).toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2})}}</td>
                                            <td class="has-text-right">{{Number(business.gross_sale_amount).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}}</td> -->
                                            
                                        </tr>
                                        
                                    </tbody>
                                    <!-- <tfoot>
                                        <td><strong>Total count:</strong></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td></td>
                                        <td class="has-text-right"><strong>{{businesess.length}}</strong> of <strong>{{this.counts}}</strong> </td>
                                    </tfoot> -->
                                </table>
                            </div>
                    </template>
                </vue3-html2pdf>
            
        
    </div>
</template>

<script>
import axios from 'axios'
import Modal from './Modal.vue'
import Vue3Html2pdf from 'vue3-html2pdf'
export default {
    name: 'Businesses',
    components: {
        Modal, Vue3Html2pdf
    },
    
    data() {
        return {
            businesess: [],
            businessReport: [],
            barangays: [],
            currentPage: 1,
            showNext: false,
            showPrev: false,
            showAdvanced: false,
            query: '',
            values: '',
            counts:0,
            filename: 'ok.pdf',
            noPage: 0,
            totalPage: 0,
        }
    },
    computed: {
        // ...mapFields(["controlValue"]),

        htmlToPdfOptions() {
            return {
                margin: [0.2, 0, 0.5, 0],
                filename: this.filename,
                image: {
                    type: "jpeg",
                    quality: 0.98,
                    },
                enableLinks: true,
                html2canvas: {
                    scale: 3,
                    useCORS: true,
                    },
                jsPDF: {
                    unit: "in",
                    format: "letter",
                    orientation: "portrait",
                    },
            };
        },
    },
    mounted() {
        this.getBusinesses()
    },
    methods: {
        loadNext() {
            this.currentPage += 1
            this.getBusinesses()
            this.noPage += this.businesess.length
        },
        loadPrev() {
            this.currentPage -= 1
            this.getBusinesses()
            this.noPage -= this.businesess.length
        },
        getBusinesses() {
            //axios.get(`/api/v1/businesses/?size=10`) 
            axios.get(`/api/v1/businesses/?page=${this.currentPage}&size=25&search=${this.query}`) 
                 .then(response => {
                     this.showNext=false
                     this.showPrev=false
                     this.businesess=response.data.results
                    //  console.log(response.data)
                     this.counts=response.data.count
                    if (this.counts < this.noPage ){
                        this.noPage = this.counts
                        }
                     if (this.currentPage <= 1){
                        this.noPage = this.businesess.length
                     }
                    //  this.noPage = this.currentPage * this.businesess.length

                    //  for(let i=0; i < response.data.length; i++){
                    //      this.businesess.push(response.data[i])
                    //  }
                     if (response.data.next){
                         this.showNext=true
                     }
                     if (response.data.previous){
                         this.showPrev=true
                     }
                     //this.businesses = response.data
                 })
                 .catch(error => {
                     console.log(error)
                 })
        },
        getBusinessesReport() {
            //axios.get(`/api/v1/businesses/?size=10`) 
            axios.get(`/api/v1/businesses/?search=${this.query}`) 
                 .then(response => {
                    //console.log(response)
                     this.businessReport=response.data

                     //console.log(this.businesess)
                     //this.counts=response.data.count
                    //  for(let i=0; i < response.data.length; i++){
                    //      this.businesess.push(response.data[i])
                    //  }
                     //this.businesses = response.data
                    
                    this.generateReport()
                 })
                 .catch(error => {
                     console.log(error)
                 })
        },
        submitForm() {
            this.getBusinesses()
        },
        getBarangays() {
            axios.get(`/api/v1/barangays/?size=200`)
                 .then(response => {
                     this.barangays=response.data.results
                 })
                 .catch(error => JSON.stringify(error))
        },
        showSearch() {
            this.showAdvanced= !this.showAdvanced
        },
        showValue(event) {
            this.values=event.target.value
            if (this.values=='barangay'){
                this.getBarangays()
            }
            this.query=''
            this.filename=this.values
        },
        generateReport() {
            this.$refs.html2Pdf.generatePdf()

        },
        async beforeDownload ({ html2pdf, options, pdfContent }) {
            await html2pdf().set(options).from(pdfContent).toPdf().get('pdf').then((pdf) => {
                const totalPages = pdf.internal.getNumberOfPages()
                for (let i = 1; i <= totalPages; i++) {
                    pdf.setPage(i)
                    pdf.setFontSize(10)
                    pdf.setTextColor(150)
                    pdf.text('Page ' + i + ' of ' + totalPages, (pdf.internal.pageSize.getWidth() * 0.88), (pdf.internal.pageSize.getHeight() - 0.3))
                } 
            }).save()
        },
    }
}
</script>

<style lang="scss">
    
</style>