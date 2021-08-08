<template>
    <div class="page-dashboard">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong>Dashboard</div>
                <hr>
            </div>
            <div class="column is-12"><strong>Grand total</strong></div>
            <div class="column is-3">
                <div class="box">
                    <div><strong class="is-size-7 has-text-grey-light">Total businesses</strong></div>
                    <hr>
                    <div class="has-text-primary has-text-centered title is-5">{{business_count}}</div>
                </div>
            </div>
            <div class="column is-3">
                <div class="box">
                    <div><strong class="is-size-7 has-text-grey-light">Total collection</strong></div>
                    <hr>
                    <div class="has-text-primary has-text-centered title is-5">1,000,000.00</div>
                </div>
            </div>
            <div class="column is-3">
                <div class="box">
                    <div><strong class="is-size-7 has-text-grey-light">Business permits (Y | N)</strong></div>
                    <hr>
                    <div class="has-text-centered"><span class="has-text-primary title is-5">{{this.business_permit_yes}}</span> <span class="has-text-dark title is-5">|</span> <span class="has-text-danger title is-5">{{this.business_count-this.business_permit_yes}}</span> </div>
                </div>
            </div>
            <div class="column is-3">
                <div class="box">
                    <div><strong class="is-size-7 has-text-grey-light">Notifications (Read | Unread)</strong></div>
                    <hr>
                    <div class="has-text-centered"><span class="has-text-primary title is-5">{{this.notification_count-this.notification_unread}}</span> <span class="has-text-dark title is-5">|</span> <span class="has-text-danger title is-5">{{notification_unread}}</span> </div>
                </div>
            </div>

            <div class="column is-12"><strong>Others</strong></div>
            <div class="column is-3">
                <div class="box">
                    <div class="title is-6">Delinquent</div>
                    <hr>
                    <div class="has-text-primary has-text-centered title is-5">10</div>
                </div>
            </div>
            <div class="column is-3">
                <div class="box">
                    <div class="title is-6">Closed business</div>
                    <hr>
                    <div class="has-text-primary has-text-centered title is-5">5</div>
                </div>
            </div>
            <div class="column is-3">
                <div class="box">
                    <div class="title is-6">Annual collection</div>
                    <hr>
                    <div class="has-text-primary has-text-centered title is-5">250,000.00</div>
                </div>
            </div>
            <div class="column is-3">
                <div class="box">
                    <div class="title is-6">Total notifications</div>
                    <hr>
                    <div class="has-text-primary has-text-centered title is-5">{{this.notification_count}}</div>
                </div>
            </div>

            <div class="column is-12"><strong>Graph</strong></div>
            <div class="column is-6">
                <PlanetChart />
            </div>
            <div class="column is-3">
                <PieChart />
            </div>
            <div class="column is-3">
                <PieChart1 />
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import PlanetChart from '../../components/PlanetChart.vue'
import PieChart from '../../components/PieChart.vue'
import PieChart1 from '../../components/PieChart1.vue'
import BtmMap from '../../components/BtmMap.vue'

export default {
    name: 'Dashboard',
    components: {
        PlanetChart, PieChart, PieChart1, BtmMap
    },
    data() {
        return {
            business: [],
            business_count: 0,
            business_permit_yes:0,
            business_permit_no:0,
            notification: [],
            notification_count:0,
            notification_read:0,
            notification_unread:0,
            gross_amount:0
        }
    },
    async mounted() {
        await this.getBusiness()
        await this.getBusinessPermit()
        await this.getNotification()
        await this.getNotifications()
        // await this.getPayments()
    },
    computed() {
        
    },
    methods: {
        getBusiness(){
            axios.get('/api/v1/businesses/?size=100000')
                 .then(response => {
                     console.log(response)
                     this.business=response.data.results
                     this.business_count=response.data.count
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getNotification(){
            axios.get('/api/v1/notifications/')
                 .then(response => {
                     this.notification=response.data.results
                     this.notification_count=response.data.count
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getNotifications(){
            axios.get('/api/v1/notifications/?is_read=False')
                 .then(response => {
                     this.notification_unread=response.data.count
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        getBusinessPermit(){
            axios.get('/api/v1/businesses/?permit=yes&size=100000')
                 .then(response => {
                     console.log(response)
                     this.business_permit_yes=response.data.count
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        // getPayments(){
        //     axios.get('/api/v1/payments/?business=21')
        //          .then(response => {
        //              console.log(response)
        //              //this.gross_amount=response.data[0]
        //          })
        //          .catch(error => {
        //              console.log(JSON.stringify(error))
        //          })
        // }
    }
}
</script>