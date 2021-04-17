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
                        v-model="searchValue"
                        label="Поиск"
                        outlined
                        class="text_field"                      
                    ></v-text-field>
                </v-col>
                <v-col cols="2">
                    <v-btn
                    @click="searchStudent"
                    outlined
                    rounded
                    min-height="55px"
                    class="btn"
                    >
                    Найти
                    </v-btn>                         
                </v-col>                        
                 
                <v-col cols="2">
                    
                </v-col> 
                <v-spacer></v-spacer>               
            </v-row>
            <v-row>
                <p>{{searchValue}}</p>
                <ul>
                    <li v-for="st in this.searchStudent" :key="st.id">
                        <p>{{st.name}}</p>
                    </li>
                </ul>
            </v-row>
            <v-row>
                <StudentCard />
            </v-row>
        </v-col>
        <div>
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
        searchValue:'',
        student:[
            {
                id: 1,
                name: "Katya",
                skills: ["c++", "java", "react", "html"]
            },
            {
                id: 2,
                name: "Vanya",
                skills: ["c++", "java", "vue", "html", "git"]
            },
            {
                id: 3,
                name: "Kostya",
                skills: ["c++", "java", "pyton", "django"]
            },
            {
                id: 4,
                name: "Max",
                skills: ["c++", "java", "pyton", "figma"]
            },
            {
                id: 5,
                name: "Roma",
                skills: ["java", "react", "html", "figma", "c#", "c"]
            },
            {
                id: 6,
                name: "Alica",
                skills: ["c"]
            },
            {
                id: 7,
                name: "GeyOrgiy",
                skills: ["dog", "cat", "drink"]
            },
            {
                id: 8,
                name: "Дима",
                skills: ["c++", "pyton"]
            },
            {
                id: 9,
                name: "Olga",
                skills: ["time-managment"]
            },
            {
                id: 10,
                name: "Serega",
                skills: ["c++", "java"]
            },
        ]        
    }
  },
  computed:{
      searchStudent(){
          return this.student.filter(el =>{
              return el.name.toLowerCase().includes(this.searchValue.toLowerCase())
          })
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

.btn{
    color: #FFF;
    background-color: #1319AD;
    width: 100%;
}
</style>
