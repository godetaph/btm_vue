<template>
    <div class="page-add-business">
        <div class="columns is-multiline is-mobile">
                <div class="column is-12">
                    <div class="is-size-5"><strong>BTM</strong><span class="has-text-info">Add</span>Business</div>
                    <hr>
                </div>

                    <div class="box ml-4">
                        <figure class="image is-128x128" v-if="!business.qrcode_url">
                            <img src="https://versions.bulma.io/0.7.0/images/placeholders/128x128.png">
                        </figure>
                        <figure class="image is-128x128" v-else>
                            <img :src="business.qrcode_url" alt="">
                        </figure>
                    </div>

                    <div class="column is-12 is-size-6 mt-4"><strong class="is-size-7 has-text-grey-light">Business basic information:</strong></div>
                    <div class="column is-3">
                        <div class="field">
                            <label for="">QR Code</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="qr_code" v-model="business.qr_code" disabled>
                            </div>

                            <label for="">Business code</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="qr_code" v-model="business.business_code">
                            </div>
                        </div>
                    </div>
                    <div class="column is-9">
                        <div class="field">
                            <label for="">Business name</label>
                            <div class="control">
                                <input type="text" class="input is-small is-uppercase" name="business_name" v-model="business.business_name">
                            </div>
                        </div>
                    </div>

                    <div class="column is-3">
                        <div class="field">
                            <label for="">Owner contact no.</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="business_owner_number" v-model="business.business_owner_number">
                            </div>
                        </div>
                    </div>
                    <div class="column is-9">
                        <div class="field">
                            <label for="">Business owner name</label>
                            <div class="control">
                                <input type="text" class="input is-small is-uppercase" name="business_owner_name" v-model="business.business_owner_name">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div>Gender</div>
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
                            <label for="">Representative name</label>
                            <div class="control">
                                <input type="text" class="input is-small is-uppercase" name="business_representative" v-model="business.business_representative">
                            </div>
                        </div>
                    </div>

                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light"> Address and GPS Location:</strong></div>
                    <div class="column is-5">
                        <div class="">Barangay</div>
                        <div class="select is-small">
                            <select name="barangay" id="" v-model="business.barangay">
                                <option value="" selected>-- Select barangay --</option>
                                <option v-for="barangay in barangays" v-bind:key="barangay.id" v-bind:value="barangay.id">{{barangay.barangay_name}}</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-3">
                        <div class="field">
                            <label for="">Purok</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="purok" v-model="business.purok">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">Stall No.</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="stall_no" v-model="business.stall_no">
                            </div>
                        </div>
                    </div>
                    
                    
                    <div class="column is-3">
                        <div class="field">
                            <label for="">GPS Lattitude</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="gps_latitude" v-model="business.gps_latitude">
                            </div>
                        </div>
                    </div>
                    <div class="column is-3">
                        <div class="field">
                            <label for="">GPS Longitude</label>
                            <div class="contol">
                                <input type="text" class="input is-small" name="gps_longitude" v-model="business.gps_longitude">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">GPS Altitude</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="gps_altitud" v-model="business.gps_altitud">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">GPS Accuracy</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="gps_accuracy" v-model="business.gps_accuracy">
                            </div>
                        </div>
                    </div>

                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light">Ownership:</strong></div>
                    <div class="column is-5">
                        <div class="">Ownership type</div>
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
                        <div class="">Business permit?</div>
                        <div class="select is-small">
                            <select name="is_business_permit" id="" v-model="business.is_business_permit">
                                <option value="">-- Select business permit? --</option>
                                <option value="yes">Yes</option>
                                <option value="no">No</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-4" v-if="business.is_business_permit=='no'">
                        <div class="">Business permit status</div>
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
                        <div class="">Notice status</div>
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
                            <label for="">Notice status remarks</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="notice_remarks" v-model="business.notice_remarks">
                            </div>
                        </div>
                    </div>
                    
                    <div class="column is-4">
                        <div>Business status</div>
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
                        <div>Payment type</div>
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
                        <div>Reason for inactivity</div>
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
                            <label for="">Inactivity reason</label>
                            <div class="control">
                                <input type="text" class="input is-small" v-model="business.inactivity_reason">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6" v-if="business.business_status=='INACTIVE'">
                        <div class="field">
                            <label for="">Inactivity remarks</label>
                            <div class="control">
                                <input type="text" class="input is-small" v-model="business.inactivity_remarks">
                            </div>
                        </div>
                    </div>
                    <column class="column is-12"><strong>FSIC Details:</strong></column>
                    <div class="column is-1">
                        <label for="">FSIC?</label>
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
                            <label for="">FSIC Number</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="fsic_number" v-model="business.fsic_number">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div>Status</div>
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
                            <label for="">Rental amount</label>
                            <div class="control">
                                <input type="number" class="input is-small" name="location_rental_amount" v-model="business.location_rental_amount">
                            </div>
                        </div>
                    </div>
                    <div class="column is-5" v-if="business.location_status=='rented'">
                        <div class="field">
                            <label for="">Lessor name</label>
                            <div class="control">
                                <input type="text" class="input is-small" name="lessor_name" v-model="business.lessor_name">
                            </div>
                        </div>
                        
                    </div>
                    <div class="column is-2">
                        <div>Application status</div>
                        <div class="select is-small">
                            <select name="applicationn_status" id="" v-model="business.application_status">  
                                <option value="">-- Select --</option>
                                <option value="new">New</option>
                                <option value="renew">Renewal</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">Capital amount</label>
                            <div class="control">
                                <input type="number" class="input is-small" v-model="business.capitalization_amount">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">Gross sales</label>
                            <div class="control">
                                <input type="number" class="input is-small" v-model="business.gross_sale_amount">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">Total employees</label>
                            <div class="control">
                                <input type="number" class="input is-small" v-model="business.total_employees">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">Total male</label>
                            <div class="control">
                                <input type="number" class="input is-small" v-model="business.total_male">
                            </div>
                        </div>
                    </div>
                    <div class="column is-2">
                        <div class="field">
                            <label for="">Total female</label>
                            <div class="control">
                                <input type="number" class="input is-small" v-model="business.total_female">
                            </div>
                        </div>
                    </div>
                    <div class="column is-12"><strong class="is-size-7 has-text-grey-light">Owner/Goods/Business pictures:</strong></div>
                    <div class="column is-4">
                        <div class="field">
                            <label for="">Owner picture</label>
                            <div class="control">
                                <input type="file" @change="onFileChange" class="input is-small" name="owner_picture">
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="field">
                            <label for="">Goods/services</label>
                            <div class="control">
                                <input type="file" @change="onFileChange" class="input is-small" name="goods_picture">
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="field">
                            <label for="">Business permit</label>
                            <div class="control">
                                <input type="file" @change="onFileChange" class="input is-small" name="business_permit">
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="field">
                            <label for="">Owner signature</label>
                            <div class="control">
                                <input type="file" @change="onFileChange" class="input is-small" name="owner_signature">
                            </div>
                        </div>
                    </div>

                    <div class="column is-12"><strong>Other pictures:</strong></div>
                    <div class="column is-4">
                        <div class="field">
                            <label for="">Picture 1</label>
                            <div class="control">
                                <input type="file" @change="onFileChange" class="input is-small" name="picture1">
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="field">
                            <label for="">Picture 2</label>
                            <div class="control">
                                <input type="file" @change="onFileChange" class="input is-small" name="picture2">
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="field">
                            <label for="">Picture 3</label>
                            <div class="control">
                                <input type="file" @change="onFileChange" class="input is-small" name="picture3">
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
import {toast} from 'bulma-toast'
export default {
    name: 'Business',
    data() {
        return {
            busines: {},
            owner_picture: null,
            goods_picture: null,
            business_permit: null,
            owner_signature: null,
            picture1: null,
            picture2: null,
            picture3: null,
            qrcode:{
                qrcode:'',
                qrcode_image:''
            },
            business: {},
            barangays: [],
            errors: []
        }
    },
    mounted() {
        // this.createQrcode()
        this.createBusiness()
        this.getBarangays()
        //await this.getCategories()
        
    },
    methods: {
        createBusiness(){
            axios.get('/api/v1/businesses/?qrcode=true')
                 .then(response => {
                     this.business=response.data[0]
                     console.log(this.business)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        createQrcode(){
            axios.get('/api/v1/qrcodes/')
                 .then(response => {
                     this.qrcode=response.data[0]
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },  
        getBarangays() {
            axios.get('/api/v1/barangays/?size=200')
                 .then(response => {
                     this.barangays = response.data.results
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        // getCategories() {
        //     axios.get('/api/v1/categories/')
        //          .then(response => {
        //              this.categories = response.data
        //          })
        //          .catch(error => {
        //              console.log(JSON.stringify(error))
        //          })
        // },
        onFileChange(e) {
            console.log(e)
            let inputName = e.srcElement.name;
            console.log(e.srcElement.name)
            switch(inputName){
                case "owner_picture":
                    this.owner_picture = e.target.files[0]
                    break;
                case "goods_picture":
                    this.goods_picture = e.target.files[0]
                    break;
                case "business_permit":
                    this.business_permit=e.target.files[0]
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
        },
        submitForm(){
            let formData = new FormData();
            // if (this.owner_picture != null)
            //     formData.append('owner_picture', this.owner_picture, this.owner_picture.name)
            // if (this.goods_picture != null)
            //     formData.append('goods_picture', this.goods_picture, this.goods_picture.name)
            // if (this.business_permit != null)
            //     formData.append('business_permit', this.business_permit, this.business_permit.name)
            // if (this.owner_signature != null)
            //     formData.append('owner_signature', this.owner_signature, this.owner_signature.name)
            // if (this.picture1 != null)
            //     formData.append('picture1', this.picture1, this.picture1.name)
            // if (this.picture2 != null)
            //     formData.append('picture2', this.picture2, this.picture2.name)
            // if (this.picture2 != null)
            //     formData.append('picture2', this.picture2, this.picture2.name)
            // if (this.picture3 != null)
            //     formData.append('picture3', this.picture3, this.picture3.name)

            // formData.append('qrcode', this.business.qrcode)
            // formData.append('business_owner_number', this.business.business_owner_number)
            // formData.append('business_name', this.business.business_name)
            // formData.append('business_owner_name', this.business.business_owner_name)
            // formData.append('owner_gender', this.business.owner_gender)
            // formData.append('ownership_type', this.business.ownership_type)
            // formData.append('is_business_permit', this.business.is_business_permit)
            // formData.append('business_permit_status', this.business.business_permit_status)
            // formData.append('is_notice', this.business.is_notice)
            // formData.append('notice_remarks', this.business.notice_remarks)
            // formData.append('business_status', this.business.business_status)
            // formData.append('payment_type', this.business.payment_type)
            // formData.append('inactive_remarks', this.business.inactive_remarks)
            // formData.append('inactive_reason', this.business.inactive_reason)
            // formData.append('fsic', this.business.fsic)
            // formData.append('fsic_number', this.business.fsic_number)
            // formData.append('capitalization_amount', this.business.capitalization_amount)
            // formData.append('gross_sale_amount', this.business.gross_sale_amount)
            // formData.append('total_employees', this.business.total_employees)
            // formData.append('total_male', this.business.total_male)
            // formData.append('total_female', this.business.total_female)
            // formData.append('location_status', this.business.location_status)
            // formData.append('application_status', this.business.application_status)
            // formData.append('location_rental_amount', this.business.location_rental_amount)
            // formData.append('lessor_name', this.business.lessor_name)
            // formData.append('purok', this.business.purok)
            // formData.append('stall_no', this.business.stall_no)
            // formData.append('gps_altitud', this.business.gps_altitud)
            // formData.append('gps_longitude', this.business.gps_longitude)
            // formData.append('gps_latitude', this.business.gps_latitude)
            // formData.append('gps_accuracy', this.business.gps_accuracy)
            // formData.append('business_representative', this.business.business_representative)
            // formData.append('barangay', this.business.barangay)

            this.business.submitted_from = 'web'
            this.business.created_by = this.$store.state.user.id

            console.log(this.business)
            axios.patch(`/api/v1/businesses/${this.business.id}/`, this.business)
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

<style lang="scss">
    .select, .select select {
        width: 100%;
    }
</style>