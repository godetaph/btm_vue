<template>
    <div class="page-preferences">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title is-5">Preferences</h1>
                <hr>
                <div class="column is-12">
                    <div class="box">
                        <ul>
                            <li><router-link to="/dashboard/categories"><strong>Categories</strong></router-link></li>
                            <li><router-link to="/dashboard/barangays"><strong>Barangays</strong></router-link></li>
                            <li v-if="this.$store.state.user.level=='admin'"><router-link to="/dashboard/periods"><strong>Periodic year (Fical Year)</strong></router-link></li>
                            <hr>
                            <li v-if="this.$store.state.user.level=='admin'"><router-link to="/dashboard/users"><strong>User Management</strong></router-link></li>
                            <hr>
                            <li v-if="this.$store.state.user.level=='admin'"><router-link to="/dashboard/settings"><strong>Settings</strong></router-link></li>
                        </ul>
                    </div>
                </div>
            </div> 
        </div>
    </div>
</template>
<script>
export default {
    name: 'Preferences'
}
</script>