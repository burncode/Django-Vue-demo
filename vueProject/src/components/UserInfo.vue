<template>
<div class="center-block" style="margin-top: 50px;">
  <table class="table table-striped">
      <caption class="text-center" style="font-size: 20px; font-weight: 600;">用户信息</caption>
      <tbody>
          <tr>
              <td>Username</td>
              <td>{{ userinfo.username }} </td>
          </tr>
          <tr>
              <td>First name</td>
              <td> {{ userinfo.firstname }} </td>
          </tr>
          <tr>
              <td>Last name</td>
              <td> {{ userinfo.lastname }} </td>
          </tr>
          <tr>
              <td>Email address</td>
              <td> {{ userinfo.email }} </td>
          </tr>
          <tr>
              <td>Last login</td>
              <td> {{ userinfo.lastlogin }} </td>
          </tr>
          <tr>
              <td>Date joined</td>
              <td> {{ userinfo.datejoined }} </td>
          </tr>
      </tbody>
  </table>
</div>
</template>

<script>
export default {
  name: 'user-info',
  data: function(){
      return {
          getUserInfoUrl: '/user/user_info',
          userinfo: {},
      };
  },
  props: {
      isLogin: {
          tyep: String,
          required: true,
      },
  },
  methods: {
      getUserInfo: function(){
          var vm = this;
          this.$http.get(this.getUserInfoUrl).then((res) => {
              if(res.ok){
                  vm.userinfo = res.data;
              } else {
                  vm.userinfo = {};
              }
          }, (err) => {
              vm.userinfo = {};
          });
      },
      clearUserInfo: function(){
          this.userinfo = {};
      },
  },
  watch: {
      isLogin: function(oldVal, newVal){
          if(this.isLogin){
              this.getUserInfo();
          } else {
              this.clearUserInfo();
          }
      },
  },
}
</script>