<template>
    <div class="page-businesses">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="is-size-5"><strong>BTM</strong>BusinessList</div>
                <hr>

                <business-list />
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import BusinessList from '../../components/BusinessList.vue'
// import BusinessList from './BusinessList.vue'
export default {
  components: { BusinessList },
    name: 'Businesses',
    // data() {
    //     return {
    //         businesess: [],
    //         currentPage: 1,
    //         showNext: false,
    //         showPrev: false,
    //         query: ''
    //     }
    // },
    // mounted() {
    //     this.getBusinesses()
    // },
    // methods: {
    //     loadNext() {
    //         this.currentPage += 1
    //         this.getBusinesses()
    //     },
    //     loadPrev() {
    //         this.currentPage -= 1
    //         this.getBusinesses()
    //     },
    //     getBusinesses() {
    //         axios.get(`/api/v1/businesses/?page=${this.currentPage}&search=${this.query}`) 
    //              .then(response => {
    //                  this.showNext=false
    //                  this.showPrev=false
    //                  this.businesess=response.data.results
    //                 //  for(let i=0; i < response.data.length; i++){
    //                 //      this.businesess.push(response.data[i])
    //                 //  }
    //                  if (response.data.next){
    //                      this.showNext=true
    //                  }
    //                  if (response.data.previous){
    //                      this.showPrev=true
    //                  }
    //                  //this.businesses = response.data
    //              })
    //              .catch(error => {
    //                  console.log(error)
    //              })
    //     },
    //     submitForm() {
    //         this.getBusinesses()
    //     }
    //}

}
</script>