<template>
    <v-col>
        <v-row>
            <v-col cols="12">
                <v-card outlined class="card">
                    <v-row>
                        <v-col cols="8">
                            <v-row class="colp">
                                <h3 class="card_title">РТУ МИРЭА</h3>                    
                            </v-row>
                            <v-row>
                            <p class="card_text">Признанный в России и в мире современный образовательный и научно-исследовательский центр, сочетающий в своей работе классические университетские традиции и современные образовательные технологии.</p>
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
                        <v-col cols="4">
                            <img src="./mirea_photo.png" class="photo">
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
            
        </v-row>
        <v-row>
           <v-col cols="12">
                <v-card outlined class="card">
                    <v-row>
                        <v-col cols="8">
                            <v-row class="colp">
                                <h3 class="card_title">МГТУ им. Баумана</h3>                    
                            </v-row>
                            <v-row>
                            <p class="card_text">Российский национальный исследовательский университет, научный центр, особо ценный объект культурного наследия народов России. В 2008 году он получил награду «Европейское качество» «за стремление достичь высокого качества образовательных услуг в соответствии с международными стандартами»</p>
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
                        <v-col cols="4">
                            <img src="./baumanka_photo.png" class="photo">
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
           <v-col cols="12">
                <v-card outlined class="card">
                    <v-row>
                        <v-col cols="8">
                            <v-row class="colp">
                                <h3 class="card_title">Горный университет</h3>                    
                            </v-row>
                            <v-row>
                            <p class="card_text">Один из крупнейших вузов по горному делу и первое высшее техническое учебное заведение России. Входит в категорию Национальный исследовательский университет России (2009).</p>
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
                        <v-col cols="4">
                            <img src="./gornyy_photo.png" class="photo">
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
           <v-col cols="12">
                <v-card outlined class="card">
                    <v-row>
                        <v-col cols="8">
                            <v-row class="colp">
                                <h3 class="card_title">Высшая школа экономики</h3>                    
                            </v-row>
                            <v-row>
                            <p class="card_text">Сотрудники вуза участвовали в создании стратегий развития страны, в модернизации образования и здравоохранения, реформе государственной службы, работали над программой «Электронная Россия» и многих других проектах</p>
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
                        <v-col cols="4">
                            <img src="./vyshka_photo.png" class="photo">
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </v-col>
</template>


<script>

export default {
  name: 'EmployerCard',
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
    font-size: 30px;
    line-height: 37px;
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

.card_text{
    font-family: Montserrat;
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    line-height: 20px;
    color: #202020;
}

.v-btn__content{
    font-family: Montserrat;
    font-style: normal;
    font-weight: bold;
    font-size: 18px;
    line-height: 22px;
}

</style>