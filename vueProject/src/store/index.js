import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

var store = new Vuex.Store({
  state: {
    isLogin: false,
  },
  mutations: {
    onLoginStateChanged(state, isLogin) {
      state.isLogin = Boolean(isLogin);
    },
  },
  actions: {

  },

});
export default store;