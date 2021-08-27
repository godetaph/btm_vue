<template>
    <div class="page-edit-business">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong><span class="has-text-info">Edit</span>Business</div>
                <hr>
            </div>

                <div class="columns">
                    <div class="column is-6">
                        <div class="box ml-4">
                            <figure class="image is-128x128" v-if="!qrcode.qrcode_image">
                                <img src="https://versions.bulma.io/0.7.0/images/placeholders/128x128.png">
                            </figure>
                            <figure class="image is-128x128" v-else>
                                <img :src="qrcode.qrcode_image">
                            </figure>
                        </div>
                    </div>
                    <div class="column is-6">               
                        <div class="box ml-2">
                            <figure class="image is-128x128" v-if="!business.owner_picture">
                                <img src="https://versions.bulma.io/0.7.0/images/placeholders/128x128.png">
                            </figure>
                            <figure class="image is-128x128">
                                <img :src="business.owner_picture">
                            </figure>
                        </div>
                    </div>
                </div>
                <div class="column is-12 mb-4">
                    <div class="columns">
                        <div class="field ml-4">
                            <label for="" class="is-size-7">QR Code</label>
                            <div class="control mb-2">
                                <input type="text" style="width:250px" class="input is-small" name="qr_code" v-model="business.qr_code" disabled>
                            </div>

                            <label for="" class="is-size-7">Business code</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="business_code" v-model="business.business_code">
                            </div>
                        </div>
                    </div>
                </div>
                
                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light">Business basic information:</strong></div>
                    <!-- <div class="columns"> -->
                        <div class="column is-9">
                            <div class="field">
                                <label for="" class="is-size-7">Business name</label>
                                <div class="control">
                                    <input type="text" class="input is-small is-uppercase" name="business_name" v-model="business.business_name">
                                </div>
                            </div>
                        </div>

                        <div class="column is-3">
                            <div class="field">
                                <label for="" class="is-size-7">Owner contact no.</label>
                                <div class="control">
                                    <input type="text" class="input is-small" name="business_owner_number" v-model="business.business_owner_number">
                                </div>
                            </div>
                        </div>
                        <div class="column is-9">
                            <div class="field">
                                <label for="" class="is-size-7">Business owner name</label>
                                <div class="control">
                                    <input type="text" class="input is-small is-uppercase" name="business_owner_name" v-model="business.business_owner_name">
                                </div>
                            </div>
                        </div>
                        
                        <div class="column is-2">
                            <label for="" class="is-size-7">Gender</label>
                            <div class="select is-small">
                                <select name="gender" id="" v-model="business.owner_gender">
                                    <option value="" selected>-- Select gender --</option>
                                    <option value="male">Male</option>
                                    <option value="female">Female</option>
                                </select>
                            </div>
                        </div>
                        <div class="column is-6">
                            <div class="field">
                                <label for="" class="is-size-7">Representative name</label>
                                <div class="control">
                                    <input type="text" class="input is-small is-uppercase" name="business_representative" v-model="business.business_representative">
                                </div>
                            </div>
                        </div>
                    <!-- </div> -->

                    <div class="column is-12 "><strong class="is-size-7 has-text-grey-light">Address and GPS Location:</strong></div>
                    <div class="column is-5">
                        <label for="" class="is-size-7">Barangay</label>
                        <div class="select is-small">
                            <select name="barangay" id="" v-model="business.barangay">
                                <option value="" selected>-- Select barangay --</option>
                                <option v-for="barangay in barangays" v-bind:key="barangay.id" v-bind:value="barangay.id">{{barangay.barangay_name}}</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-3">
                        <div class="field">
                            <label for="" class="is-size-7">Purok</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="purok" v-model="business.purok">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">Stall No.</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="stall_no" v-model="business.stall_no">
                            </div>
                        </div>
                    </div>
                    
                    
                    <div class="column is-3">
                        <div class="field">
                            <label for="" class="is-size-7">GPS Lattitude</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="gps_latitude" v-model="business.gps_latitude">
                            </div>
                        </div>
                    </div>
                    <div class="column is-3">
                        <div class="field">
                            <label for="" class="is-size-7">GPS Longitude</label>
                            <div class="contol">
                                <input type="text" class="input is-small" name="gps_longitude" v-model="business.gps_longitude">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">GPS Altitude</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="gps_altitud" v-model="business.gps_altitud">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field" >
                            <label for="" class="is-size-7">GPS Accuracy</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="gps_accuracy" v-model="business.gps_accuracy">
                            </div>
                        </div>
                    </div>

                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light">Ownership:</strong></div>
                    <div class="column is-5">
                        <label for="" class="is-size-7">Ownership type</label>
                            <div class="select is-small">
                                <select name="ownership_type" id="" v-model="business.ownership_type">
                                    <option value="">-- Select ownership --</option>
                                    <option value="single">Single Proprietor</option>
                                    <option value="partnership">Partnership</option>
                                    <option value="corporation">Corporation</option>
                                    <option value="cooperative">Cooperative</option>
                                </select>
                            </div>
                    </div>
                    <div class="column is-3">
                        <label for="" class="is-size-7">Business permit</label>
                        <div class="select is-small">
                            <select name="is_business_permit" id="" v-model="business.is_business_permit">
                                <option value="">-- Select business permit? --</option>
                                <option value="yes">Yes</option>
                                <option value="no">No</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-4" v-if="business.is_business_permit=='no'">
                        <label for="" class="is-size-7">Business permit status</label>
                        <div class="select is-small">
                            <select name="business_permit_status" id="" v-model="business.business_permit_status">
                                <option value="" selected>-- Select business status --</option>
                                <option value="FIRST">First notice</option>
                                <option value="SECOND">Second notice</option>
                                <option value="FINAL">Third notice</option>
                                <option value="CLOSURE">Subject for closure</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-3" v-if="business.business_permit_status">
                        <label for="" class="is-size-7">Notice status</label>
                        <div class="select is-small">
                            <select name="is_notice" id="" v-model="business.is_notice">
                                <option value="">-- Select --</option>
                                <option value="serve">Serve</option>
                                <option value="unserve">Unserve</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-9" v-if="business.is_notice">
                        <div class="field">
                            <label for="" class="is-size-7">Notice status remarks</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="notice_remarks" v-model="business.notice_remarks">
                            </div>
                        </div>
                    </div>
                    
                    <div class="column is-4">
                        <label for="" class="is-size-7">Business status</label>
                        <div class="select is-small">
                            <select name="business_status" id="" v-model="business.business_status">
                                <option value="" selected>-- Select business status --</option>
                                <option value="ACTIVE1">Active w/o extension</option>
                                <option value="ACTIVE2">Active with extension</option>
                                <option value="INACTIVE">Inactive</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-4" v-if="business.business_status=='ACTIVE1'">
                        <label for="" class="is-size-7">Payment type</label>
                        <div class="select is-small">
                            <select name="business_status" id="" v-model="business.payment_type">
                                <option value="" selected>-- Select payment type --</option>
                                <option value="annual">Annual</option>
                                <option value="semi-annual">Semi-annual</option>
                                <option value="quarterly">Quarter</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-8" v-if="business.business_status=='INACTIVE'">
                        <label for="" class="is-size-7">Reason for inactivity</label>
                        <div class="select is-small">
                            <select name="inactive_reason" id="" v-model="business.inactive_reason">
                                <option value="" selected>-- Select reason inactivity --</option>
                                <option value="temporary">Temporary closed</option>
                                <option value="suspended">Suspended</option>
                                <option value="closed">Closed</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-6" v-if="business.business_status=='INACTIVE'">
                        <div class="field">
                            <label for="" class="is-size-7">Inactivity reason</label>
                            <div class="control">
                                <input type="text" class="input is-small" v-model="business.inactivity_reason">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6" v-if="business.business_status=='INACTIVE'">
                        <div class="field">
                            <label for="" class="is-size-7">Inactivity remarks</label>
                            <div class="control">
                                <input type="text" class="input is-small" v-model="business.inactivity_remarks">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">Annual payable</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" name="annual_amount" v-model="business.annual_amount">
                            </div>
                        </div>
                    </div>
                    <column class="column is-12"><strong class="is-size-7 has-text-grey-light">FSIC Details:</strong></column>
                    <div class="column is-2">
                        <label for="" class="is-size-7">FSIC?</label>
                        <div class="select is-small">
                            <select name="fsic" id="" v-model="business.fsic">
                                <option value="" selected>-- Select --</option>
                                <option value="yes">Yes</option>
                                <option value="no">No</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-2" v-if="business.fsic=='yes'">
                        <div class="field">
                            <label for="" class="is-size-7">FSIC Number</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="fsic_number" v-model="business.fsic_number">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <label for="" class="is-size-7">Location status</label>
                        <div class="select is-small">
                            <select name="location_status" id="" v-model="business.location_status">
                                <option value="" selected>-- Select --</option>
                                <option value="owned">Owned</option>
                                <option value="rented">Rented</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-2" v-if="business.location_status=='rented'">
                        <div class="field">
                            <label for="" class="is-size-7">Rental amount</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" name="location_rental_amount" v-model="business.location_rental_amount">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6" v-if="business.location_status=='rented'">
                        <div class="field">
                            <label for="" class="is-size-7">Lessor name</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="lessor_name" v-model="business.lessor_name">
                            </div>
                        </div>
                        
                    </div>
                    <div class="column is-2">
                        <label for="" class="is-size-7">Application status</label>
                        <div class="select is-small">
                            <select name="applicationn_status" id="" v-model="business.application_status">  
                                <option value="" selected>-- Select --</option>
                                <option value="new">New</option>
                                <option value="renew">Renewal</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">Capital amount</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" v-model="business.capitalization_amount">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">Gross sales</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" v-model="business.gross_sale_amount">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">Total employees</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" v-model="business.total_employees">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">Total male</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" v-model="business.total_male">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="" class="is-size-7">Total female</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" v-model="business.total_female">
                            </div>
                        </div>
                    </div>
                    
                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light">Categories:</strong></div>
                    <div class="column is-12">
                        <div class="columns is-multiline">
                            <!-- <div class="column is-6">
                                <label for="" class="is-size-7">Categories</label>
                                <div class="select is-small">
                                    <select name="" id="" class="select">
                                        <option value="">Select categories</option>
                                        <option v-for="category in categories" :key="category.id" :value="category.id">{{category.category_name}}</option>
                                    </select>
                                </div>
                            </div> -->
                            <!-- <div class="column is-2">
                                <div class="field">
                                    <div class="control">
                                        <button class="button is-success is-small mt-5" @click="addCategory">
                                            Add category
                                        </button>
                                    </div>
                                </div>
                            </div> -->
                            <div class="column is-12 notification is-light" v-if="business_categories.length > 0">
                                <label v-for="business_category in business_categories" :key="business_category.id" class="ml-1">
                                    <span class="tag is-info">{{business_category.cat_name}}</span>
                                </label>
                            </div>
                             <div class="column is-12 notification is-light" v-if="business_categories.length == 0">
                                <p class="tag is-warning">No categories added</p>
                                <p class="mt-4"><router-link :to="{name: 'BusinessCategories', params: {id:business.id}}" class="has-text-link is-size-7">Click to add categories</router-link></p>
                                
                            </div>
                        </div>
                    </div>

                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light">Owner/Goods/Business pictures:</strong></div>
                    <div class="column is-12">
                        <div class="field">
                            <label for="" class="is-size-7">Owner picture</label>
                            <div class="control" v-if="!business.owner_picture">
                                <input type="file" @change="onFileChange" class="input is-small" name="owner_picture">
                            </div>
                            <div v-else>
                                <img :src="business.owner_picture" alt=""
                                    :class="{ full: fullWidthImage }" @click="fullWidthImage = !fullWidthImage">
                                    <p><button class="is-light" @click="removeImage('owner_picture')">Remove</button></p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-12">
                        <div class="field">
                            <label for="" class="is-size-7">Goods/services</label>
                            <div class="control" v-if="!business.goods_services_picture">
                                <input type="file" @change="onFileChange" class="input is-small" name="goods_picture">
                            </div>
                            <div v-else>
                                <img :src="business.goods_services_picture" alt="" :class="{ full: fullWidthImage }" 
                                @click="fullWidthImage = !fullWidthImage">
                                <p><button class="is-light" @click="removeImage('goods_picture')">Remove</button></p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-12">
                        <div class="field">
                            <label for="" class="is-size-7">Business permit</label>
                            <div class="control" v-if="!business.business_permit_picture">
                                <input type="file" @change="onFileChange" class="input is-small" name="permit">
                            </div>
                            <div class="" v-else>
                                <img :src="business.business_permit_picture" alt="" :class="{ full: fullWidthImage }" 
                                @click="fullWidthImage = !fullWidthImage">
                                <p><button class="is-light" @click="removeImage('permit')">Remove</button></p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-12">
                        <div class="field">
                            <label for="" class="is-size-7">Owner signature</label>
                            <div class="control" v-if="!business.owner_signature">
                                <input type="file" @change="onFileChange" class="input is-small" name="owner_signature">
                            </div>
                            <div class="" v-else>
                                <img :src="business.owner_signature" alt="" :class="{ full: fullWidthImage }" 
                                @click="fullWidthImage = !fullWidthImage">
                                <p><button class="is-light" @click="removeImage('owner_signature')">Remove</button></p>
                            </div>
                        </div>
                    </div>

                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light">Other pictures:</strong></div>
                    <div class="column is-6">
                        <div class="field">
                            <label for="" class="is-size-7">Picture 1</label>
                            <div class="control" v-if="!business.picture1">
                                <input type="file" @change="onFileChange" class="input is-small" name="picture1">
                            </div>
                            <div class="" v-else>
                                <img :src="business.picture1" alt="" :class="{ full: fullWidthImage }" 
                                @click="fullWidthImage = !fullWidthImage">
                                <p><button class="is-light" @click="removeImage('picture1')">Remove</button></p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <label for="" class="is-size-7">Picture 2</label>
                            <div class="control" v-if="!business.picture2">
                                <input type="file" @change="onFileChange" class="input is-small" name="picture2">
                            </div>
                            <div class="" v-else>
                                <img :src="business.picture2" alt="" :class="{ full: fullWidthImage }" 
                                @click="fullWidthImage = !fullWidthImage">
                                <p><button class="is-light" @click="removeImage('picture2')">Remove</button></p>
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <label for="" class="is-size-7">Picture 3</label>
                            <div class="control" v-if="!business.picture3">
                                <input type="file" @change="onFileChange" class="input is-small" name="picture3">
                            </div>
                            <div class="" v-else>
                                <img :src="business.picture3" alt="" :class="{ full: fullWidthImage }" 
                                @click="fullWidthImage = !fullWidthImage">
                                <p><button class="is-light" @click="removeImage('picture3')">Remove</button></p>
                            </div>
                        </div>
                    </div>

                    <div class="column is-12"><strong>Collector information:</strong></div>    
                    <div class="column is-12"><strong>{{$store.state.user.username}}</strong></div>

                    <div class="column is-12">
                            <button class="button is-success" @click="submitForm">Submit</button>
                    </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'EditBusiness',
    data() {
        return {
            business: {},
            barangays: [],
            qrcode: {},
            qr_id: '',
            categories: [],
            business_categories: [],
            fullWidthImage: false,
            owner_picture:'',
            goods_picture:'',
            permit:'',
            owner_signature: '',
            picture1: '',
            picture2: '',
            picture3: '',
            is_owner_pic: false,
            is_goods_pic: false
        }
    },
    mounted() {
        this.getBarangays(),
        this.getCategories(),
        this.getBusiness(),
        this.getBusinessCategories()
    },
    methods: {
        getQrcode(qrcode) {
            axios.get(`/api/v1/qrcodes?qr_code=${qrcode}`)
                 .then(response => {
                     this.qrcode=response.data[0]
                     console.log(this.qrcode.id + ' - qrcode1')
                     this.qr_id = this.qrcode.id
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        onFileChange(e){
            console.log(e)
            let inputName = e.srcElement.name;
            switch(inputName){
                case "owner_picture":
                    this.owner_picture = e.target.files[0]
                    // this.business.owner_picture=e.target.files[0]
                    console.log(this.business.owner_picture)
                    console.log(this.owner_picture)
                    this.is_owner_pic=true
                    break;
                case "goods_picture":
                    this.goods_picture = e.target.files[0]
                    // this.business.goods_services_picture = e.target.files[0]
                    this.is_goods_pic=true
                    console.log(this.goods_picture + " 01")
                    console.log(this.business.goods_services_picture + "02")
                    break;
                case "permit":
                    this.permit=e.target.files[0]
                    break;
                case "owner_signature":
                    this.owner_signature=e.target.files[0]
                    break;
                case "picture1":
                    this.picture1=e.target.files[0]
                    break;
                case "picture2":
                    this.picture2=e.target.files[0]
                    break;
                case "picture3":
                    this.picture3=e.target.files[0]
                    break;
            }
            // pict = URL.createObjectURL(this.file)
        },
        removeImage(inputData){
            console.log(inputData)
            switch(inputData){
                case 'owner_picture':
                    this.business.owner_picture = ''
                    break;
                case 'goods_picture':
                    this.business.goods_services_picture=''
                    break;
            }
            console.log(this.business.owner_picture)
        },
        getBarangays() {
            axios.get("/api/v1/barangays/?size=100")
                 .then(response => {
                     this.barangays = response.data.results
                 })
                 .catch(error => {
                     console.response(JSON.stringify(error))
                 })
        },
        getCategories() {
            axios.get("/api/v1/categories/?size=200")
                 .then(response => {
                     this.categories = response.data.results
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusiness(){
            const businessId = this.$route.params.id
            axios.get(`/api/v1/businesses/${businessId}/`)
                 .then(response => {
                     this.business = response.data
                     this.getQrcode(this.business.qr_code)
                     console.log(this.business)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusinessCategories(){
            const businessId=this.$route.params.id
            axios.get(`/api/v1/business-categories?business=${businessId}`)
                 .then(response => {
                     console.log(response)
                     for (let i = 0; i < response.data.length; i++) {
                         this.business_categories.push(response.data[i])
                     }
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm(){
            const businessId = this.$route.params.id
            //console.log(this.business)
            this.business.submitted_from = 'web'
            this.business.created_by = this.$store.state.user.id
            this.business.modified_by = this.$store.state.user.id

            let formData = new FormData();
            if (this.owner_picture){
                this.business.owner_picture=this.owner_picture
                formData.append('owner_picture', this.business.owner_picture)
            }
            if (this.goods_picture){
                this.business.goods_services_picture = this.goods_picture
                formData.append('goods_picture', this.business.goods_services_picture)
            }
            if (this.permit){
                this.business.business_permit_picture=this.permit
                formData.append('permit', this.business.business_permit_picture)
            }
            if (this.owner_signature){
                this.business.owner_signature=this.owner_signature
                formData.append('owner_signature', this.business.owner_signature)
            }
            if (this.picture1){
                this.business.picture1=this.picture1
                formData.append('picture1', this.business.picture1)
            }
            if (this.picture2){
                this.business.picture2=this.picture2
                formData.append('picture2', this.business.picture2)
            }
            if (this.picture3){
                this.business.picture3=this.picture3
                formData.append('picture3', this.business.picture3)
            }
            formData.append('qr_code', this.business.qr_code)
            // formData.append('qrcode', this.business.qrcode)
            formData.append('business_code', this.business.business_code)
            formData.append('business_owner_number', this.business.business_owner_number)
            formData.append('business_name', this.business.business_name)
            formData.append('business_owner_name', this.business.business_owner_name)
            formData.append('owner_gender', this.business.owner_gender)
            formData.append('ownership_type', this.business.ownership_type)
            formData.append('is_business_permit', this.business.is_business_permit)
            formData.append('business_permit_status', this.business.business_permit_status)
            formData.append('is_notice', this.business.is_notice)
            formData.append('notice_remarks', this.business.notice_remarks)
            formData.append('business_status', this.business.business_status)
            formData.append('payment_type', this.business.payment_type)
            formData.append('annual_amount', this.business.annual_amount)
            formData.append('inactive_remarks', this.business.inactive_remarks)
            formData.append('inactive_reason', this.business.inactive_reason)
            formData.append('fsic', this.business.fsic)
            formData.append('fsic_number', this.business.fsic_number)
            formData.append('capitalization_amount', this.business.capitalization_amount)

            formData.append('gross_sale_amount', this.business.gross_sale_amount)
            formData.append('total_employees', this.business.total_employees)
            formData.append('total_male', this.business.total_male)
            formData.append('total_female', this.business.total_female)

            formData.append('location_status', this.business.location_status)
            formData.append('application_status', this.business.application_status)
            if (this.business.location_rental_amount != null)
                formData.append('location_rental_amount', this.business.location_rental_amount)  
            formData.append('lessor_name', this.business.lessor_name)
            formData.append('purok', this.business.purok)
            formData.append('stall_no', this.business.stall_no)

            formData.append('gps_altitud', this.business.gps_altitud)
            formData.append('gps_longitude', this.business.gps_longitude)
            formData.append('gps_latitude', this.business.gps_latitude)
            formData.append('gps_accuracy', this.business.gps_accuracy)
            formData.append('business_representative', this.business.business_representative)
            formData.append('barangay', this.business.barangay)
            formData.append('submitted_from', this.business.submitted_from)
            formData.append('created_by', this.business.created_by)
            formData.append('modified_by', this.business.modified_by)

            // this.business.qrcode = "\\" + this.qrcode.id
            

            //console.log(this.formData)
            console.log(this.business)

            axios.patch(`/api/v1/businesses/${businessId}/`, formData)
                 .then(response => {
                     toast ({
                        message: 'New business was added successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     this.$router.push("/dashboard/businesses")
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>

<style scoped>
    .full {
        width: 100%;
        height: auto;
    }
    img {
        width: 150px;
        border-radius: 2px;
        box-shadow: 1px 1px 3px 1px rgba(0, 0, 0, 0.5);
        transition: width 1s;
    }
        img:hover {
        cursor: pointer;
    }
</style>