<template>
    <div class="page-add-barangay">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong><span class="has-text-info">Add</span>Barangay</div>
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
import {toast} from 'bulma-toast'
export default {
    name: 'AddBarangay',
    data() {
        return {
            barangay: {}
        }
    },
    methods: {
        submitForm() {
            axios.post("/api/v1/barangays/", this.barangay)
                 .then(response => {
                     toast ({
                        message: 'New barangay successfully added.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     this.$router.push("/dashboard/barangays")
                 })
                 .catch(error => {
                     console.log = JSON.stringify(error)
                 })
        }
    }
}
</script>