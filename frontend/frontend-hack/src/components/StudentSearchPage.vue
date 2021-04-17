<template>
    <div class="container">
        <v-col>
            <v-row>
                <v-col cols="5" class="title">
                    <h2 >Поиск студентов</h2>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="5">
                    <v-text-field
                        v-model="message4"
                        label="Поиск"
                        outlined
                        class="text_field"                        
                    ></v-text-field>
                </v-col>
                <v-col cols="2" class="btn_cont">
                    <v-btn
                    outlined
                    rounded
                    class="btn">
                    Найти
                    </v-btn>                         
                </v-col>                        
                 
                <v-col cols="2">
                    
                </v-col> 
                <v-spacer></v-spacer>               
            </v-row>
            <v-row>
                <StudentCard />
            </v-row>
        </v-col>
        <div class="text-center">
            <v-pagination
            v-model="page"
            :length="6"
            ></v-pagination>
        </div>
    </div>    
</template>

<script>
import StudentCard from './StudentCard.vue'
export default {
  name: 'StudentSearchPage',
  components: {
    StudentCard
  },
  data () {
    return {
        page: 1,
    }
  }
    
}
</script>

<style lang="scss" scoped>

.container{
  margin: 0 auto;
  max-width: 970px;
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

.text_field{
    border-radius: 10px;
}

.btn_cont{
    margin-top: 9px;
}

.btn{
    color: #FFF;
    background-color: #1319AD;
    width: 100%;
}
</style>
