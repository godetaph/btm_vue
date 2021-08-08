<template>
    <div class="page add-period">
        <div class="columns is-multiline">
            <div class="title is-5">Add period</div>
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
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'AddPeriod',
    data() {
        return {
            period:{
                period_year:''
            }
        }
    },
    methods:{
        submitForm(){
            axios.post('/api/v1/periods/', this.period)
                 .then(response => {
                     toast ({
                        message: 'New period was added successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-left',
                     })
                     this.$router.push("/dashboard/periods")
                 })
        }
    }

}
</script>

<style>

</style>