<template>
  <div class="page-edit-team">
      <div class="columns is-multiline">
          <div class="column is-12">
              <div class="is-size-5"><strong>BTM</strong> | <span class="has-text-info">Update</span>Team</div>
                <hr>
                <div class="column is-3">
                    <div class="is-size-7">Organization number</div>
                    <div class="control">
                        <input type="text" class="input is-small" v-model="team.org_number">
                    </div>
                </div>
                <div class="column is-8">
                    <div class="is-size-7">Organization name</div>
                    <div class="control">
                        <input type="text" class="input is-small" v-model="team.name">
                    </div>
                </div>
                <div class="column is-8">
                    <div class="is-size-7">Address</div>
                    <div class="control">
                        <input type="text" class="input is-small" v-model="team.team_address">
                    </div>
                </div>
                <div class="column is-3">
                    <div class="is-size-7">Zip code</div>
                    <div class="control">
                        <input type="text" class="input is-small" v-model="team.zip_code">
                    </div>
                </div>

                <div class="control mt-4">
                    <button class="button is-success ml-3 is-small" @click="submitForm">Submit data</button>
                </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'EditTeam',
    data() {
        return {
            team: {}
        }
    },
    mounted() {
        this.getOrCreateTeam()
    },
    methods: {
        getOrCreateTeam(){
            axios.get('/api/v1/teams/')
                 .then(response => {
                     this.team=response.data[0]
                 })
                 .catch(error => JSON.stringify(error))
        },
        submitForm(){
            axios.patch(`/api/v1/teams/${this.team.id}/`, this.team)
                 .then(response => {
                     toast ({
                        message: 'Updated period successfully.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center',
                     })
                     this.$router.push("/dashboard/my-account")
                 })
        }
    }
}
</script>

<style>

</style>