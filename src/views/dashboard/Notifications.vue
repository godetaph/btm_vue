<template>
  <div class="page-notifications">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="is-size-5"><strong>BTM</strong>Notifications</div>
              <hr>
                <div class="column is-12">
                    <form @submit.prevent="submitForm" action="" class="mb-4">
                        <div class="field has-addons">
                            <div class="control">
                                <input type="text" class="input is-small" style="width:300px;" v-model="query">
                            </div>
                            <div class="control">
                                <button class="button is-success ml-2 is-small">Search</button>
                            </div>
                            <!-- <div class="control">
                                <button class="button is-light ml-2 is-small" @click="showSearch">Advanced search</button>
                            </div> -->
                        </div>
                    </form>

                    <div class="is-size-7 mb-2"><strong class="has-text-grey-light">NOTIFICATION DISPLAY</strong> </div>

                    <div class="notification" v-for="notification in notifications" v-bind:key="notification.id">
                        <button class="delete is-pulled-right" @click="deleteNotification(notification)" v-if="this.$store.state.user.level=='admin'"></button>
                        <div class="title is-6 mb-4 has-text-primary">{{notification.business_name}}</div>
                        <p class="mb-2 has-text-dark">Message: <strong>{{notification.message}}</strong></p>
                        <p v-if="notification.append_type=='Period'"><span class="tag is-info">{{notification.append_type}}</span> - on {{notification.created_on}} | {{notification.created}} ago</p>
                        <p v-else><strong class="tag is-info">{{notification.append_type}}</strong>  - on {{notification.created_on}} | {{notification.created}} ago</p>
                        <p v-if="!notification.is_read" class="has-text-danger">Read: <strong>No</strong></p>
                        <p v-else>Read : <strong>Yes</strong></p>
                        <button @click="clickRead(notification)" v-if="!notification.is_read" class="button is-dark mt-4 is-small">Read</button>
                    </div>

                     <div class="buttons">
                        <button class="button is-outlined is-dark" @click="loadNext()" v-if="showNext">Next page</button>
                        <button class="button is-outlined is-dark" @click="loadPrev()" v-if="showPrev">Previous page</button>
                    </div>
                </div>
               
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import Swal from 'sweetalert2'

export default {
    name: 'Notifications',
    data() {
        return {
            notifications: [],
            notification: {},
            countNotification:0,
            isDeleted:false,
            currentPage: 1,
            showNext: false,
            showPrev: false,
            query: ''
        }
    },
    async mounted() {
        await this.getNotifications()
        await this.getCount()
    },
    methods: {
        loadNext() {
            this.currentPage += 1
            this.getNotifications()
        },
        loadPrev() {
            this.currentPage -= 1
            this.getNotifications()
        },
        getNotifications() {
            this.notifications=[]
            axios.get(`/api/v1/notifications/?page=${this.currentPage}&search=${this.query}`)
                 .then(response => {
                    this.showNext=false
                    this.showPrev=false
                    //  for (let i = 0; i < response.data.length; i++) {
                    //      this.notifications.push(response.data[i])   
                    //  }
                    this.notifications=response.data.results

                    if (response.data.next){
                        this.showNext=true
                    }
                    
                    if (response.data.previous){
                        this.showPrev=true
                    }
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        submitForm(){
            this.getNotifications()
        },
        clickRead(notification) {
            this.notification=notification
            this.notification.is_read=true
            axios.patch(`/api/v1/notifications/${notification.id}/`,this.notification)
                 .then(response => {
                     console.log(response.statusText)
                     toast ({
                        message: 'New business category was added successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 1000,
                        position: 'bottom-center',
                     })
                     this.getCount()
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        },
        deleteNotification(notification){
            Swal.fire({
                title: 'You are about to delete this record.',
                // text: 'Press YES to continue.',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: 'hsl(141, 71%, 48%)',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, continue!'
            }).then((result) => {
                if (result.isConfirmed) {
                    this.notification=notification
                    axios.delete(`/api/v1/notifications/${this.notification.id}/`)
                        .then(response => {
                            this.isDeleted=true
                            this.getNotifications()
                            this.getCount()

                            console.log(response.statusText)
                            Swal.fire({
                                title: 'Deleted!',
                                text: 'Your record has been deleted.',
                                icon: 'success',
                                confirmButtonText: 'Confirmed.'
                            })
                            
                            // this.$router.push('/dashboard/categories')
                        })
                        .catch(error => {
                            console.log(JSON.stringify(error))
                        })

                    
                }
            })
        },
        clickDelete(notification) {
            console.log(notification.id)
            if (confirm("Delete this notification record?")){
                this.notification=notification
                axios.delete(`/api/v1/notifications/${this.notification.id}/`, this.notification)
                    .then(response => {
                        console.log("deleted")
                        this.isDeleted=true
                        toast ({
                            message: 'Notification was deleted successfully.',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 1000,
                            position: 'bottom-center',
                        })
                        //this.$router.push('/dashboard/notifications')
                        //notifications=[]
                        this.getNotifications()
                        this.getCount()
                        // this.$forceUpdate()
                        // this.$router.go()
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            }
        },
        getCount() {
            axios.get("/api/v1/notifications/?is_read=False")
                 .then(response => {
                    this.countNotification=response.data.count
                    this.$store.commit('countNotification', this.countNotification)
                 })
                 .catch(error => {
                     console.log(JSON.stringify(error))
                 })
        }
    }
}
</script>