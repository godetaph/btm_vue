<template>
    <div class="page-edit-barangay">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong><span class="has-text-info">Edit</span>Barangay</div>
                <hr>
                <div class="column is-6">
                    <div class="field">
                        <label for="">Barangay name</label>
                        <div class="control">
                            <input type="text" class="input" name="barangay_name" v-model="barangay.barangay_name">
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
    name: 'EditBarangay',
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
                 .then(respose => {
                     this.barangay = respose.data
                 })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        submitForm() {
            const barangayId = this.$route.params.id
            axios.patch(`/api/v1/barangays/${barangayId}/`, this.barangay)
                 .then(response => {
                     toast({
                         message: 'The changes were saved',
                         type: 'is-success',
                         dismissible: true,
                         pauseOnHover: true,
                         duration: 2000,
                         position: 'botton-center'
                     })
                     this.$router.push("/dashboard/barangays")
                 })
        }
    }
    
}
</script>