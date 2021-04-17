<template>
    <v-col>
        <v-row>
            <v-col cols="12">
                <v-card outlined class="card">
                    <v-row>
                        <v-col cols="4">
                            <v-row class="colp">
                                <v-col cols="9">
                                    <h3 class="card_title">ОАО Роснефть</h3> 
                                </v-col>
                                <v-spacer>

                                </v-spacer>
                                <v-col>
                                    <v-layout justify-end>
                                        <p class="rating">9.1</p>
                                    </v-layout>
                                </v-col>                                                   
                            </v-row>
                            <v-row>
                                <p class="internship_name">Профессия: VR/AR разработчик</p>
                            </v-row>
                            <v-row>
                            <p class="card_text">Разработка обучающего ПО в виртуальной реальности для обучения.</p>
                            </v-row>
                        </v-col>
                        <v-col cols="4">
                            <v-row class="colp">
                                <v-col cols="9">
                                    <h3 class="card_title2">Требуемые навыки</h3> 
                                </v-col>                                                
                            </v-row>
                            <v-row>
                                <p class="skill">Java</p>
                                <p class="skill">Разработка приложений VR</p>
                                <p class="skill">C#</p>
                                <p class="skill">Машинное обучение</p>
                            </v-row>
                        </v-col>
                        <v-col cols="4">
                            <v-row class="colp">
                                <v-col cols="9" class="colp">
                                    <h3 class="card_title2">Срок стажировки</h3> 
                                </v-col>                                                
                            </v-row>
                            <v-row>
                                <p class="card_text">От 3 до 6 месяцев</p>
                            </v-row>
                            <v-row>
                                <v-col cols="6" class="colp">
                                    <v-btn
                                    color="#1319AD"
                                    outlined
                                    rounded
                                    class="btn_text"
                                    >Подробнее</v-btn>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>            
        </v-row>        
    </v-col>
</template>


<script>

export default {
  name: 'InternshipCard',
  components: {
  }
}
</script>

<style lang="scss" scoped>

.card{
    border: 1px solid #000000;
    padding: 25px;
}

.colp{
    padding-left: 0;
    padding-bottom: 4%;
}

.card_title{
    font-family: Montserrat;
    font-style: normal;
    font-weight: bold;
    font-size: 22px;
    line-height: 27px;
    color: #1319AD;
}

.rating{
    color: #06A53C;
    font-family: Montserrat;
    font-style: normal;
    font-weight: bold;
    font-size: 22px;
    line-height: 27px;
}

.internship_name{
    font-family: Montserrat;
    font-style: normal;
    font-weight: bold;
    font-size: 18px;
    line-height: 22px;
}

.card_text{
   font-family: Montserrat;
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    line-height: 20px;
    color: #000;
}

.card_title2{
    font-family: Montserrat;
    font-style: normal;
    font-weight: bold;
    font-size: 22px;
    line-height: 27px;
    color: #000;
}

.v-btn__content{
    font-family: Montserrat;
    font-style: normal;
    font-weight: bold;
    font-size: 18px;
    line-height: 22px;
}

.skill{
    font-family: Montserrat;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 17px;
    background: #E8E8F7;
    border: 1px solid #000000;
    box-sizing: border-box;
    border-radius: 50px;
    padding: 8px;
    margin-right: 5px;
}
</style>