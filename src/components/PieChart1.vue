<template>
    <div>
        <div class="box">
            <div><strong class="is-size-7 has-text-grey-light">Notifications</strong></div>
            <canvas id="pieChart1" ></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js'

export default {
    name: 'PieChart1',
    data() {
        return {
            // data: []
        }
    },
    mounted() {
        this.getPie1()
    }, 
    methods: {
        getPie1(){
            const ctx = document.getElementById('pieChart1').getContext('2d')
            // new Chart(ctx, this.planetChartData)
            var pieChart1 = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: [
                        'Read',
                        'Unread',
                    ],
                    datasets: [{
                        label: 'Business permit status',
                        data: [17, 9],
                        backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 205, 86)',
                        ],
                        hoverOffset: 4
                    }]
                }
            })
        }
    }


}
</script>

<style>

</style>