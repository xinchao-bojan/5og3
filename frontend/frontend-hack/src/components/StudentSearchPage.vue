<template>
    <div class="container">
        <v-col>
            <v-row>
                <v-col cols="5" class="title">
                    <h2 >Поиск студентов</h2>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                </v-col>
                <v-col>
                </v-col>
                <v-col>
                </v-col>                
            </v-row>
            <v-row>
                <StudentCard />
            </v-row>
        </v-col>
    </div>    
</template>

<script>
import StudentCard from './StudentCard.vue'
export default {
  name: 'StudentSearchPage',
  components: {
    StudentCard
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