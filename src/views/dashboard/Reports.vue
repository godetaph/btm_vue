<template>
    <div class="page-reports">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong><span class="has-text-info"></span>Reports</div>
                <hr>
                <div class="column is-6">
                    <ul><a href="#"> List of business</a></ul>
                    <ul><a href="#"> List of no permit</a></ul>
                </div>

            </div>        
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name: 'Reports',
    // data() {
    //     return {
    //         barangay: {}
    //     }
    // },
    // methods: {
    //     submitForm() {
    //         axios.post("/api/v1/barangays/", this.barangay)
    //              .then(response => {
    //                  toast ({
    //                     message: 'New barangay successfully added.',
    //                     type: 'is-success',
    //                     dismissible: true,
    //                     pauseOnHover: true,
    //                     duration: 2000,
    //                     position: 'bottom-center',
    //                  })
    //                  this.$router.push("/dashboard/barangays")
    //              })
    //              .catch(error => {
    //                  console.log = JSON.stringify(error)
    //              })
    //     }
    // }
}
</script>