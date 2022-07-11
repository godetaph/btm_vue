<template>
    <div class="page-reports">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong><span class="has-text-info"></span>Print Reports</div>
                <hr>
                <div class="column is-6">
                    
                </div>
                <vue3-html2pdf
                    :show-layout="false"
                    :float-layout="true"
                    :enable-download="false"
                    :preview-modal="true"
                    :paginate-elements-by-height="1400"
                    filename="ok"
                    :pdf-quality="2"
                    :manual-pagination="false"
                    pdf-format="a4"
                    pdf-orientation="portrait"
                    pdf-content-width="800px"

                   
                    @hasStartedGeneration="hasStartedGeneration()"
                    @hasGenerated="hasGenerated($event)"
                    ref="html2Pdf"
                >
                    <template v-slot:pdf-content>
                        <!-- PDF Content Here -->

                            <body>
                                <h3>This is a sample pdf file</h3>
                            </body>
                        
                    </template>
                </vue3-html2pdf>
                <div>
                    <button class="button" @click="generateReport()">Print</button>
                </div>
            </div>        
        </div>
    </div>
</template>
<script>
import Vue3Html2pdf from 'vue3-html2pdf'
 
export default {
    name: 'ReportPrint',
    components: {
        Vue3Html2pdf
    },
    data() {
        return {
            filename: 'business-list',
        }
    },
    methods: { 
        generateReport () {
            this.$refs.html2Pdf.generatePdf()
        }
    },
}
</script>