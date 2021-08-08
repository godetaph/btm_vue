<template>
    <div class="page-categories">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong>Categories</div>
                <hr>
                <router-link to="/dashboard/categories/add" class="button is-dark mt-4 is-small">Add category</router-link>


                <div class="column is-6 is-size-7">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>Category</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="category in categories" v-bind:key="category.id">
                                <td>{{category.category_name}}</td>
                                <td> 
                                    <router-link :to="{ name: 'EditCategory', params: {id: category.id} }" class="">Edit</router-link> | 
                                    <router-link :to="{ name: 'DeleteCategory', params: {id: category.id} }" class="">Delete</router-link>
                                </td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <tr>
                                <td><strong>Total count:</strong></td>
                                <td><strong>{{categories.length}} of {{total_count}}</strong></td>
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
    name: 'Categories',
    data() {
        return{
            categories: [],
            total_count:0,
            currentPage:1,
            showNext:false,
            showPrev:false
        }
    },
    mounted() {
        this.getCategories()
    },
    methods: {
        loadNext(){
            this.currentPage += 1
            this.getCategories()
            
        },
        loadPrev(){
            this.currentPage -= 1
            this.getCategories()
        },
        getCategories() {
            axios.get(`api/v1/categories/?page=${this.currentPage}&size=20`)
                 .then(response => {
                     this.showNext=false
                     this.showPrev=false
                    //  for (let i = 0; i < response.data.length; i++) {
                    //      this.categories.push(response.data[i])
                    //  }
                    this.categories=response.data.results
                    this.total_count=response.data.count

                    if (response.data.next){
                        this.showNext=true
                    }
                    if (response.data.previous){
                        this.showPrev=true
                    }
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
    }
}
</script>