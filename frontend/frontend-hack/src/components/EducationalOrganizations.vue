<template>
    <div class="container">
        <v-col>
            <v-row>
                <v-col cols="7" class="title">
                    <h2 >Образовательные организации</h2>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="8">
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
                    min-height="55px"
                    class="btn">
                    Найти
                    </v-btn>                         
                </v-col>
                <v-col cols="2">
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12">
                    <OrganizationCard />
                </v-col>                
            </v-row>
            <div>
            <v-pagination
            v-model="page"
            :length="6"
            ></v-pagination>
        </div>
        </v-col>
    </div>
    
</template>

<script>
import OrganizationCard from './OrganizationCard.vue'
export default {
  name: 'EmployersList',
  components: {
    OrganizationCard
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

.text_field{
    border-radius: 10px;
}

.btn{
    color: #FFF;
    background-color: #1319AD;
    width: 100%;
}

</style>
