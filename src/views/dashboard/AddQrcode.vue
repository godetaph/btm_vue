<template>
    <div class="page-add-qrcode">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title">Add Qrcode</div>
                <hr>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AddQrcode',
    data() { 
        return {
            qrcode:{}
        }
    },
    methods: {
        submitForm() {
            axios.post("/api/v1/qrcodes", this.qrcode)
                 .then(response => {
                     console.log(response.statusText)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }

}
</script>

<style>

</style>