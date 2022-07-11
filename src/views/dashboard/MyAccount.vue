<template>
    <div class="page-my-account">
        <div class="is-size-5"><strong>BTM</strong> | <span class="has-text-info">My</span>Account</div>
        <hr>
        <strong>Team: </strong> {{team.name}} <br>
        <strong>Address: </strong> {{team.team_address}} <br>
        <strong>Username: </strong> <span class="tag is-info">{{$store.state.user.username}}</span> 
        <hr>

        <div class="buttons">
            <router-link to="/dashboard/my-account/edit-team" class="button is-outline-black is-small">Edit team</router-link>
            <button @click="logout()" class="button is-danger is-small">Log out</button>
        </div>
        
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'MyAccount',
    data() {
        return {
            team: {}
        }
    },
    async mounted() {
        await this.getTeam()
    },
    methods: {
        getTeam() {
            axios.get('/api/v1/teams/')
                 .then(response => {
                     this.team=response.data[0]
                 })
                 .catch(error => JSON.stringify(error))
        },
        logout() {
            axios.post("/api/v1/token/logout/", this.$store.state.refresh_token)
                 .then(response => {
                     axios.defaults.headers.common['Authorization'] = ""
                     localStorage.removeItem('username')
                     localStorage.removeItem('userid')
                     localStorage.removeItem('token')
                     this.$store.commit('removeToken')
                     this.$router.push('/')
                 })
                 .catch(error => {
                     if (error.response) {
                         console.log(JSON.stringify(error.response.data))
                     } else if (error.message) {
                        console.log(JSON.stringify(error.message))
                     } else {
                         console.log(JSON.stringify(error))
                     }
                 })
        }
    }
}
</script>