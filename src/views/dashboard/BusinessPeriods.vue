<template>
    <div class="page-businesses">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title is-5">Business tax mapped</h1>
                <hr>

                <business-list />
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import BusinessList from '../../components/BusinessMapped.vue'
// import BusinessList from './BusinessList.vue'
export default {
  components: { BusinessList },
    name: 'Businesses',
}
</script>