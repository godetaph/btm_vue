<template>
  <div class="page-delete-payments">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="title is-5">
                  Delete payments
              </div>
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
              <div class="mt-4 box">
                  <div class="title is-5 has-text-danger">You are about to delete this record.</div>
                  <p>Mode: <strong>{{payment.payment_mode}}</strong></p>
                  <p>Date: <strong>{{payment.payment_date}}</strong></p>
                  <p>Paid to: <strong>{{payment.paid_to}}</strong></p>
                  <p>O.R. no: <strong>{{payment.or_no}}</strong></p>
                  <p>Amount: <strong>{{payment.amount_paid}}</strong></p>
              
              <hr>
              <div class="field mt-4">
                  <button class="button is-danger mr-2" @click="deleteForm">Delete payment</button>
                  <button class="button is-light" @click="cancelDelete">Cancel</button>
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
    name: 'DeletePayment',
    props:['businessId'],
    data() {
        return{
            business: {},
            payment: {}
        }
    },
    mounted() {
        this.getBusiness()
        this.getPayment()
    },
    methods: {
        getBusiness(){
            axios.get(`/api/v1/businesses/${this.businessId}/`)
                 .then(response => {
                     this.business=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getPayment(){
            const paymentId=this.$route.params.id
            axios.get(`/api/v1/payments/${paymentId}/`)
                 .then(response => {
                     this.payment=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        deleteForm(){
            const paymentId=this.$route.params.id
            axios.delete(`/api/v1/payments/${paymentId}/`, this.payment)
                 .then(response => {
                     toast({
                         message: 'The payment was deleted successfully.',
                         type: 'is-success',
                         dismissible: true,
                         pauseOnHover: true,
                         duration: 2000,
                         position: 'bottom-center',
                     })
                    this.$router.push(`/dashboard/payments/${this.businessId}`)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        cancelDelete(){
            this.$router.push(`/dashboard/payments/${this.businessId}`)
        }
    }
}
</script>

<style>

</style>