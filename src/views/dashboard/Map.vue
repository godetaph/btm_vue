<template>
    <div class="page-mapa">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong>Mapping</div>
            </div>
            <div class="column">
                <google-map />
            </div>
        </div>
    </div>
</template>

<script>
import GoogleMap from '../../components/BtmMap.vue'
export default {
    name: 'Map',
    components: {
        GoogleMap
    }
}
</script>

<style>

</style>