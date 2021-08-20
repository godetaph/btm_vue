<template>
  <div class="page-settings">
      <div class="columns is-multiline">
          <div class="column is-12">
            <div class="is-size-5">
                <strong>BTM</strong> | Settings
            </div>
            <hr>
            <div class="column is-6">
                <!-- <div class="box"> -->
                    <div class="is-size-6"><strong>Date setting</strong></div>
                    <div class="column is-6">
                        <div class="field">
                            <div class="is-size-7">Annual</div>
                            <div class="control">
                                <input type="date" class="input is-small" v-model="settingz.annual_date">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <div class="is-size-7">Semi-annual</div>
                            <div class="control">
                                <input type="date" class="input is-small" v-model="settingz.semi_annual_date1">
                            </div>
                            <div class="control mt-2">
                                <input type="date" class="input is-small" v-model="settingz.semi_annual_date2">
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <div class="is-size-7">Quarterly</div>
                            <div class="control">
                                <input type="date" class="input is-small" v-model="settingz.quarter_date1">
                            </div>
                            <div class="control mt-2">
                                <input type="date" class="input is-small" v-model="settingz.quarter_date2">
                            </div>
                            <div class="control mt-2">
                                <input type="date" class="input is-small" v-model="settingz.quarter_date3">
                            </div>
                            <div class="control mt-2">
                                <input type="date" class="input is-small" v-model="settingz.quarter_date4">
                            </div>
                        </div>
                    </div>
                <!-- </div> -->
                <div class="control mt-4">
                    <button class="button is-success ml-3 is-small" @click="submitForm">Submit data</button>
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
    name: 'Setting',
    data() {
        return {
            settingz: {}
        }
    },
    mounted(){
        this.getSetting()
    },
    methods: {
        getSetting(){
            this.settingz = {}
            axios.get('/api/v1/settings/')
                 .then(response => {
                     this.settingz=response.data[0]
                     console.log(this.settingz)
                 })
                 .catch(error => console.log(JSON.stringify(error)))
        },
        submitForm(){
            axios.patch(`/api/v1/settings/${this.settingz.id}/`, this.settingz)
                 .then(response => {
                     toast({
                         message: 'The changes were saved',
                         type: 'is-success',
                         dismissible: true,
                         pauseOnHover: true,
                         duration: 2000,
                         position: 'bottom-center',
                     })
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