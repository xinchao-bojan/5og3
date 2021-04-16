<template>
  <header class="header">
      <div class="container">
  <v-app >
    <v-app-bar
      app
      color="#2C4EFF"
      class="app_bar"
      
    >
    <div class="app_container">
      <v-col>
        <v-row>
          <v-col cols="1">
            <router-link to="/">
              <p class="app_text">Главная</p>
            </router-link>
          </v-col>
          <v-col cols="2-3">
            <router-link to="/EmployersList ">
              <p class="app_text">Список работотдателей</p>
            </router-link>
          </v-col>
          <v-col cols="4">
            <p class="app_text">Образовательные организации</p>
          </v-col>
          <v-spacer>

          </v-spacer>
          <v-col cols="11-12" justify-end>
            <v-layout justify-end>
              <p class="app_text">Профиль</p>
            </v-layout>
            
          </v-col>          
      </v-row>
    </v-col>
    </div>
    
    </v-app-bar>

      <v-main>
        <router-view>
        </router-view>
      </v-main>

      </v-app>
    </div>
  </header>
</template>

<script>
export default {
  setup () {

  }
}
</script>

<style lang="scss" scoped>
header {
  max-width: 100%;
  flex: 0 0 auto;
}

.container{
  margin: 0 auto;
  width: 1170px;
}

.app_bar{
  height: 64px;
}

.app_container{
  margin: 0 auto;
  width: 1170px;
}

.app_text{
  color: rgb(255, 255, 255);
  font-family: Roboto;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 21px;
  margin: 0;
}
</style>
