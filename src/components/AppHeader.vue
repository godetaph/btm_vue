<template>
    <nav class="navbar is-dark">
            <div class="navbar-brand">
            <router-link to="/" class="navbar-item"><strong>BTM</strong> | BusinessTaxMapping</router-link>
            </div>

            <div class="navbar-menu">
                <div class="navbar-end">
                    <template v-if="$store.state.isAuthenticated">
                        <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>
                        <router-link to="/dashboard/notifications" class="navbar-item">Notification<span class="tag is-danger is-rounded"> {{countNotif}} </span></router-link>
                        <!-- <router-link to="/dashboard/notifications" class="navbar-item">Notification<span class="tag is-danger is-rounded" v-if="notificationCount == 0"> {{notification.length}} </span></router-link> -->
                        <!-- <router-link to="/dashboard/businesses" class="navbar-item">Business</router-link> -->
                        <div class="navbar-item has-dropdown is-hoverable">
                            <a class="navbar-link">
                            Data
                            </a>

                            <div class="navbar-dropdown">

                                <router-link to="/dashboard/businesses" class="navbar-item">Business</router-link>

                                <router-link to="/dashboard/business-periods" class="navbar-item">Mapping data</router-link>

                                <a class="navbar-item">
                                    Delinquent
                                </a>
                                <hr class="navbar-divider">
                                <router-link to="/dashboard/upload-collection" class="navbar-item">Upload collection</router-link>
                                <hr class="navbar-divider">
                                <router-link to="/dashboard/sms-home" class="navbar-item">SMS</router-link>
                                <!-- <hr class="navbar-divider">
                                <router-link to="/dashboard/reports" class="navbar-item">Report</router-link> -->
                                
                            </div>
                        </div>
                        <router-link to="/dashboard/map" class="navbar-item">Map</router-link>
                        <router-link to="/dashboard/preferences" class="navbar-item">Preferences</router-link>

                        <div class="navbar-item">
                            <div class="buttons">
                            <router-link to="/dashboard/my-account" class="button is-light is-small">{{$store.state.user.username}}</router-link>
                            </div>
                        </div>
                    </template>

                    <template v-else>
                    <router-link to="/" class="navbar-item">Home</router-link>

                    <div class="navbar-item">
                        <div class="buttons">
                        <router-link to="/sign-up" class="button is-success"><strong>Sign up</strong></router-link>
                        <router-link to="/log-in" class="button is-light">Log in</router-link>
                        </div>
                    </div>
                    </template>
                </div>
            </div>
        </nav>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AppHeader',
    data() {
        return {
            notification: [],
            notificationCount: 0
        }
    },
    mounted() {
        this.countNotification()
        // this.getCount()
    },
    watch: {
        notificationCount: function() {
            console.log(this.notificationCount + " - watcher")
        }
    },
    computed: {
        countNotif() {
            return this.$store.getters.notifCount
        }
    },
    methods: {
        countNotification(){
            axios.get(`/api/v1/notifications?is_read=False`)
                .then(response => {
                    this.$store.commit("countNotification", response.data.count)
                    console.log(this.$store.state.notificationCount)
                    this.notificationCount=this.$store.state.notificationCount
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            },
        // getCount(){
        //   this.notificationCount=this.$store.state.notificationCount
        // }
  }

}
</script>
