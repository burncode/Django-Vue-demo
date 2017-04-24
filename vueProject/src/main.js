import Vue from 'vue'
import VueResource from 'vue-resource'
import UserApp from './components/UserApp.vue'
import store from './store'

Vue.use(VueResource)
Vue.http.interceptors.push((request, next) => {
    request.credentials = true;
    next();
});
new Vue({
    el: '#app',
    store,
    render: h => h(UserApp)
})