<template>
<div class="container" id="userinfoapp" >
    <user-login v-on:loginchanged="onLoginStateChanged"></user-login>
    <user-info :is-login="isLogin"></user-info>  
</div>
</template>

<script>
import UserLogin from './UserLogin.vue'
import UserInfo from './UserInfo.vue'

export default {
  data () {
    return {
      isLogin: false,
    };
  },
  methods: {
    onLoginStateChanged: function(isLogin){
        console.info('onLoginStateChanged, ' + isLogin);
        this.isLogin = isLogin;
    },
  },
  components : {
    UserLogin,
    UserInfo
  }
}

</script>

<style>
#userinfoapp {
  width: 500px; 
  margin-top: 100px
}
</style>