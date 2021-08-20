<template>
  <div class="page scan-qr-code">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="is-size-5">Scan QR Code</div>

            <div class="column is-12">
                <div class="control">
                    <input type="text" class="input" v-model="qrcode">
                </div>
                <button class="button is-success is-small" @click="getBusinessQrCode">
                    Scan Code
                </button>
            </div>

              <p>QR Code: {{business.qr_code}}</p>
              <p>Buiness: {{business.business_name}}</p>

              
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ScanQrCode',
    data() {
        return {
            business: {},
            qrcode:''
        }
    },
    methods: {
        getBusinessQrCode(){
            axios.get(`/api/v1/businesses/?scan=${this.qrcode}`)
                 .then(response => {
                     this.business=response.data[0]
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