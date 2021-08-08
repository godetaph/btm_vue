<template>
    <div class="page-delete-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Delete category</div>
                <hr>
                
                <div class="title-5 mb-4">Are you sure to delete the category?</div>
                <div class="field mb-6">
                    <div class="control">
                        <p>Category name: <strong>{{category.category_name}}</strong></p>
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <button class="button is-danger" @click="submitForm">Delete</button>
                        <router-link to="/dashboard/categories" class="button is-light">Cancel</router-link>
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
    name: 'EditCategory',
    data() {
        return {
            category: {}
        }
    },
    mounted() {
        this.getCategory()
    },
    methods: {
        getCategory() {
            const categoryId = this.$route.params.id
            axios.get(`/api/v1/categories/${categoryId}/`)
                 .then(response => {
                     this.category = response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm() {
            const categoryId = this.$route.params.id
            this.category.is_deleted = true
            axios.patch(`/api/v1/categories/${categoryId}/`, this.category)
                 .then(response => {
                     toast({
                         message: 'The category was deleted successfully.',
                         type: 'is-success',
                         dismissible: true,
                         pauseOnHover: true,
                         duration: 2000,
                         position: 'top-center',
                     })
                    this.$router.push("/dashboard/categories")
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>