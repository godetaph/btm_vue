<template>
    <div class="page-business">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Business detail</div>
                <hr>
            </div>

            <div class="box ml-4">
                <figure class="image is-128x128" v-if="!qrcode.qrcode_image">
                    <img src="https://versions.bulma.io/0.7.0/images/placeholders/128x128.png">
                </figure>
                <figure class="image is-128x128" v-else>
                    <img :src="qrcode.qrcode_image">
                </figure>
            </div>
            <div class="box ml-4">
                <figure class="image is-128x128" v-if="!business.owner_picture">
                    <img src="https://versions.bulma.io/0.7.0/images/placeholders/128x128.png">
                </figure>
                <figure class="image is-128x128">
                    <img :src="business.owner_picture">
                </figure>
            </div>
            <div class="column is-8">
                <div class="buttons is-pulled-right">
                    <router-link :to="{name: 'EditBusiness', params: {id:business.id}}" class="button is-info is-small">Edit</router-link>
                    <button class="button is-danger is-small" @click="deleteBusiness(business)" v-if="level=='admin'">Delete</button>
                </div>
            </div>
            <div class="column is-6">
                <div class="box mt-2">
                    <div class="title is-4 has-text-primary is-uppercase">{{business.business_name}}</div>
                    <div class="mb-2"><strong class="is-size-7 has-text-grey">Basic information</strong></div>
                    <p>Owner: <strong>{{business.business_owner_name}}</strong> </p>
                    <p v-if="business.owner_gender">Gender: <strong>{{business.owner_gender}}</strong></p>
                    <p v-if="business.barangay">Barangay: <strong>{{business.bar_name}}, </strong>Purok: <strong v-if="business.purok">{{business.purok}}, </strong> Stall no.: <strong v-if="business.stall_no">{{business.stall_no}}</strong></p>
                    <p v-if="business.business_owner_number">Contact no.: <strong>{{business.business_owner_number}}</strong></p>
                    <p v-if="business.business_representative">Representative: <strong>{{business.business_representative}}</strong></p>
                    
                    <div class="mb-2 mt-4"><strong class="is-size-7 has-text-grey">Ownership</strong></div>
                    <p v-if="business.ownership_type=='single'">Type: <strong>Single proprietor</strong></p>
                    <p v-if="business.ownership_type=='partnership'">Type: <strong>Partnership</strong></p>
                    <p v-if="business.ownership_type=='corporation'">Type: <strong>Corporation</strong></p>
                    <p v-if="business.ownership_type=='cooperative'">Type: <strong>Cooperativer</strong></p>
                    <p v-if="business.is_business_permit=='yes'">Business permit: <span class="tag is-primary">Yes</span></p>
                    <p v-else>Business permit: <span class="tag is-danger">No</span></p>
                    <p v-if="business.business_permit_status=='FIRST'">Business permit status: <span class="tag is-primary">First notice</span></p>
                    <p v-if="business.business_permit_status=='SECOND'">Business permit status: <span class="tag is-info">Second notice</span></p>
                    <p v-if="business.business_permit_status=='FINAL'">Business permit status: <span class="tag is-warning">Third notive</span></p>
                    <p v-if="business.business_permit_status=='CLOSURE'">Business permit status: <span class="tag is-danger">Subject for closure</span></p>
                    <p v-if="business.is_notice=='serve'">Business permit notice: <span class="tag is-primary">Serve</span></p>
                    <p v-else>Business permit notice: <span class="tag is-warning">Unserve</span></p>
                    <p v-if="business.notice_remarks">Business notice remarks: <strong>{{business.notice_remarks}}</strong></p>
                    <p v-if="business.business_status=='ACTIVE1'">Business status: <strong>Active w/o extension</strong></p>
                    <p v-if="business.business_status=='ACTIVE2'">Business status: <strong>Active with extension</strong></p>
                    <p v-if="business.business_status=='INACTIVE'">Business status: <strong>Inactive</strong></p>
                    <p v-if="business.inactive_remarks">Inactive remarks: <strong>{{business.inactive_remarks}}</strong></p>
                    <p v-if="business.inactive_reason">Inactive reason: <strong>{{business.inactive_reason}}</strong></p>
                    <p v-if="business.payment_type=='annual'">Payment type: <strong>Annually</strong></p>
                    <p v-if="business.payment_type=='semi-annual'">Payment type: <strong>Semi-annually</strong></p>
                    <p v-if="business.payment_type=='quarterly'">Payment type: <strong>Quarterly</strong></p>

                    <div class="mb-2 mt-4"><strong class="is-size-7 has-text-grey">FSIC detail</strong></div>
                    <p v-if="business.fsic=='yes'">FSIC: <span class="tag is-primary">Yes</span></p>
                    <p v-else>FSIC: <span class="tag is-warning">No</span></p>
                    <p v-if="business.fsic_number">FSIC no.: <strong>{{business.fsic_number}}</strong></p>
                    <p v-if="business.application_status=='new'">Application status: <strong>New</strong></p>
                    <p v-else>Application status: <strong>Renewal</strong></p>
                    <p v-if="business.location_status=='owned'">Location status: <strong>Owned</strong></p>
                    <p v-else>Application status: <strong>Rented</strong></p>
                    <p v-if="business.location_rental_amount">Rental amount: <strong>{{business.location_rental_amount}}</strong></p>
                    <p v-if="business.lessor_name">Lessor name: <strong>{{business.lessor_name}}</strong></p>
                    <p v-if="business.capitalization_amount">Capitalization: <strong>{{business.capitalization_amount}}</strong></p>
                    <p v-if="business.gross_sale_amount">Gross sales: <strong>{{business.gross_sale_amount}}</strong></p>
                    <p v-if="business.total_employees">Total employees: <strong>{{business.total_employees}}</strong></p>
                    <p v-if="business.total_male">Total male: <strong>{{business.total_male}}</strong></p>
                    <p v-if="business.total_female">Total female: <strong>{{business.total_female}}</strong></p>
                </div>
            </div>
            <div class="column is-6">
                <div class="box mt-2">
                    <div class="mb-2"><strong class="is-size-7 has-text-grey">Business Location</strong>
                        <button class="button is-small is-dark is-pulled-right mb-2" @click="getLocation">Get location</button>         
                    </div>
                    <GMapMap
                        :center="center"
                        :zoom="zoom"
                        map-type-id="roadmap" 
                        style="width: 100%; height: 700px"
                    >
                        <GMapCluster>
                            <GMapMarker
                                :key="index"
                                v-for="(m, index) in markers"
                                :position="m.position"
                                :clickable="true"
                                @click="center=m.position"
                            />
                        </GMapCluster>
                    </GMapMap>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <div class="mb-2"><strong class="is-size-7 has-text-grey">Categories ({{categories.length}})</strong></div>
                    <label v-for="category in categories" v-bind:key="category.id" class="ml-2"><span class="tag is-info"> {{category.cat_name}}</span></label>
                    <!-- <ul>

                        <li v-for="category in categories" v-bind:key="category.id"><span class="tag is-light"> {{category.cat_name}}</span></li> 
                    </ul> -->
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <div class="mb-2"><strong class="is-size-7 has-text-grey">Payments</strong></div>
                    <table class="table is-fullwidth is-stripped is-narrow is-hoverable is-size-7">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Mode</th>
                                <th>Paid to</th>
                                <th>O.R. no</th>
                                <th>Amount</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="payment in payments" v-bind:key="payment.id"> 
                                <td>{{payment.payment_date}}</td>
                                <td>{{payment.payment_mode}}</td>
                                <td>{{payment.paid_to}}</td>
                                <td>{{payment.or_no}}</td>
                                <td>{{Number(payment.amount_paid).toLocaleString('en-US', {style: 'currency', currency: 'PHP', minimumFractionDigits: 2, maximumFractionDigits: 2})}}</td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <tr>
                                <td><strong>Total</strong></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td><strong>{{Number(total_paid).toLocaleString('en-US', {style: 'currency', currency: 'PHP', minimumFractionDigits: 2, maximumFractionDigits: 2})}}</strong></td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
            
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import Swal from "sweetalert2"
// import LocationMap from '../../components/LocationMap.vue'
export default {
    name: 'Business',
    // components: {LocationMap},
    data() {
        return {
            business: {},
            level: '',
            qrcode: {},
            categories: [],
            payments: [],
            total_paid: '',
            // center: { lat: 7.010607, lng: 125.091134 },
            zoom:10,
            center: { 
                lat: 7.189447, 
                lng: 124.532875 
            },
            marks: {
                position: {
                        lat:'',
                        lng:''
                    }
                },
            markers: [
            {
                position: {
                    lat: 7.189447,
                    lng: 124.532875
                }
            },
            ]
        }
    },
    mounted() {
        this.getBusiness()
    },
    methods: {
        getQrcode(qrcode) {
            axios.get(`/api/v1/qrcodes?qr_code=${qrcode}`)
                 .then(response => {
                     this.qrcode=response.data[0]
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusiness(){
            const businessId=this.$route.params.id
            this.level = this.$store.state.user.level
            axios.get(`/api/v1/businesses/${businessId}`)
                 .then(response => {
                     this.business=response.data
                     this.getQrcode(this.business.qr_code)
                     this.getCategories(this.business.id)
                     this.getPayments(this.business.id)

                    this.center.lat=parseFloat(this.business.gps_latitude)
                    // console.log(parseFloat(this.business.gps_latitude))
                    this.center.lng=parseFloat(this.business.gps_longitude)
                    // console.log(parseFloat(this.business.gps_longitude))
                    this.markers[0].position.lat=parseFloat(this.business.gps_latitude)
                    this.markers[0].position.lng=parseFloat(this.business.gps_longitude)
                    this.zoom=14
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getLocation(){
            this.center.lat=parseFloat(this.business.gps_latitude)
            console.log(parseFloat(this.business.gps_latitude))
            this.center.lng=parseFloat(this.business.gps_longitude)
            console.log(parseFloat(this.business.gps_longitude))
            this.markers[0].position.lat=parseFloat(this.business.gps_latitude)
            this.markers[0].position.lng=parseFloat(this.business.gps_longitude)
            this.zoom=16
        },
        getCategories(businessId) {
            axios.get(`/api/v1/business-categories?business=${businessId}`)
                 .then(response => {
                     for (let i = 0; i < response.data.length; i++) {
                         this.categories.push(response.data[i])
                         console.log(this.categories)
                     }
                     })
                 .catch(error => console.log(JSON.stringify(error)))
        },
        getPayments(businessId){
            axios.get(`/api/v1/payments?business=${businessId}`)
                 .then(response => {
                     for (let i = 0; i < response.data.length; i++) {
                         this.payments.push(response.data[i]); 
                         this.total_paid+=response.data[i].amount_paid
                     }
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        deleteBusiness(business){
            Swal.fire({
                title: 'You are about to delete this record.',
                // text: 'Press YES to continue.',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: 'hsl(141, 71%, 48%)',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, continue!'
            }).then((result) => {
                if (result.isConfirmed) {
                    axios.delete(`/api/v1/businesses/${business.id}`)
                     .then(response => {
                         console.log(response.statusText)
                         Swal.fire({
                            title: 'Deleted!',
                            text: 'Your record has been deleted.',
                            icon: 'success',
                            confirmButtonText: 'Confirmed.'
                         })
                         this.$router.push('/dashboard/businesses')
                     })
                     .catch(error => {
                         console.log(JSON.stringify(error))
                     })

                    
                }
            })
        }
    }
}
</script>

<style scoped>
    #tabs-with-content .tabs:not(:last-child) {
    margin-bottom: 0;
    }

    #tabs-with-content .tab-content {
    padding: 1rem;
    display: none;
    }

    #tabs-with-content .tab-content.is-active {
    display: block;
    }
</style>