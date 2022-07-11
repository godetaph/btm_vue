import { createApp } from 'vue'
import VueGoogleMaps from '@fawmi/vue-google-maps'
import VueSweetAlert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

//import './filters/format-date'

axios.defaults.baseURL = 'https://btm-101.herokuapp.com' //'http://127.0.0.1:8000'
// axios.defaults.baseURL = 'http://127.0.0.1:8000'


createApp(App).use(store).use(VueSweetAlert2).use(router, axios).use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyCnXgXro5rBNfMYHwmk9ZOeorKf8-IRVXU',
    },
}).mount('#app')


// createApp(App).use(store).use(router, axios, (VueGoogleMaps, {
//     load: {
//         key: "AIzaSyA7YIMYXuzrMKc4LfIk4nTexX8WUe2v9tc",
//         libraries: "places"
//     },
// })).mount('#app')

