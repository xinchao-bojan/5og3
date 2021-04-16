<template>
  <v-col>
    <v-row>
      <v-col cols="4">
        <h2 class="title">Лучшие работодатели</h2>
      </v-col>
      <v-spacer>

      </v-spacer>
      <v-col cols="3">
        <v-btn color="#C4C4C4" elevation="2" width="100%">
          Предлагаю стажировку
        </v-btn>
      </v-col>
      <v-col cols="3">
        <v-btn color="#C4C4C4" elevation="2" width="100%">
          Ищу стажировку
        </v-btn>
      </v-col>
      
    </v-row>
    <v-row>
      <EmployerCard />
      
      
    </v-row>
  </v-col>
</template>

<script>
import EmployerCard from './EmployerCard'

export default {
  name: 'Home',
  components: {
    EmployerCard
  }
}
</script>

<style lang="scss" scoped>
.title{
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 28px;
  line-height: 33px;
}
</style>
