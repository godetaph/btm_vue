<template>
    <div class="page-business-categories">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">
                    Line of business | Categories
                </div>
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

                <div class="title is-5">List of line of business</div>
                <router-link class="button is-dark  mb-4" :to="{name: 'AddBusinessCategory', params: {id:business.id}}">Add business category</router-link>
                <table class="table is-fullwidth is-stripped is-narrow is-hoverable">
                    <thead>
                        <tr>
                            <th>Category</th>
                            <th>Comment</th>
                            <th>Notifed</th>
                            <th>...</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="busCategory in busCategories" v-bind:key="busCategory">
                            <td>{{busCategory.cat_name}}</td>
                            <td>{{busCategory.comment}}</td>
                            <td>{{busCategory.is_pushed}}</td>
                            <td>
                                <router-link :to="{name: 'EditBusinessCategory', params: {id:busCategory.id, businessId:business.id}}">Edit</router-link> | 
                                <router-link :to="{name: 'DeleteBusinessCategory', params: {id:busCategory.id, businessId:business.id}}">Delete</router-link>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'BusinessCategories',
    data() {
        return {
            business: {},
            busCategories: []
        }
    },
    mounted() {
        this.getBusiness()
        this.getBusinessCategories()
    },
    methods: {
        getBusiness(){
            const businessId=this.$route.params.id
            axios.get(`/api/v1/businesses/${businessId}/`)
                 .then(res => {
                     this.business=res.data
                 })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        getBusinessCategories(){
            const businessId=this.$route.params.id
            axios.get(`/api/v1/business-categories?business=${businessId}`)
                 .then(response => {
                     for (let i = 0; i < response.data.length; i++) {
                         this.busCategories.push(response.data[i])
                     }
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>