import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      id: '',
      username: ''
    },
    isAuthenticated: false,
    token: '',
    notificationCount:0,
    qrid:''
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.id = localStorage.getItem('userid')
        state.user.username = localStorage.getItem('username')
      } else {
        state.user.id = '',
        state.user.username = '',
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.user.id = ''
      state.user.username = ''
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user){
      state.user = user
    },
    countNotification(state, count){
      state.notificationCount=count
    }
  },
  getters: {
    notifCount: state => {
      return state.notificationCount
    }
  },
  actions: {
  },
  modules: {
  }
})
