<template>
  <div class="page smshome">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="is-size-5"><strong>SMS</strong><span class="has-text-info">Home</span></div>
                <hr>
                <div class="columns">
                    <div class="column is-12">
                        <strong class="">SMS Message</strong> 
                        <div class="column">
                            <div class="column is-12">
                                <textarea v-on:keyup="countdown" v-model="message" name="sms" maxlength="160" id="" class="textarea" placeholder="SMS Message here (max = 160 character)" rows="5"></textarea>
                            </div>
                            <div class="column">
                                <span class="pull-left" v-bind:class="{'has-text-danger': hasError}">{{remainCount}} text remaining.</span>
                                
                            </div>
                            
                        </div>
                        <hr>
                        <div class="column">
                            <strong>Recepient/s</strong>
                            <div class="columns">
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
                                        </div>
                                    </form>
                                </div>
                                <div class="column is-4">
                                    <div class="select is-small ">
                                        <select name="" id="" class="select" v-model="query" @change="submitForm">
                                            <option value="">-- Select a barangay --</option>
                                            <option v-for="barangay in barangays" v-bind:key="barangay.id" v-bind:value="barangay.barangay_name">
                                                {{barangay.barangay_name}}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div class="column">
                                <table class="table table is-striped is-narrow is-hoverable is-fullwidth is-size-7 mt-4">
                                    <thead>
                                        <tr>
                                            <th><input type="checkbox" class="checkbox" v-bind:checked="allSelected" @click="selectAll"></th>
                                            <th>Business</th>
                                            <th>Representative</th>
                                            <th>Contact number</th>
                                            <th>Barangay</th>
                                            <th>Purok</th>
                                            <th>Stall</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="business in businesses" v-bind:key="business.id">
                                            <td><input type="checkbox" class="checkbox" v-model="business.selected"/></td>
                                            <td>{{ business.business_name }}</td>
                                            <td>{{ business.business_owner_name }}</td>
                                            <td>{{ business.business_owner_number }}</td>
                                            <td v-if="business.barangay">{{business.bar_name}}</td>
                                            <td v-else>-</td>
                                            <td>{{business.purok}}</td>
                                            <td>{{business.stall_no}}</td>
                                        </tr>
                                    </tbody>
                                </table>
                                <div class="column is-8">
                                    <h2 class="subtitle">Current Selections</h2>
                                        <div class="content">

                                            <p >
                                                <span class="tag is-light">{{ currentSelections }}</span>
                                            </p>
                                        </div>
                                </div>
                            </div>
                            <div class="buttons">
                                <button class="button is-outlined is-dark is-small" @click="loadNext()" v-if="showNext">Next</button>
                                <button class="button is-outlined is-dark is-small" @click="loadPrev()" v-if="showPrev">Previous</button>
                            </div>
                        </div>
                        <button class="button is-primary ml-5" @click="sendSms()">Send message</button>
                    </div>
                </div>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SmsHome',
    data() {
        return {
            currentPage: 1,
            showNext: false,
            showPrev: false,
            showAdvanced: false,
            query: '',
            values: '',
            barangays: [],
            businesses: [],
            maxCount: 160,
            remainCount: 160,
            message: '',
            hasError: false,
            // items: [
            //         { id: 101, name: "Item #1" },
            //         { id: 102, name: "Item #2" },
            //         { id: 103, name: "Item #3" }
            //         ],
            currentSelections: null
        }
    },
    mounted() {
        // this.getBusinesses()
        this.selectedItems  //  this.items.forEach( itm => this.$set(itm, "selected", false));
    },
    computed: {
        allSelected() {
            // return this.items.every(itm => itm.selected);
            return this.businesses.every(itm => itm.selected);
        }
    },
    methods: {
        loadNext() {
            this.currentPage += 1
            this.getBusinesses()
        },
        loadPrev() {
            this.currentPage -= 1
            this.getBusinesses()
        },
        getBusinesses() {
            //axios.get(`/api/v1/businesses/?size=10`) 
            axios.get(`/api/v1/businesses/?page=${this.currentPage}&size=25&search=${this.query}`) 
                 .then(response => {
                     this.showNext=false
                     this.showPrev=false
                     this.businesses=response.data.results
                     this.counts=response.data.count
                    //  for(let i=0; i < response.data.results.length; i++){
                    //      this.businesess.push(response.data.results[i])
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
        countdown: function() {
            this.remainCount = this.maxCount - this.message.length
            this.hasError = this.remainCount < 0
        },
        selectedItems() {
            var vm = this;
            this.businesses.forEach( itm => vm.$set(itm, "selected", false));
        },
        selectAll() {
            let all_s = this.allSelected;
            this.businesses.forEach( itm => itm.selected = !all_s );
        },
        submitForm(){
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
        },
        sendSms() {
            var message = "Hello, world"
            var smsNo = "https://www.isms.com.my/isms_send.php?un=smsjosh&pwd=SMSPassw0rd&dstno=63" + this.currentSelections + "&msg=" + this.message + "&type=1&sendid=MTO"
            const myString = {un: 'smsjosh', pwd: 'SMSPassw0rd', dstno: this.currentSelections, msg: message, type: '1', sendid: 'MTO'}
            //alert("SMS Sent" + myString.toString())
            const headers = {
                'Access-Control-Allow-Origin': '*'
            }
            axios.post('https://www.isms.com.my/isms_send.php', myString, {headers})
                 .then(response => {
                     console.write(response.data)
                 })
                 .catch(error => JSON.stringify(error))
            alert("SMS Sent" + smsNo)
        }
    },
    watch: {
        businesses: {
        handler() {
            this.currentSelections = this.businesses
            .filter( itm => itm.selected )
            .map( itm => itm.business_owner_number.substr(1,10))
            .join(';63')
            .toString();
        },
        deep: true
        }
    }
}
</script>

<style>

</style>
