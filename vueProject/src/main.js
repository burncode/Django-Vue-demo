import Vue from 'vue'
import VueResource from 'vue-resource'
import UserApp from './components/UserApp.vue'

Vue.use(VueResource);

new Vue({
  el: '#app',
  render: h => h(UserApp)
})