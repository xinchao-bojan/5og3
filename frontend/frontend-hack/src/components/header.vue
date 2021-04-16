<template>
  <header class="header">
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
                    <p class="app_text">Рейтинг работодателей</p>
                  </router-link>
                </v-col>
                <v-col cols="4">
                  <p class="app_text">Образовательные организации</p>
                </v-col>
                <v-spacer>

                </v-spacer>
                <v-col cols="11-12" justify-end>
                  <v-layout justify-end>
                    <router-link to="/login" class="app_text">Профиль</router-link>
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
  setup () {

  }
}
</script>

<style lang="scss" scoped>
header {
  max-width: 100%;
  flex: 0 0 auto;
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
  text-decoration: none;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 21px;
  margin: 0;
}
</style>
