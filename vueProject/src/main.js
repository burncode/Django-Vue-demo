import Vue from 'vue'
import VueResource from 'vue-resource'
import UserApp from './components/UserApp.vue'
import store from './store'

Vue.use(VueResource)

new Vue({
  el: '#app',
  store,
  render: h => h(UserApp)
})