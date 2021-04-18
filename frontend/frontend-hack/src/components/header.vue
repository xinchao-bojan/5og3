<template>
  <header class="header">
    <v-app-bar app color="#fff" class="app_bar">
      <div class="app_container">
        <v-col>
          <v-row>
            <v-col cols="1">
              <router-link to="/" class="app_text"> Главная </router-link>
            </v-col>
            <v-col cols="3">
              <v-layout justify-center>
                <router-link to="/EmployersList" class="app_text">
                  Рейтинг работодателей
                </router-link>
              </v-layout>
            </v-col>
            <v-col cols="3">
              <router-link class="app_text" to="/EducationalOrganization">
                <p class="app_text">Образовательные организации</p>
              </router-link>
            </v-col>
            <v-spacer> </v-spacer>
            <v-col cols="2" justify-end v-if="!isLoggedIn">
              <v-layout justify-end>
                <router-link to="/registration" class="app_text">
                  <p class="app_text">Зарегистрироваться</p>
                </router-link>
              </v-layout>
            </v-col>
            <v-col cols="1" class="vhod" v-if="!isLoggedIn">
              <div class="span"></div>
              <v-layout justify-end>
                <router-link to="/login" class="app_text">
                  <p class="app_text">Войти</p>
                </router-link>
              </v-layout>
            </v-col>
            <v-col cols="1" class="vhod" v-if="isLoggedIn">
              <v-layout justify-end>
                <router-link to="/profile" class="app_text">
                  <p class="app_text">
                    <img src="@/assets/icon_acc.svg" alt="" />
                  </p>
                </router-link>
              </v-layout>
            </v-col>
            <v-col cols="1" class="vhod" v-if="isLoggedIn">
              <v-layout justify-end>
                <router-link to="/">
                  <a class="nav-link" @click="logout">
                    <img src="@/assets/icon_logout.svg" alt="" />
                  </a>
                </router-link>
              </v-layout>
            </v-col>
          </v-row>
        </v-col>
      </div>
    </v-app-bar>
  </header>
</template>

<script>
export default {
  setup() {},
  computed: {
    isLoggedIn: function () {
      console.log("Hello from computed isLoggedIn");
      console.log(
        "Значение isAuthenticated",
        this.$store.getters.isAuthenticated
      );
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    logout: function () {
      console.log("jopasdjasi");
      this.$store.dispatch("LOGOUT").then(() => {
        console.log("Вы вышли из системы");
        this.$router.push("/Authorization").catch(() => {});
      });
    },
  },
};
</script>

<style lang="scss" scoped>
header {
  max-width: 100%;
  flex: 0 0 auto;
}

.app_bar {
  height: 64px;
}

.app_container {
  margin: 0 auto;
  width: 1170px;
}

.app_text {
  color: #000;
  font-family: Roboto;
  text-decoration: none;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 21px;
  margin: 0;
  &:hover {
    color: #1319ad;
  }
  &:focus {
    color: #0d1289;
  }
}

.vhod {
  display: inline-flex;
}

.span {
  width: 2px;
  height: 100%;
  background-color: #000;
}
</style>
