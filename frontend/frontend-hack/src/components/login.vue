<template>
  <div class="auth-block">
    <div class="auth-block__reg" v-if="this.isActiveBtn">
      <div class="btns-block">
        <button class="btn-login">Я студент</button>
        <button class="btn-login not-active" v-on:click="isActiveBtn = false">
          Я работодатель
        </button>
      </div>
      <form>
        <input
          v-model="email"
          class="default-input"
          type="email"
          placeholder="Адрес эл. почты"
          required
        />
        <input
          v-model="password"
          class="default-input"
          type="password"
          placeholder="Пароль"
          required
        />
        <button class="btn-submit" type="submit" @click="sendStudent">
          Войти как студент
        </button>
      </form>
    </div>
    <div class="auth-block__reg" v-else>
      <div class="btns-block">
        <button class="btn-login not-active" v-on:click="isActiveBtn = true">
          Я студент
        </button>
        <button class="btn-login">Я работодатель</button>
      </div>
      <form>
        <input
          v-model="email"
          class="default-input"
          type="email"
          placeholder="Адрес эл. почты"
          required
        />
        <input
          v-model="password"
          class="default-input"
          type="password"
          placeholder="Пароль"
          required
        />
        <button class="btn-submit" type="submit" @click="sendEmployer">
          Войти как работодатель
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  setup() {},
  data() {
    return {
      isActiveBtn: true,
      email: "",
      password: "",
    };
  },
  methods: {
    sendStudent(e) {
      e.preventDefault();
      axios
        .post("https://9021260458c0.ngrok.io/api/auth/jwt/create/", {
          email: this.email,
          password: this.password,
        })
        .then((response) => {
          let token = response.data.access;
          console.log(response);
          this.$router.push("/");
          if (response.status === 200) {
            localStorage.setItem("token", token);
            console.log(response.config.data, response);
            console.log("localStorage after set: ", localStorage);
          }
        });
      console.log("send Student", this.email);
    },
    sendEmployer() {
      console.log("send Employer", this.email);
    },
  },
};
</script>

<style lang="scss">
.auth-block {
  margin-top: 60px;
  display: flex;
  justify-content: center;
  .auth-block__reg {
    display: flex;
    flex-direction: column;
    form {
      display: flex;
      flex-direction: column;
    }
  }
}
.btns-block {
  margin-bottom: 25px;
  text-align: center;
}

.btn-submit {
  background-color: #1319ad;
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

.default-input {
  padding: 10px 18px;
  background-color: #f6f6f6;
  border: 1px solid black;
  margin-bottom: 18px;
}
</style>
