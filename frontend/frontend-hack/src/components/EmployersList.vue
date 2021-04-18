<template>
    <div class="container">
        <v-col>
            <v-row>
                <v-col cols="5" class="title">
                    <h2 >Рейтинг работодателей</h2>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <EmployerBigCard />
                </v-col>
                
            </v-row>
        </v-col>
    </div>
    
</template>

<script>
import EmployerBigCard from './EmployerBigCard.vue'
export default {
  name: 'EmployersList',
  components: {
    EmployerBigCard
  }
}
</script>

<style lang="scss" scoped>
.container{
    margin: 0 auto;
    width: 1170px;
}

.title{
    font-family: 'Montserrat', sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 30px;
    line-height: 37px;
    color: #000;
    margin-top: 5%;
}

</style>
