<template>
  <v-col>
    <v-row class="bg_color">
      <div class="container">
        
          <v-col cols="6">
            <v-row>
              <h1 class="title1">Добро пожаловать в сервис для поиска стажировок</h1>
            </v-row>
            <v-row>
              <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Platea massa elementum odio in pellentesque in. Quisque fermentum egestas egestas egestas magna commodo aenean ultricies.</p>
            </v-row>
            <v-row>
              <v-col cols="6">
                <v-btn
                rounded
                color="#BF1A42"
                class="btn"
                width="100%">
                  Хочу стажироваться
                </v-btn>
              </v-col>
              <v-col cols="6">
                <v-btn
                rounded
                color="#fff"
                outlined
                class="btn"
                width="100%">
                  Я работодатель
                </v-btn>
              </v-col>         
            </v-row>
          </v-col>
          
      </div>
      <v-col cols="6">
        <img src="./pic.png" class="photo">
      </v-col> 
    </v-row>
    <div class="container">
      <v-row class="section2">
        <v-col cols="5">
          <h2 class="title2">Лучшие работодатели</h2>
        </v-col> 
        <v-spacer></v-spacer>
        <v-col cols="1" >
          <v-layout justify-end>
            <router-link to="/EmployersList" class="link">
              <v-icon
                color="#000"
                large
                @click="next"
              >
                mdi-arrow-right
              </v-icon>
            </router-link>
          </v-layout>
        </v-col>     
      </v-row>
      <v-row>
        <EmployerCard />
      </v-row>
      <v-row class="section2">
        <v-col cols="6">
          <h2 class="title2">Образовательные организации</h2>
        </v-col> 
        <v-spacer></v-spacer>
        <v-col cols="1" >
          <v-layout justify-end>
            <v-icon
            color="#000"
              large
              @click="next"
            >
              mdi-arrow-right
            </v-icon>
            </v-layout>
        </v-col>     
      </v-row>
      <v-row>
        <OrganizationCard />
      </v-row>
      <v-row class="section2">
        <v-col cols="6">
          <h2 class="title2">Рекомендуемые стажировки</h2>
        </v-col> 
        <v-spacer></v-spacer>
        <v-col cols="1" >
          <v-layout justify-end>
            <v-icon
            color="#000"
              large
              @click="next"
            >
              mdi-arrow-right
            </v-icon>
            </v-layout>
        </v-col>     
      </v-row>
      <v-row>
        <v-col>
          <InternshipCard />
        </v-col>
      </v-row>
    </div>
  </v-col>
</template>

<script>
import EmployerCard from './EmployerCard'
import InternshipCard from './InternshipCard.vue'
import OrganizationCard from './OrganizationCard'

export default {
  name: 'Home',
  components: {
    EmployerCard,
    OrganizationCard,
    InternshipCard
  },
  methods: {
    next () {
        
    },
  },
}
</script>

<style lang="scss" scoped>
.bg_color{
  background-color: #1319AD;
  justify-content: space-between;;
}

.container{
  margin: 0 auto;
  width: 1170px;
}

.title1{
  font-family: Montserrat;
  font-style: normal;
  font-weight: bold;
  font-size: 50px;
  line-height: 61px;
  color: #fff;
}

.description{
  font-family: Montserrat;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 29px;
  margin-top: 10%;
  color: #fff;
}

.btn{
  color: #fff;
  &:hover{
    background: linear-gradient(to right, #9d1737 0%, #bf1a42 100%);
    border:none;
  }
  &:focus{
    background: #9D1737;
  }
}

.btn2{
  color: #fff;
}

.photo{
  width: 600px;
  transform: -50% ;
}

.section2{
  margin-top: 9%;
}

.title2{
  font-family: Montserrat;
  font-style: normal;
  font-weight: bold;
  font-size: 30px;
  line-height: 37px;
  margin-bottom: 5%;
}

.link{
  text-decoration: none;
}
</style>
