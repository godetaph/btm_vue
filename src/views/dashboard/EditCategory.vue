<template>
    <div class="page-edit-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong>EditCategory</div>

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
import { toast } from 'bulma-toast'
export default {
    name: 'EditCategory',
    data() {
        return {
            category: {}
        }
    },
    mounted(){
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
            axios.patch(`/api/v1/categories/${categoryId}/`, this.category)
                 .then(response => {
                     toast({
                         message: 'The changes were successfully saved',
                         type: 'is-success',
                         dismissible: true,
                         pauseOnHover: true,
                         duration: 2000,
                         position: 'bottom-center',
                     })
                     this.$router.push('/dashboard/categories')
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>