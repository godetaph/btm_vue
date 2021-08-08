<template>
    <div class="page-delete-barangay">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Delete business category</div>

                <div class="box mt-4">
                    <p class="title is-5 has-text-primary"><strong>{{business.business_name}}</strong></p>
                    <p>Owner: <strong>{{business.business_owner_name}}</strong> </p>
                    <p v-if="business.barangay">Barangay: <strong>{{business.bar_name}}</strong></p>
                    <p v-if="business.purok">Purok: <strong>{{business.purok}}</strong></p>
                    <p v-if="business.stall_no">Stall: <strong>{{business.stall_no}}</strong></p>
                </div> 

                <div class="title-5 mb-4">Are you sure to delete the business catetory?</div>
                <div class="field mb-6">
                    <div class="control">
                        <p>Category: <strong>{{business_category.cat_name}}</strong></p>
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <button class="button is-danger" @click="submitForm">Delete</button>
                        <button class="button is-light ml-2" @click="cancelDelete">Cancel</button>
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
    name: 'DeleteBusinessCategory',
    props: ['businessId'],
    data() {
        return {
            business: {},
            business_category: {}
        }
    },
    mounted() {
        this.getBusiness()
        this.getBusinessCategory()
    },
    methods: {
        getBusiness(){
            axios.get(`/api/v1/businesses/${this.businessId}`)
                 .then(response => {
                     this.business=response.data
                     console.log(this.business)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusinessCategory() {
            const id = this.$route.params.id

            axios.get(`/api/v1/business-categories/${id}/`)
                 .then(response => {
                     this.business_category = response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm() {
            const Id = this.$route.params.id
            axios.delete(`/api/v1/business-categories/${Id}/`, this.business_category)
                 .then(response => {
                     console.log(response.statusText)
                     toast({
                         message: 'The barangay was deleted successfully.',
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
        cancelDelete() {
            this.$router.push(`/dashboard/business-categories/${this.business.id}`)
        },
        countNotification(){
            axios.get(`/api/v1/notifications?is_read=False`)
                .then(response => {
                    this.$store.commit('countNotification', response.data.count)
                    //console.log(response.data.length + " - ok - notification")
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