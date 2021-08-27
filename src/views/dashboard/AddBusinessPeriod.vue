<template>
    <div class="page-add-business-period">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Add business map</div>
                <hr>
            
                <div class="box mt-4">
                    <p class="title is-5 has-text-primary"><strong>{{business.business_name}}</strong></p>
                    <p>Owner: <strong>{{business.business_owner_name}}</strong> </p>
                    <p v-if="business.barangay">Barangay: <strong>{{business.barangay.barangay_name}}</strong></p>
                    <p v-if="business.category">Category: <strong>{{business.category}}</strong></p>
                    <p v-if="business.business_status">Status: <strong>{{business.business_status}}</strong></p>
                    <p v-if="business.capitalization_amount">Capitalization: <strong>{{business.capitalization_amount}}</strong></p>
                    <p v-if="business.gross_sale_amount">Gross sales: <strong>{{business.gross_sale_amount}}</strong></p>
                </div> 
                <div class="column is-12 title is-5">Transaction detail</div>
                <div class="column is-6">
                    <label for="">Period: <strong>{{period.period_year}} (Active)</strong></label>
                    <!-- <div class="select" >
                        <select name="" id="" class="select"  v-model="business_period.period">
                            <option value="">--Select period--</option>
                            <option v-for="period in periods" v-bind:key="period.id" :value="period.id">{{period.period_year}}</option>
                        </select>
                    </div> -->

                </div>
                <div class="column is-12">
                    <label for="">Comment/Notice</label>
                    <div class="control">
                        <textarea name="" id="" rows="10" class="textarea" v-model="business_period.comment"></textarea>
                    </div>
                </div>
                <div class="column is-6">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Submit data</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'AddBusinessPeriod',
    data() {
        return {
            business:{
                id:''
            },
            business_period: {},
            periods:[],
            period: {}
        }
    },
    async mounted() {
        await this.getPeriods()
        await this.getBusiness()
    },
    methods: {
        getPeriods(){
            axios.get(`/api/v1/periods/`)
                 .then(response => {
                        this.periods=response.data
                        this.period=this.periods.find(p => p.is_active==true)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusiness(){
            const businessId=this.$route.params.id
            axios.get(`/api/v1/businesses/${businessId}/`)
                 .then(response => {
                     this.business=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm(){
            this.business_period.business=this.business.id
            this.business_period.period=this.period.id
            this.business_period.created_by=this.$store.state.user.id
            this.business_period.collector=this.$store.state.user.id
            console.log(this.business_period)
            axios.post('/api/v1/business-periods/', this.business_period)
                 .then(response => {
                     console.log(response.statusText)
                     toast ({
                        message: 'New business was added successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     this.countNotification()
                     this.$router.push("/dashboard/business-periods")
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        countNotification(){
            axios.get(`/api/v1/notifications?is_read=False`)
                .then(response => {
                    this.$store.commit('countNotification', response.data.count)
                    console.log(response)
                    console.log(this.$store.state.notificationCount)
                    //this.$emit('countNotes', response.data.length)
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }, 
    }

}
</script>