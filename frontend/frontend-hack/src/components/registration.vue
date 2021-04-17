<template>
  <div class="auth-block">
    <div class="auth-block__reg" v-if="this.isActiveBtn">
        <div class="btns-block">
            <button class="btn-login">Я студент</button>
            <button class="btn-login not-active" v-on:click="isActiveBtn = false">Я работодатель</button>
        </div>
        <form action="">
            <input v-model="firstname" class="default-input" type="text" placeholder="Имя" required>
            <input v-model="secondname" class="default-input" type="text" placeholder="Фамилия" required>
            <input v-model="lastname" class="default-input" type="text" placeholder="Отчество" required>
            <input v-model="dateborn" class="default-input" type="text" placeholder="Дата рождения" required>
            <input v-model="sex" class="default-input" type="text" placeholder="Пол" required>
            <input v-model="email" class="default-input" type="email" placeholder="Адрес эл.почты" required>
            <input v-model="institut" class="default-input" type="text" placeholder="Учебное заведение" required>
            <input v-model="chair" class="default-input" type="text" placeholder="Направление обучения" required>
            <input v-model="password" class="default-input" type="password" placeholder="Пароль" required>
            <input v-model="passwordconfirm" class="default-input" type="password" placeholder="Подтвердите пароль" required>
            <button class="btn-submit" type="submit" @click="regStudent">Зарегистрироваться</button>
        </form>
    </div>
    <div class="auth-block__reg" v-else>
        <div class="btns-block">
            <button class="btn-login not-active" v-on:click="isActiveBtn = true">Я студень</button>
            <button class="btn-login">Я работодатель</button>
        </div>
        <form action="">
            <input v-model="firstname" class="default-input" type="text" placeholder="Имя" required>
            <input v-model="secondname" class="default-input" type="text" placeholder="Фамилия" required>
            <input v-model="lastname" class="default-input" type="text" placeholder="Отчество" required>
            <input v-model="dateborn" class="default-input" type="text" placeholder="Дата рождения" required>
            <input v-model="sex" class="default-input" type="text" placeholder="Пол" required>
            <input v-model="email" class="default-input" type="email" placeholder="Адрес эл.почты" required>
            <input v-model="organization" class="default-input" type="text" placeholder="Организация" required>
            <input v-model="password" class="default-input" type="password" placeholder="Пароль" required>
            <input v-model="passwordconfirm" class="default-input" type="password" placeholder="Подтвердите пароль" required>
            <button class="btn-submit" type="submit" @click="regEmployer">Зарегистрироваться</button>
        </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
axios.defaults.headers.common = "Access-Control-Allow-Origin";
export default {
  setup() {},
  data() {
    return {
      isActiveBtn: true,
      firstname: "",
      email: "",
      secondname: "",
      lastname: "",
      dateborn: "",
      sex: "",
      organization: "",
      password: "",
      passwordconfirm: "",
      chair: "",
      institut: "",
    };
  },
  methods: {
    regStudent(e){
        e.preventDefault()
        // const headers = "Access-Control-Allow-Origin: *"
        axios.post('http://6da79bcfcdd5.ngrok.io/api/auth/users/', {
          first_name: this.firstname,
          last_name: this.secondname,
          email: this.email,
          password: this.password
        })
        .then(
            response =>{
                console.log("response status: ", response.status);
                console.log("this: ", response.status);
            }
        ).catch(function (error) {
              console.error(error.response)});
        console.log("reg Student", e);
    },
    regEmployer(e){
        console.log("reg Employer", e);
    }
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
    margin: 0 35px 25px 35px;
}

.btn-submit{
    background-color: #1319AD;
    color: #fff;
    border-radius: 50px;
    padding: 10px;
    margin: 0 50px;
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
