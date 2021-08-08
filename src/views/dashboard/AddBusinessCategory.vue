<template>
  <div class="page-add-business-category">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="title is-5">Add Line of Buiness | Categories</div>
          

            <div class="box mt-4">
                <p class="title is-5 has-text-primary"><strong>{{business.business_name}}</strong></p>
                <p>Owner: <strong>{{business.business_owner_name}}</strong> </p>
                <p v-if="business.barangay">Barangay: <strong>{{business.barangay.barangay_name}}</strong></p>
                <p v-if="business.category">Category: <strong>{{business.category}}</strong></p>
                <p v-if="business.business_status">Status: <strong>{{business.business_status}}</strong></p>
                <p v-if="business.capitalization_amount">Capitalization: <strong>{{business.capitalization_amount}}</strong></p>
                <p v-if="business.gross_sale_amount">Gross sales: <strong>{{business.gross_sale_amount}}</strong></p>
            </div> 
            <div class="column is-6">
                <div class="field">
                    <label for="">Business category</label>
                        <div class="select">
                            <select name="category" id="" v-model="businessCategory.category">
                                <option value="" selected>-- Select category --</option>
                                <option v-for="category in categories" v-bind:key="category.id" v-bind:value="category">{{category.category_name}}</option>
                            </select>
                        </div>
                </div>
                <div class="field">
                    <label for="">Comment</label>
                    <div class="control">
                        <textarea class="textarea" rows="10" v-model="businessCategory.comment"></textarea>
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <input type="checkbox" class="checkbox" v-model="businessCategory.is_pushed"> Push to notification
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Submit </button>
                    </div>
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
    name: 'AddBusinessCategory',
    data() {
        return {
            categories:[],
            businessCategory: {
                category:''
            },
            business:{} 
        }
    },
    mounted() {
        this.getCategories()
        this.getBusiness()
    },
    methods: {
        getCategories(){
            axios.get('/api/v1/categories/?size=200')
                 .then(response => {
                    //  for (let i = 0; i < response.data.length; i++) {
                    //      this.categories.push(response.data[i])
                    //  }
                    this.categories=response.data.results
                 })
                 .catch(error=> {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusiness(){
            const businessId=this.$route.params.id
            axios.get(`/api/v1/businesses/${businessId}`)
                 .then(response => {
                     this.business=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm(){
            this.businessCategory.business=this.business.id
            this.businessCategory.category=this.businessCategory.category.id
            axios.post('/api/v1/business-categories/', this.businessCategory)
                 .then(response => {
                     console.log(response.statusText)
                     toast ({
                        message: 'New business category was added successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     this.countNotification()
                     this.$router.push(`/dashboard/business-categories/${this.business.id}`)
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

<style>

</style>