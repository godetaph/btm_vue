<template>
  <div class="column is-12 box">
      <div class="columns">
        <div class="column is-4">
            <div class="select is-small">
              <select name="criteria" id="" class="select" @change="getCriteria($event)">
                <option value="" selected>-- Select field --</option>
                <option value="permit">Business permit</option>
                <option value="notice">Permit status</option>
                <option value="ownership">Ownership type</option>
                <option value="status">Business status</option>
                <option value="payment">Payment type</option>
                <option value="application">Application status</option>
                <option value="location">Location status</option>
              </select>
          </div>
        </div>
         <div class="column is-3">
            <div class="select is-small"> 
              <select name="" id="" class="select" @change="getBarangayMap($event)" >
                <option value="" class="">--Select barangay--</option>
                <option value="0">All barangay</option>
                <option v-for="barangay in barangays" :key="barangay.id" :value="barangay.id">{{barangay.barangay_name}}</option>
              </select>
            </div>
        </div>
      </div>
      <div class="column is-12 notification is-light">
          <p>Total count: <strong>{{businesses.length}}</strong></p>
          <p v-if="criteria == 'barangay'">Barangay: <strong>{{brgy}}</strong></p>
          <p v-if="icon1">
              <img :src="icon1" alt=""> {{icon_label1}}
          </p>
          <p v-if="icon2">
              <img :src="icon2" alt=""> {{icon_label2}}
          </p>
          <p v-if="icon3">
              <img :src="icon3" alt=""> {{icon_label3}}
          </p>
          <p v-if="icon4">
              <img :src="icon4" alt=""> {{icon_label4}}
          </p>
          <p v-if="icon5">
              <img :src="icon5" alt=""> {{icon_label5}}
          </p>
      </div>
      
      <div class="columns">
      <!-- types: roadmap, sateillite, hybrid, terrain -->
      <div class="column is-12">
        <GMapMap
            :center="center"
            :zoom="zoom"
            map-type-id="terrain" 
            style="width: 100%; height: 700px"
        >
          <!-- <GMapCluster> -->
            <GMapMarker
                :key="index"
                v-for="(m, index) in markers"
                :position="m.position"
                :icon="m.icon_type"
                :clickable="true"
                :draggable="true"
                @click="openMarker(m.id)"
                
            >
            <div class="">
              <GMapInfoWindow :opened="openedMarkerID === m.id">
                <div v-if="m.permit=='yes'"><strong>{{m.business}}</strong>
                  <div class="is-size-7 mt-1">
                    <span class="tag is-primary is-rounded">{{m.permit}}</span>
                    <span class="tag is-warning is-rounded" v-if="m.business_status=='ACTIVE1'">Active w/o extension</span>
                    <span class="tag is-primary is-rounded" v-if="m.business_status=='ACTIVE2'">Active with extension</span>
                    <span class="tag is-danger is-rounded" v-if="m.business_status=='INACTIVE'">Inactive</span>
                  </div>
                  <div class="is-size-7 mt-1">
                    <span class="tag is-primary is-rounded">{{m.ownership_type}}</span>
                    <span class="tag is-primary is-rounded" v-if="m.payment_type=='annual'">Annually</span>
                    <span class="tag is-info is-rounded" v-if="m.payment_type=='semi-annual'">Semi-Annually</span>
                    <span class="tag is-warning is-rounded" v-if="m.payment_type=='quarterly'">Quarterly</span>
                  </div>
                  
                
                  <MyComponent/>
                </div>
                <div v-if="m.permit=='no'"><strong>{{m.business}}</strong>
                  <div class="is-size-7 mt-1">
                    <span class="tag is-danger is-rounded">{{m.permit}}</span>
                    <span class="tag is-warning is-rounded" v-if="m.business_status=='ACTIVE1'">Active w/o extension</span>
                    <span class="tag is-primary is-rounded" v-if="m.business_status=='ACTIVE2'">Active with extension</span>
                    <span class="tag is-danger is-rounded" v-if="m.business_status=='INACTIVE'">Inactive</span>
                </div>
                <div class="is-size-7 mt-1">
                    <span class="tag is-primary is-rounded">{{m.ownership_type}}</span>
                    <span class="tag is-primary is-rounded" v-if="m.payment_type=='annual'">Annually</span>
                    <span class="tag is-info is-rounded" v-if="m.payment_type=='semi-annual'">Semi-annually</span>
                    <span class="tag is-warning is-rounded" v-if="m.payment_type=='quarterly'">Quarterly</span>
                  </div>
                <MyComponent/>
                </div>
              </GMapInfoWindow>
            </div>
            </GMapMarker>
          <!-- </GMapCluster> -->
        </GMapMap>

        <!-- <div class="column is-12">
          <ul>
            <li v-for="m in markers" v-bind:key="m.id">{{m.position}}, {{m.businesses}}, {{m.id}}</li>
           
          </ul>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BtmMap',
  data() {
    return {
        openedMarkerID: null,
        showInfo: false,
        criteria:'',
        zoom:10,
        businesses:[],
        barangays:[],
        brgy:'',
        choice: '',
        icon1: '',
        icon2: '',
        icon3: '',
        icon4: '',
        icon5: '',
        icon_label1: '',
        icon_label2: '',
        icon_label3: '',
        icon_label4: '',
        icon_label5: '',
        center: { 
                lat: 7.189447, 
                lng: 124.532875 
            },
        marks: {
          business:'',
          position: {
            lat:'',
            lng:''
          },
        },
        markers: [{
          id: '',
          business:'LGU Midsayap',
          permit: '',
          business_status:'',
          ownership_type:'',
          payment_type:'',
          icon_type:'',
          bar_name:'',
          position: {
            lat:7.189447,
            lng:124.532875 
          },
        },],

    }
  },
  mounted() {
    // this.getPermits()
    this.getBarangays()
  },
  methods: {
    getDefault() {
      axios.get('/api/v1/businesses/?size=1000000')
           .then(response => {
             this.markers.length=0
             this.businesses=response.data.results
             let busStatus=''
             let icon = ''
             for (let i = 0; i < response.data.results.length; i++) {

               const element = response.data.results[i];


                // if (this.criteria == 'permit'){
                if (element.business_status == 'ACTIVE1'){
                  busStatus="Active w/o extension"
                } else if( element.business_status == 'ACTIVE2'){
                  busStatus="Active with extension"
                } else {
                  busStatus="Inactive"
                }

                // if (element.is_business_permit=='yes')
                //   icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
                // else 
                //   icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
                console.log(this.criteria + ' - all')
                switch (this.criteria) {
                    case 'permit':
                      if (element.is_business_permit=='yes')
                        {
                          icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
                          
                        }
                      else 
                        {
                          icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
                          
                        }

                      break;
                    case 'notice':
                      console.log(this.criteria + ' - inside notice')
                      if (element.business_permit_status == 'FIRST')
                        {
                          icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'         
                          }
                      else if (element.business_permit_status == 'SECOND')
                        {
                          icon = 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png'
                        }
                      else if (element.business_permit_status == 'FINAL')
                        {
                          icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
                        }
                      else if (element.business_permit_status == 'CLOSURE')
                        {
                          icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
                        }
                      else if (element.business_permit_status == 'null' || element.business_permit_status == 'undefined' || element.business_permit_status.length === 0)
                        {
                          icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
                        }
                        
                      break;
                    case 'ownership':
                      console.log(this.criteria + ' - inside ownership' + ' - ' + element.ownership_type)
                      if (element.ownership_type == 'single') {
                        icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
                      }
                      else if (element.ownership_type == 'partnership')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.ownership_type == 'corporation')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/orange-dot.png'}
                      else if (element.ownership_type == 'cooperative')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png'}
                      else
                        icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
                      break;
                    case 'status':
                      if (element.business_status == 'ACTIVE1')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.business_status == 'ACTIVE2')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.business_status == 'INACTIVE')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}
                      break;
                    case 'payment':
                      if (element.payment_type == 'annual')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.payment_type == 'semi-annual')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.payment_type == 'quarterly')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png'}
                      else if (element.payment_type == 'null' || element.payment_type == 'undefined')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      break;
                    case 'application':
                      if (element.application_status == 'new')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.application_status == 'renew')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.application_status == 'null' || element.application_status == 'undefined' || lement.application_status == '')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      break;
                    case 'location':
                      if (element.location_status == 'owned')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.location_status == 'rented')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.location_status == 'null' || element.location_status == 'undefined' || element.location_status == '')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      break;
                    default:
                      break;
                  }


                //   if (element.is_business_permit == 'no'){
                this.markers.push({"id": element.id, "business":element.business_name, "permit":element.is_business_permit, "business_status": element.business_status, "ownership_type":element.ownership_type, "payment_type":element.payment_type, "icon_type": icon, "position": {"lat":parseFloat(element.gps_latitude), "lng": parseFloat(element.gps_longitude)},})
                  // }
                // }
             }
            console.log(this.markers)
           })
           .catch(error => {
             console.log(JSON.stringify(error))
           })
    },
    getCriteria(event) {
      console.log(event.target.value)

      switch (event.target.value) {
        case 'permit': 
          this.icon1= 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
          this.icon_label1=" [Yes] - with business permit"
          this.icon2= 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
          this.icon_label2=" [No] - without business permit"
          this.icon3= ''
          this.icon_label3=''
          this.icon4= ''
          this.icon_label4=''
          this.icon5= ''
          this.icon_label5=''
          break;
        case 'notice':
          this.icon1= 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
          this.icon_label1=" [FIRST] - First notice"
          this.icon2= 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png'
          this.icon_label2=" [SECOND] - Second notice"
          this.icon3='http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
          this.icon_label3=" [FINAL] - Third notice"
          this.icon4='http://maps.google.com/mapfiles/ms/icons/red-dot.png'
          this.icon_label4=" [CLOSURE] - Subject for closure"
          this.icon5= 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
          this.icon_label5=" No data available"
          break;
        case 'ownership':
          this.icon1= 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
          this.icon_label1=" [SINGLE] - Single proprietorship"
          this.icon2= 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
          this.icon_label2=" [PARTNER] - Partnership"
          this.icon3='http://maps.google.com/mapfiles/ms/icons/orange-dot.png'
          this.icon_label3=" [CORPO] - Corporation"
          this.icon4='http://maps.google.com/mapfiles/ms/icons/purple-dot.png'
          this.icon_label4=" [COOP] - Cooperative"
          this.icon5= 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
          this.icon_label5=" No data available"
          break;
        case 'status':
          this.icon1= 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
          this.icon_label1=" [ACTIVE W/O] - Active without extension"
          this.icon2= 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
          this.icon_label2=" [ACTIVE] - Active with extension"
          this.icon3='http://maps.google.com/mapfiles/ms/icons/red-dot.png'
          this.icon_label3=" [INACTIVE] - Inactive"
          this.icon4='http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
          this.icon_label4=" No data available"
          this.icon5= ''
          this.icon_label5=''
          break;
        case 'payment':
          this.icon1= 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
          this.icon_label1=" [ANNUAL] - Payment done once a year."
          this.icon2= 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
          this.icon_label2=" [SEMI-ANNUAL] - Payment done every six months of the year."
          this.icon3='http://maps.google.com/mapfiles/ms/icons/purple-dot.png'
          this.icon_label3=" [QUARTER] - Payment done every quarter of the year."
          this.icon4='http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
          this.icon_label4=" No data available"
          this.icon5= ''
          this.icon_label5=''
          break;
        case 'application':
          this.icon1= 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
          this.icon_label1=" [New] - New application."
          this.icon2= 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
          this.icon_label2=" [RENEW] - Renewal of application"
          this.icon3='http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
          this.icon_label3=" No data available"
          this.icon4= ''
          this.icon_label4=''
          this.icon5= ''
          this.icon_label5=''
          break;
        case 'location':
          this.icon1= 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
          this.icon_label1=" [OWNED] - Location is owned by the business owner."
          this.icon2= 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
          this.icon_label2=" [RENTED] - Location is rented by the business owner."
          this.icon3='http://maps.google.com/mapfiles/ms/icons/pink-dot.png'
          this.icon_label3=" No data available"
          this.icon4= ''
          this.icon_label4=''
          this.icon5= ''
          this.icon_label5=''
          break;
        default:
          this.businesses.length=0
          this.markers.length=0
          break;
      }
      
      this.criteria=event.target.value
    },
    openMarker(id) {
       this.openedMarkerID = id
       this.showInfo = true
    },
    getBarangays(){
      axios.get('/api/v1/barangays/?size=1000')
          .then(response => {
            this.barangays = response.data.results
          })
          .catch(error => JSON.stringify(error))
    },
    getBarangayMap(event) {
      const bar = event.target.value
      console.log(bar + ' - bar')
      if (bar > 0){
        axios.get(`/api/v1/businesses/?bar=${bar}&size=100000`)
            .then(response => {
              this.markers.length=0
              this.businesses=response.data.results
              this.brgy=response.data.results[0].bar_name
              let busStatus=''
              let icon = ''
              for (let i = 0; i < response.data.results.length; i++) {

                const element = response.data.results[i];

                  // if (this.criteria == 'permit'){
                  if (element.business_status == 'ACTIVE1'){
                    busStatus="Active w/o extension"
                  } else if( element.business_status == 'ACTIVE2'){
                    busStatus="Active with extension"
                  } else {
                    busStatus="Inactive"
                  }
                  console.log(this.criteria + ' - criteria')
                  switch (this.criteria) {
                    case 'permit':
                      if (element.is_business_permit=='yes')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else 
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}
                      break;
                    case 'notice':
                      //console.log(this.criteria + ' - inside notice')
                      if (element.business_permit_status == 'FIRST')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.business_permit_status == 'SECOND')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png'}
                      else if (element.business_permit_status == 'FINAL')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.business_permit_status == 'CLOSURE')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/black-dot.png'}
                      break;
                    case 'ownership':
                      //console.log(this.criteria + ' - inside ownership' + ' - ' + element.ownership_type)
                      if (element.ownership_type == 'single') {
                        icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
                      }
                      else if (element.ownership_type == 'partnership')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.ownership_type == 'corporation')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/orange-dot.png'}
                      else if (element.ownership_type == 'cooperative')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      break;
                    case 'status':
                      if (element.business_status == 'ACTIVE1')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.business_status == 'ACTIVE2')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.business_status == 'INACTIVE')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}
                      break;
                    case 'payment':
                      if (element.payment_type == 'annual')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.payment_type == 'semi-annual')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.payment_type == 'quarterly')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png'}
                      else if (element.payment_type == 'null' || element.payment_type == 'undefined' || element.payment_type == '')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      break;
                      break;
                    case 'application':
                      if (element.application_status == 'new')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.application_status == 'renew')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else if (element.payment_type == 'null' || element.payment_type == 'undefined' || lement.payment_type == '')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      break;
                    case 'location':
                      if (element.location_status == 'owned')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'}
                      else if (element.location_status == 'rented')
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'}
                      else
                        {icon = 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png'}
                      break;
                    default:
                      break;
                  }

                  
                  //   if (element.is_business_permit == 'no'){
                  this.markers.push({"id": element.id, "business":element.business_name, "permit":element.is_business_permit, "business_status": element.business_status, "ownership_type":element.ownership_type, "payment_type":element.payment_type, "icon_type": icon, "position": {"lat":parseFloat(element.gps_latitude), "lng": parseFloat(element.gps_longitude)},})
                    // }
                  // }
              }
              console.log(this.markers)
            })
            .catch(error => JSON.stringify(error))

            this.zoom=12
      }
      else {
        this.getDefault()
        this.zoom=12
      }
    }
  }
}
</script>