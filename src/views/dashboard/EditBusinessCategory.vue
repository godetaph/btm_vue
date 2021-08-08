<template>
  <div class="page-add-business-category">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="title is-5">Edit Line of Buiness | Categories</div>
          

            <div class="box mt-4">
                <p class="title is-5 has-text-primary"><strong>{{business.business_name}}</strong></p>
                <p>Owner: <strong>{{business.business_owner_name}}</strong> </p>
                <p v-if="business.barangay">Barangay: <strong>{{business.bar_name}}</strong></p>
                <p v-if="business.purok">Purok: <strong>{{business.purok}}</strong></p>
                <p v-if="business.stall_no">Stall: <strong>{{business.stall_no}}</strong></p>
            </div> 

            <div class="column is-6">
                <div class="field">
                    <label for="">Business category</label>
                        <div class="select">
                            <select name="category" id="" v-model="businessCategory.category">
                                <option value="" selected>-- Select category --</option>
                                <option v-for="category in categories" v-bind:key="category.id" v-bind:value="category.id">{{category.category_name}}</option>
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
    props: ['businessId'],
    data() {
        return {
            businessCategory: {},
            business:{},
            categories:[]
        }
    },
    mounted() {
        this.getCategories()
        this.getBusiness()
        this.getBusinessCategory()
    },
    methods: {
        getCategories(){
            axios.get(`/api/v1/categories/?size=200`)
                 .then(response => {
                    //  for (let i = 0; i < response.data.length; i++) {
                    //      this.categories.push(response.data.results[i])
                    //  }
                    this.categories=response.data.results
                 })
                 .catch(error=> {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusiness(){
            axios.get(`/api/v1/businesses/${this.businessId}`)
                 .then(response => {
                     this.business=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusinessCategory(){
            const busCategoryId=this.$route.params.id
            axios.get(`/api/v1/business-categories/${busCategoryId}`)
                 .then(response => {
                     this.businessCategory=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm(){
            this.businessCategory.business=this.business.id
            this.businessCategory.category=this.businessCategory.category
            axios.patch(`/api/v1/business-categories/${this.businessCategory.id}/`, this.businessCategory)
                 .then(response => {
                     console.log(response.statusText + " RESULT")
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
                    console.log(response.data.length + " - ok - notification")
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
