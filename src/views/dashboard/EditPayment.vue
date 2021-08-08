<template>
    <div class="page-edit-payment">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Edit payment</div>
                <hr>

                <div class="box mt-4" v-if="payment.business">
                    <p class="title is-5 has-text-primary"><strong>{{business.business_name}}</strong></p>
                    <p>Owner: <strong>{{business.business_owner_name}}</strong> </p>
                    <p v-if="business.barangay">Barangay: <strong>{{business.barangay.barangay_name}}</strong></p>
                    <p v-if="business.category">Category: <strong>{{business.category}}</strong></p>
                    <p v-if="business.business_status">Status: <strong>{{business.business_status}}</strong></p>
                    <p v-if="business.capitalization_amount">Capitalization: <strong>{{business.capitalization_amount}}</strong></p>
                    <p v-if="business.gross_sale_amount">Gross sales: <strong>{{business.gross_sale_amount}}</strong></p>
                </div>   

                <div class="column is-4">
                        <div class="field">
                            <label for="">Payment mode</label>
                            <div class="select is-small">
                                <select name="payment_mode" id="" v-model="payment.payment_mode">
                                    <option value="" selected>-- Select paymant mode --</option>
                                    <option value="annual">Annual</option>
                                    <option value="semi">Semi-annual</option>
                                    <option value="quarter">Quarterly</option>
                                </select>
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Date</label>
                            <div class="control">
                                <input type="date" class="input is-small" v-model="payment.payment_date">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Paid to</label>
                            <div class="control">
                                <input type="text" class="input is-small" v-model="payment.paid_to" required>
                            </div>
                        </div>
                        <div class="field">
                            <label for="">O.R. Number</label>
                            <div class="control">
                                <input type="text" class="input is-small" v-model="payment.or_no">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Paid amount</label>
                            <div class="control">
                                <input type="number" class="input is-small has-text-right" v-model="payment.amount_paid">
                            </div>
                        </div>
                    </div>
                    <div class="column is-12">
                        <button class="button is-success" @click="submitForm">Save changes</button>
                    </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'EditPayment',
    props: ['businessId'],
    data() {
        return{
            business: {},
            payment: {}
        }
    },
    async mounted() {
        await this.getPayment()
        await this.getBusiness()
    },
    methods: {
        getPayment() {
            const paymentId = this.$route.params.id
            axios.get(`/api/v1/payments/${paymentId}/`)
                 .then(response => {
                     this.payment = response.data
                     console.log(response.data["payment_date"])
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusiness(){
            axios.get(`/api/v1/businesses/${this.businessId}/`)
                 .then(response => {
                     this.business=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm(){

            const paymentId=this.$route.params.id
            const payment_date = this.payment.payment_date //+ ' 00:00'
            console.log(payment_date)
            this.payment.business=this.businessId
            this.payment.payment_date = payment_date
            axios.patch(`/api/v1/payments/${paymentId}/`, this.payment)
                 .then(response => {
                     toast({
                         message: 'The changes were saved',
                         type: 'is-success',
                         dismissible: true,
                         pauseOnHover: true,
                         duration: 2000,
                         position: 'bottom-center',
                     })
                    this.$router.push(`/dashboard/payments/${this.businessId}`)
                 })
        }
    }
}
</script>