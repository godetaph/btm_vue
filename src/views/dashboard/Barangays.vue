<template>
    <div class="page-barangays">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong>Barangays</div>
                <hr>
                <router-link to="/dashboard/barangays/add" class="button is-dark is-small ml-4">Add barangay</router-link>
                <div class="column is-6 is-size-7">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>Barangay</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="barangay in barangays" v-bind:key="barangay.id">
                                <td>{{barangay.barangay_name}}</td>
                                <td>
                                    <router-link :to="{ name: 'EditBarangay', params: {id:barangay.id}}">Edit</router-link> | 
                                    <router-link :to="{ name: 'DeleteBarangay', params: {id:barangay.id}}">Delete</router-link>
                                </td>
                            </tr>
                        </tbody>
                        <tfoot>
                        <tr>
                            <td><strong>Total count:</strong></td>
                            <td><strong>{{barangays.length}} of {{total_count}}</strong></td>
                        </tr>
                    </tfoot>
                    </table>
                    <div class="buttons">
                        <button class="button is-outlined is-dark is-small" @click="loadNext()" v-if="showNext">Next page</button>
                        <button class="button is-outlined is-dark is-small" @click="loadPrev()" v-if="showPrev">Previous page</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'Barangays',
    data() {
        return {
            barangays:[],
            total_count: 0,
            currentPage:1,
            showNext:false,
            showPrev:false
        }
    },
    mounted() {
        this.getBarangay()
    },
    methods: {
        loadNext(){
            this.currentPage+=1
            this.getBarangay()
        },
        loadPrev(){
            this.currentPage-=1
            this.getBarangay()
        },
        getBarangay() {
            axios.get(`/api/v1/barangays/?page=${this.currentPage}&size=20`)
                 .then(response => {
                     this.showNext=false
                     this.showPrev=false
                     this.barangays=response.data.results
                     this.total_count=response.data.count
                     if (response.data.next){
                         this.showNext=true
                     }
                     if (response.data.previous){
                         this.showPrev=true
                     }
                    //  for (let i = 0; i < response.data.length; i++) {
                    //      this.barangays.push(response.data[i])
                    //  }
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>