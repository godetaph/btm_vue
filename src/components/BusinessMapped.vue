<template>
    <div class="column is-12">

        <form @submit.prevent="submitForm" class="mb-3">
            <div class="field has-addons">
                <div class="control">
                    <div class="select is-small" style="width:200px;">
                        <select name="" id="" class="select is-small">
                            <option value="">--Year period--</option>
                            <option value="2021">2021</option>
                        </select>
                    </div>
                </div>

                <div class="control">
                    <input type="text" class="input ml-4 is-small" style="width:300px;" placeholder="Search" v-model="query">
                </div>
                <div class="control">
                    <button class="button is-success ml-2 is-small">Search</button>
                </div>
            </div>
            
        </form>

        <table class="table is-fullwidth is-stripped is-narrow is-hoverable is-bordered is-size-7">
            <thead>
                <tr>
                    <th>Business name</th>
                    <th>Owner name</th>
                    <th>Barangay</th>
                    <th>Purok</th>
                    <th>Bus. Permit</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="period in business_periods" v-bind:key="period.id">
                    <td>{{period.business_name}}</td>
                    <td>{{period.business_owner}}</td>
                    <td v-if="period.barangay">{{period.barangay}}</td>
                    <td v-else>-</td>
                    <td>{{period.purok}}</td>
                    <td>{{period.permit}}</td>
                    <td>
                        <router-link :to="{name: 'Business', params: {id:period.business}}" class="has-text-info"><i class="fa fa-info"></i>Info</router-link> | 
                        <!-- <router-link :to="{name: 'EditBusiness', params: {id:business.id}}" class="has-text-info"><i class="fa fa-pencil-square-o"></i></router-link> |  -->
                        <router-link :to="{name: 'Payments', params: {id:period.business}}" class="has-text-info"><i class="fa fa-money"></i></router-link> |
                        <router-link :to="{name: 'BusinessCategories', params: {id:period.business}}" class="has-text-info"><i class="fa fa-briefcase"></i></router-link> |
                        <!-- <router-link :to="{name: 'AddBusinessPeriod', params: {id:business.id}}" class="has-text-info"><i class="fa fa-plus"></i></router-link> -->
                        <!-- <router-link to="#" class="has-text-info" @click="$refs.modalName.openModal()"><i class="fa fa-plus"></i></router-link> -->
                        <!-- <button @click="$refs.modalName.openModal()">Open modal</button> -->
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="buttons">
            <button class="button is-outlined is-dark" @click="loadNext()" v-if="showNext">Next</button>
            <button class="button is-outlined is-dark" @click="loadPrev()" v-if="showPrev">Previous</button>
        </div>
        <!-- <button @click="$refs.modalName.openModal()">Open modal</button> -->

        <!-- <modal ref="modalName">
            <template v-slot:header>
                <h1>Modal title</h1>
            </template>

            <template v-slot:body>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc sed velit dignissim sodales ut eu sem integer vitae. Id aliquet lectus proin nibh nisl condimentum. Fringilla urna porttitor rhoncus dolor purus. Nam aliquam sem et tortor. Nisl vel pretium lectus quam id. Cras pulvinar mattis nunc sed. Quis ipsum suspendisse ultrices gravida dictum fusce ut placerat orci. Tristique magna sit amet purus. Fermentum et sollicitudin ac orci phasellus egestas tellus. Erat pellentesque adipiscing commodo elit at imperdiet dui accumsan. Felis eget nunc lobortis mattis aliquam faucibus. Tincidunt eget nullam non nisi est sit amet facilisis. Mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Vitae proin sagittis nisl rhoncus mattis rhoncus urna neque. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. Nec nam aliquam sem et tortor consequat id. Commodo nulla facilisi nullam vehicula ipsum a. Elementum tempus egestas sed sed. Faucibus purus in massa tempor nec feugiat nisl pretium fusce.</p>
                <p>Arcu cursus vitae congue mauris rhoncus aenean. Tempor id eu nisl nunc mi. Pharetra diam sit amet nisl suscipit adipiscing bibendum. Ut faucibus pulvinar elementum integer enim. Odio facilisis mauris sit amet massa vitae tortor condimentum lacinia. Eu non diam phasellus vestibulum lorem sed risus. Porttitor rhoncus dolor purus non enim praesent. Sit amet mauris commodo quis imperdiet. Lobortis feugiat vivamus at augue eget. Nibh tellus molestie nunc non blandit. Tellus mauris a diam maecenas sed enim ut. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Mattis aliquam faucibus purus in massa.</p>
            </template>

            <template v-slot:footer>
                <div class="d-flex align-items-center justify-content-between">
                <button class="btn btn--secondary" @click="$refs.modalName.closeModal()">Cancel</button>
                <button class="btn btn--primary" @click="$refs.modalName.closeModal()">Save</button>
                </div>
            </template>
        </modal> -->
    </div>

</template>

<script>
import axios from 'axios'
import Modal from './Modal.vue'
export default {
    name: 'BusinessMapped',
    components: {
        Modal
    },
    data() {
        return {
            business_periods: [],
            currentPage: 1,
            showNext: false,
            showPrev: false,
            query: ''
        }
    },
    mounted() {
        this.getBusinessPeriods()
    },
    methods: {
        loadNext() {
            this.currentPage += 1
            this.getBusinesses()
        },
        loadPrev() {
            this.currentPage -= 1
            this.getBusinesses()
        },
        getBusinessPeriods() {
            this.business_periods.length=0
            axios.get(`/api/v1/business-periods/?search=${this.query}`) 
                 .then(response => {
                    //  this.business_periods=[]
                    //  this.showNext=false
                    //  this.showPrev=false
                    //  this.business_periods=response.data.results
                     for(let i=0; i < response.data.length; i++){
                         this.business_periods.push(response.data[i])
                     }
                    //  if (response.data.next){
                    //      this.showNext=true
                    //  }
                    //  if (response.data.previous){
                    //      this.showPrev=true
                    //  }
                     //this.businesses = response.data
                 })
                 .catch(error => {
                     console.log(error)
                 })
        },
        submitForm() {
            this.getBusinessPeriods()
        }
    }
}
</script>

<style lang="scss">
    
</style>