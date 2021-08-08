<template>
    <div class="page-delete-barangay">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Delete barangay</div>

                <div class="title-5 mb-4">Are you sure to delete the barangay?</div>
                <div class="field mb-6">
                    <div class="control">
                        <p>Barangay name: <strong>{{barangay.barangay_name}}</strong></p>
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <button class="button is-danger" @click="submitForm">Delete</button>
                        <router-link to="/dashboard/barangays" class="button is-light">Cancel</router-link>
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
    name: 'DeleteBarangay',
    data() {
        return {
            barangay: {}
        }
    },
    mounted() {
        this.getBarangay()
    },
    methods: {
        getBarangay() {
            const barangayId = this.$route.params.id

            axios.get(`/api/v1/barangays/${barangayId}/`)
                 .then(response => {
                     this.barangay = response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm() {
            const barangayId = this.$route.params.id
            this.barangay.is_deleted = true
            axios.patch(`/api/v1/barangays/${barangayId}/`, this.barangay)
                 .then(response => {
                     toast({
                         message: 'The barangay was deleted successfully.',
                         type: 'is-success',
                         dismissible: true,
                         pauseOnHover: true,
                         duration: 2000,
                         position: 'bottom-center',
                     })
                     this.$router.push("/dashboard/barangays")
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>