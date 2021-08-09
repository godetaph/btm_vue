<template>
    <div class="wrapper">
      <app-header />
      <section class="section">
        <router-view></router-view>
      </section>

      <footer class="footer">
        <p class="has-text-centered">Midsayap - Business Tax Mapping System v1.0 | powered by: delta-ph.com (c) 2021</p>
      </footer>
    </div>
</template>
<script>
  import axios from 'axios'
  import AppHeader from './components/AppHeader.vue'
  export default {
    components: { AppHeader },
    name: 'App',
    beforeCreate() {
      this.$store.commit('initializeStore')
      const token = this.$store.state.token
      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
    created() {
      document.title='BTM Midsayap'
    }
  
}
</script>

<style lang="scss">
  @import '../node_modules/bulma';
</style>
