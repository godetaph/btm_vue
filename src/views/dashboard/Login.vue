<template>
    <div class="page-login">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <div class="box">
                    <h1 class="title is-5">Login</h1>

                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <label for="">Username</label>
                            <div class="control">
                                <input type="input" class="input" name="username" v-model="username">
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Password</label>
                            <div class="control">
                                <input type="password" class="input" name="password" v-model="password">
                            </div>
                        </div>
                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">
                                {{error}}
                            </p>
                        </div>
                        <div class="field">
                            <div class="control">
                                <button class="button is-success">Login</button>
                            </div>
                        </div>
                    </form>
                    <hr>
                    
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async submitForm(e) {
            axios.defaults.headers.common['Authorization'] = ""
            localStorage.removeItem("token")
            const formData = {
                username: this.username,
                password: this.password
            }
            await axios.post("/api/v1/token/login/", formData)
                       .then(response => {
                           const token = response.data.auth_token
                           this.$store.commit('setToken', token)
                           axios.defaults.headers.common['Authorization'] = "Token " + token
                           localStorage.setItem("token", token)
                       })
                       .catch(error => {
                           if (error.response) {
                                for (const props in error.response.data) {
                                    this.errors.push(`${props}: ${error.response.data[props]}`)
                                }
                                console.log(JSON.stringify(error.response.data))
                            } else if (error.message) {
                                console.log(JSON.stringify(error.message))
                            } else {
                                console.log(JSON.stringify(error))
                            }
                       })

            axios.get("/api/v1/users/me/")
                 .then(response => {
                     let level = ''
                     //if (response.data.username.)
                     if (response.data.username.substring(0,3) == 'adm'){
                         level='admin'
                     }
                     else{
                         level='staff'
                     }
                     this.$store.commit('setUser', {
                         'username': response.data.username,
                         'id': response.data.id,
                         'level': level
                     })
                     localStorage.setItem('username', response.data.username)
                     localStorage.setItem('userid', response.data.id)
                     localStorage.setItem('level', level)

                     this.$router.push('/dashboard')
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>