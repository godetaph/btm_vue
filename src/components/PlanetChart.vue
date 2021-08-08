<template>
    <div>
        <div class="box">
            <div><strong class="is-size-7 has-text-grey-light">Collections</strong></div>
            <canvas id="myChart" ></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js'
// import planetChartData from '../planet-data.js'

export default {
    name: 'PlanetChart',
    data() {
        return {
            // planetChartData: planetChartData
        }
    },
    mounted() {
        const ctx = document.getElementById('myChart').getContext('2d')
        // new Chart(ctx, this.planetChartData)
        var myChart = new Chart(ctx, {
                type: "line",
                data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                datasets: [
                    {
                    label: "Quarterly",
                    type: "line",
                    data: [0, 0, 1, 2, 79, 82, 27, 14, 10, 11, 300, 400],
                    backgroundColor: "rgba(54,73,93,.5)",
                    borderColor: "#36495d",
                    borderWidth: 3
                    },
                    {
                    label: "Semi-annual",
                    type: "bar",
                    data: [0.166, 2.081, 3.003, 0.323, 954.792, 285.886, 43.662, 51.514],
                    backgroundColor: "rgba(71, 183,132,.5)",
                    borderColor: "#47b784",
                    borderWidth: 3
                    },
                ]
                },
                options: {
                responsive: true,
                lineTension: 1,
                scales: {
                    yAxes: [
                    {
                        ticks: {
                        beginAtZero: true,
                        padding: 25
                        }
                    }
                    ]
                }
                }
            });
    },
    methods: {

    }

}
</script>

<style>

</style>