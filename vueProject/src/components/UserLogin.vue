<template>
<div class="center-block">
        <div class="input-group">
            <span class="input-group-addon" id="basic-addon1">用户名</span>
            <input type="text" class="form-control" aria-describedby="basic-addon1" v-model="username" required="required" ref="input-username">
        </div>
        <br/>
        <div class="input-group">
            <span class="input-group-addon" id="basic-addon1">密&nbsp;&nbsp;&nbsp;&nbsp;码</span>
            <input type="password" class="form-control" aria-describedby="basic-addon1"  v-model="password" required="required" ref="input-password"
            @keyup.enter="onClickAction">
        </div>
        <br/>
        <p class="text-center">
            <button @click="onClickAction" class="btn btn-danger" v-if="isLogin">注销</button>
            <button @click="onClickAction" class="btn btn-default" v-else>登录</button>
        </p>
        <div class="alert alert-danger alert-dismissible" role="alert" ref="login-error-alert" v-show="errorMsg.length > 0">
            <button type="button" class="close" @click="onClickCloseAlert"><span aria-hidden="true">&times;</span></button>
             {{ errorMsg }} 
        </div>

</div>
</template>

<script>

export default {
    name: 'user-login',
    data: function(){
        return {
            username: 'linghuchong',
            password: 'test1234',
            isLogin: false,
            errorMsg: "",
            loginUrl: 'http://127.0.0.1:8000/user/login',
            logoutUrl: 'http://127.0.0.1:8000/user/logout',
        };
    },
    computed: {
    },
    methods: {
        login: function(){
            var vm = this;
            this.$http.post(this.loginUrl, {
                'username': this.username,
                'password': this.password
            }).then((res) => {
                if(!res.ok){
                    vm.isLogin = false;
                    vm.showError('登录失败，服务器发生错误');
                    return;
                }
                if(res.data['code'] === 100){
                    // 登录成功
                    console.info('登录成功');
                    vm.isLogin = true;
                    vm.dismissError();
                } else {
                    // 登录失败
                    console.info('登录失败');
                    vm.isLogin = false;
                    vm.showError('登录失败，用户名或密码错误');
                }
            }, (err) => {
                console.error(err);
                vm.isLogin = false;
                vm.showError('登录失败，服务器发生错误');
            });
        },
        logout: function(){
            var vm = this;
            this.$http.get(this.logoutUrl).then((res) => {
                if(res.ok){
                    vm.isLogin = false;
                } else {
                    console.info('注销用户时发生错误，res.ok = false');
                }
            }, (err) => {
                console.info('注销用户时发生错误' + err);
            });
        },
        onClickAction: function(){
            if(this.isLogin){
                this.logout();
            } else {
                this.login();
            }
        },
        onClickCloseAlert: function(){
            this.dismissError();
        },
        showError: function(msg){
            this.errorMsg = msg;
        },
        dismissError: function() {
            this.errorMsg = "";
        },
    },
    watch: {
        isLogin: function(oldVal, newVal){
            console.info('watch isLogin');
            this.$emit('loginchanged', this.isLogin);
        },

    },
    created: function() {
            this.login();
    },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
