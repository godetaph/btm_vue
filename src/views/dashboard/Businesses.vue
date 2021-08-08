<template>
    <div class="page-businesses">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong>BusinessList</div>
                <hr>

                <business-list />
                <!-- <div class="column is-12">
                    <router-link to="/dashboard/businesses/add" class="button is-dark mb-4">Add business</router-link>

                    <form @submit.prevent="submitForm" class="mb-3">
                        <div class="field has-addons">
                            <div class="control">
                                <input type="text" class="input" style="width:300px;" v-model="query">
                            </div>
                            <div class="control">
                                <button class="button is-info ml-2">Search</button>
                            </div>
                        </div>
                    </form>
                    
                    <table class="table is-fullwidth is-stripped is-narrow is-hoverable">
                        <thead>
                            <tr>
                                <th>Business name</th>
                                <th>Owner name</th>
                                <th>Barangay</th>
                                <th>Category</th>
                                <th>Purok</th>
                                <th>Stall no</th>
                                <th>Bus. Permit</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="business in businesess" v-bind:key="business.id">
                                <td>{{business.business_name}}</td>
                                <td>{{business.business_owner_name}}</td>
                                <td v-if="business.barangay">{{business.barangay.barangay_name}}</td>
                                <td v-else>-</td>
                                <td>{{business.category}}</td>
                                <td>{{business.purok}}</td>
                                <td>{{business.stall_no}}</td>
                                <td>{{business.is_business_permit}}</td>
                                <td>
                                    <router-link :to="{name: 'Business', params: {id:business.id}}" class="has-text-info"><i class="fa fa-info"></i>Info</router-link> | 
                                    <router-link :to="{name: 'EditBusiness', params: {id:business.id}}" class="has-text-info"><i class="fa fa-pencil-square-o"></i></router-link> | 
                                    <router-link :to="{name: 'Payments', params: {id:business.id}}" class="has-text-info"><i class="fa fa-money"></i></router-link> |
                                    <router-link :to="{name: 'BusinessCategories', params: {id:business.id}}" class="has-text-info"><i class="fa fa-briefcase"></i></router-link> |
                                    <router-link to="#" class="has-text-info"><i class="fa fa-map" aria-hidden="true"></i></router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="buttons">
                        <button class="button is-outlined is-dark" @click="loadNext()" v-if="showNext">Next</button>
                        <button class="button is-outlined is-dark" @click="loadPrev()" v-if="showPrev">Previous</button>
                    </div>
                </div> -->
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import BusinessList from '../../components/BusinessList.vue'
// import BusinessList from './BusinessList.vue'
export default {
  components: { BusinessList },
    name: 'Businesses',
    // data() {
    //     return {
    //         businesess: [],
    //         currentPage: 1,
    //         showNext: false,
    //         showPrev: false,
    //         query: ''
    //     }
    // },
    // mounted() {
    //     this.getBusinesses()
    // },
    // methods: {
    //     loadNext() {
    //         this.currentPage += 1
    //         this.getBusinesses()
    //     },
    //     loadPrev() {
    //         this.currentPage -= 1
    //         this.getBusinesses()
    //     },
    //     getBusinesses() {
    //         axios.get(`/api/v1/businesses/?page=${this.currentPage}&search=${this.query}`) 
    //              .then(response => {
    //                  this.showNext=false
    //                  this.showPrev=false
    //                  this.businesess=response.data.results
    //                 //  for(let i=0; i < response.data.length; i++){
    //                 //      this.businesess.push(response.data[i])
    //                 //  }
    //                  if (response.data.next){
    //                      this.showNext=true
    //                  }
    //                  if (response.data.previous){
    //                      this.showPrev=true
    //                  }
    //                  //this.businesses = response.data
    //              })
    //              .catch(error => {
    //                  console.log(error)
    //              })
    //     },
    //     submitForm() {
    //         this.getBusinesses()
    //     }
    //}

}
</script>