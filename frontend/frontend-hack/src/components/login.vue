<template>
  <div class="auth-block">
    <div class="auth-block__reg" v-if="this.isActiveBtn">
        <div class="btns-block">
            <button class="btn-login">Я студент</button>
            <button class="btn-login not-active" v-on:click="isActiveBtn = false">Я работодатель</button>
        </div>
        <form action="">
            <input class="default-input" type="text" placeholder="Адрес эл. почты или телефон">
            <input class="default-input" type="text" placeholder="Пароль">
            <button class="btn-submit">Войти</button>
        </form>
    </div>
    <div class="auth-block__reg" v-else>
        <div class="btns-block">
            <button class="btn-login not-active" v-on:click="isActiveBtn = true">Я студент</button>
            <button class="btn-login">Я работодатель</button>
        </div>
        <form action="">
            <input class="default-input" type="text" placeholder="Адрес эл. почты или телефон">
            <input class="default-input" type="text" placeholder="Пароль">
            <button class="btn-submit">Войти</button>
        </form>
    </div>
  </div>
</template>

<script>
export default {
  setup() {},
  data() {
    return {
      isActiveBtn: true,
    };
  },
  methods: {
    changeActiveBtn() {
      console.log("button", this.isActiveBtn);
    },
  },
};
</script>

<style lang="scss">
.auth-block {
  margin-top: 60px;
  .auth-block__reg{
      display: flex;
      flex-direction: column;
      form{
        display: flex;
        flex-direction: column;
      }
  }
}
.btns-block{
    margin-bottom: 25px;
}

.btn-submit{
    background-color: #1319AD;
    color: #fff;
    border-radius: 50px;
    padding: 10px;
}
.btn-login {
  background: #2c4eff;
  border: 1px solid #2c4eff;
  color: #fff;
  font-size: 16px;
  padding: 10px 70px;
}

.not-active {
  background-color: #fff;
  color: #2c4eff;
  border: 1px solid #2c4eff;
}

.default-input{
    padding: 10px 18px;
    background-color: #F6F6F6;
    border: 1px solid black;
    margin-bottom: 18px;
}
</style>
