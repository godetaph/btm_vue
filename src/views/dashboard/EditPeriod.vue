<template>
    <div class="page edit-period">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Edit period</div>
            </div>
            <hr>
            <div class="column is-6">
                <div class="field">
                    <label for="">Year</label>
                    <div class="select">
                        <select name="" id="" class="select" v-model="period.period_year">
                            <option value="" selected>--Select year--</option>
                            <option value="2020">2020</option>
                            <option value="2021">2021</option>
                            <option value="2022">2022</option>
                            <option value="2023">2023</option>
                            <option value="2024">2024</option>
                            <option value="2025">2025</option>
                            <option value="2026">2026</option>
                            <option value="2027">2027</option>
                            <option value="2028">2028</option>
                            <option value="2029">2029</option>
                            <option value="2030">2030</option>
                        </select>
                    </div>
                </div>
                <div class="field">
                    <label for="">Note</label>
                    <div class="control">
                        <textarea class="textarea" name="" id="" rows="10" v-model="period.note"></textarea>
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <input type="checkbox" class="checkbox" v-model="period.is_active"> Active
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Submit data</button>
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
    name: 'EditPeriod',
    data() {
        return {
            period: {}
        }
    },
    mounted(){
        this.getPeriod()
    },
    methods: {
        getPeriod(){
            const periodId=this.$route.params.id
            axios.get(`/api/v1/periods/${periodId}/`)
                 .then(response => {
                     this.period=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm() {
            const periodId=this.$route.params.id
            axios.patch(`/api/v1/periods/${periodId}/`, this.period)
                 .then(response => {
                     toast ({
                        message: 'Updated period successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     this.$router.push("/dashboard/periods")
                 })
        }
    }

}
</script>

<style>

</style>