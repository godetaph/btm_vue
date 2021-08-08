<template>
    <div>
        <div class="box">
                <div><strong class="is-size-7 has-text-grey-light">Permits</strong></div>
                <canvas id="pieChart" ></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js'

export default {
    name: 'PieChart',
    data() {
        return {
            // data: []
        }
    },
    mounted() {
        this.getPie()
    }, 
    methods: {
        getPie(){
            const ctx = document.getElementById('pieChart').getContext('2d')
            // new Chart(ctx, this.planetChartData)
            var pieChart = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: [
                        'Yes',
                        'No',
                    ],
                    datasets: [{
                        label: 'Business permit status',
                        data: [8, 5],
                        backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
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