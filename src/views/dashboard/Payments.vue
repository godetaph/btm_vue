<template>
    <div class="page-payments">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Payments</div>
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

                <div class="column is-12">
                    <div class="title is-5">Payment list</div>
                    <router-link class="button is-dark  mb-4" :to="{name: 'AddPayment', params: {id:business.id}}">Add payment</router-link>
                    <table class="table is-fullwidth is-stripped is-narrow is-hoverable">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Mode</th>
                                <th>Paid to</th>
                                <th>O.R. no</th>
                                <th>Amount</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="payment in payments" v-bind:key="payment.id"> 
                                <td>{{payment.payment_date}}</td>
                                <td>{{payment.payment_mode}}</td>
                                <td>{{payment.paid_to}}</td>
                                <td>{{payment.or_no}}</td>
                                <td>{{payment.amount_paid}}</td>
                                <td>
                                    <router-link :to="{name: 'EditPayment', params: {id: payment.id, businessId: business.id}}">Edit</router-link> | 
                                    <router-link :to="{name: 'DeletePayment', params: {id: payment.id, businessId: business.id}}">Delete</router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
            </div>

        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'Payments',
    data() {
        return {
            business: {},
            payments:[]
        }
    },
    mounted(){
        this.getBusiness()
        this.getPayments()
    },
    methods: {
        getBusiness(){
            const businessId = this.$route.params.id
            axios.get(`/api/v1/businesses/${businessId}/`)
                 .then(response => {
                    this.business=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getPayments(){
            const businessId = this.$route.params.id
            axios.get(`/api/v1/payments?business=${businessId}`)
                 .then(response => {
                     for (let i = 0; i < response.data.length; i++) {
                         this.payments.push(response.data[i]);   
                     }
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>