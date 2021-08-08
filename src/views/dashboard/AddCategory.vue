<template>
    <div class="page-add-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title is-5">Add category</h1>

                <div class="column is-6">
                    <div class="field">
                        <label for="">Category name</label>
                        <div class="control">
                            <input type="text" class="input" name="category_name" v-model="category.category_name">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success" @click="submitForm">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name: 'AddCategory',
    data() {
        return {
            category: {}
        }        
    },
    methods: {
        submitForm() {
            axios.post("/api/v1/categories/", this.category)
                 .then(response => {
                     toast ({
                        message: 'New category added.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                     })
                     this.$router.push('/dashboard/categories')
                 })
                 .catch(error => {
                     console.log = JSON.stringify(error)
                 })
        }
    }
}
</script>