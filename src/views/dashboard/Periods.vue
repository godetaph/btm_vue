<template>
    <div class="page-periods">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title is-5">Periods</div>
                <hr>
            <div class="column is-12">
                <router-link class="button is-dark mb-4" to="/dashboard/periods/add">Add period</router-link>
                <table class="table is-fullwidth is-stripped">
                    <thead>
                        <tr>
                            <th>Year</th>
                            <th>Note</th>
                            <th>Active</th>
                            <th>...</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="period in periods" v-bind:key="period.id">
                            <td>{{period.period_year}}</td>
                            <td>{{period.note}}</td>
                            <td>{{period.is_active}}</td>
                            <td>
                                <router-link :to="{ name: 'EditPeriod', params: {id: period.id} }" class="">Edit</router-link> | 
                                <router-link :to="{ name: 'DeletePeriod', params: {id: period.id} }" class="" v-if="this.$store.state.user.level=='admin'">Delete</router-link>
                            </td>                            
                        </tr>
                    </tbody>
                </table>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Periods',
    data() {
        return {
            periods:[]
        }
    },
    mounted() {
        this.getPeriods()
    },
    methods: {
        getPeriods() {
            axios.get('/api/v1/periods/')
                 .then(response => {
                     this.periods=response.data
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>