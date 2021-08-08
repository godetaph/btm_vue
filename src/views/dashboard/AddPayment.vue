<template>
    <div class="page add-payment">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Add payment for - {{business.business_name}}</div>
                <hr>

                <div class="box mt-4" v-if="business.business_name">
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
                            <div class="select">
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
                                <input type="date" class="input"  v-model="payment.payment_date">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Paid to</label>
                            <div class="control">
                                <input type="text" class="input" v-model="payment.paid_to">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">O.R. Number</label>
                            <div class="control">
                                <input type="text" class="input" v-model="payment.or_no">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Paid amount</label>
                            <div class="control">
                                <input type="number" class="input has-text-right" v-model="payment.amount_paid">
                            </div>
                        </div>
                    </div>
                    <div class="column is-12">
                        <button class="button is-success" @click="submitForm">Submit payment</button>
                    </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'AddPayment',
    data() {
        return {
            business: {
                payment: ''
            },
            payment: {}
        }
    },
    mounted() {
        this.getBusiness()
    },
    methods: {
        getBusiness() {
            const businessId = this.$route.params.id

            axios.get(`/api/v1/businesses/${businessId}/`)
                 .then(response => {
                     this.business = response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm() {
            const businessId = this.$route.params.id
            const payment_date = this.payment.payment_date //+ ' 00:00'
            console.log(payment_date + " " + businessId)
            this.payment.business=businessId
            this.payment.payment_date = payment_date
            axios.post("/api/v1/payments/", this.payment)
                 .then(response => {
                     toast ({
                        message: 'New payment was added successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     this.$router.push(`/dashboard/payments/${businessId}`)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>