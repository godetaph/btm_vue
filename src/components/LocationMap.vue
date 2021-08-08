<template>
    <!-- types: roadmap, sateillite, hybrid, terrain -->
        <GMapMap
            :center="center"
            :zoom="14"
            map-type-id="roadmap" 
            style="width: 100%; height: 650px"
        >
            <GMapCluster>
                <GMapMarker
                    :key="index"
                    v-for="(m, index) in markers"
                    :position="m.position"
                    :clickable="true"
                    :draggable="true"
                    @click="center=m.position"
                />
            </GMapCluster>
        </GMapMap>
</template>

<script>
export default {
    name: 'LocationMap',
    data() {
        return {
            center: { lat: 7.010607, lng: 125.091134 },
            marks: {
            position: {
                    lat:'',
                    lng:''
                }
            },
            markers: [
            {
                position: {
                lat: 6.983094,
                lng: 125.103259
                }
            },
            {
                position: {
                lat: 7.010781,
                lng: 125.084420
                }
            },
            {
                position: {
                lat: 7.025494,
                lng: 125.083662
                }
            },
            {
                position: {
                lat: 7.023808,
                lng: 125.096393
                }
            }
            ]
        }
    },
}
</script>

<style>

</style>