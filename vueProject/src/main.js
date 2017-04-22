import Vue from 'vue'
import VueResource from 'vue-resource'
import UserApp from './UserApp.vue'

Vue.use(VueResource);

new Vue({
  el: '#app',
  render: h => h(UserApp)
})