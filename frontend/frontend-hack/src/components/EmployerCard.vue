<template>
    <v-col>
        <v-row>
            <v-col cols="6">
                <v-card outlined class="card">
                <v-col>
                    <v-row>
                        <v-col cols="6" class="colp">
                            <h3 class="card_title">Mail.ru Group</h3>
                        </v-col>
                        <v-spacer></v-spacer>
                        <v-col>
                            <v-layout justify-end>
                                <p class="rating">9.1</p>
                            </v-layout>
                        </v-col>
                    
                    </v-row>
                    <v-row>
                    <p class="card_text">Mail.ru Group — это команда профессионалов в самых разных областях, объединенных общей целью — создание и совершенствование реалий повседневной жизни современного человека.</p>
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
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card outlined class="card">
                <v-col>
                    <v-row>
                        <v-col cols="6" class="colp">
                            <h3 class="card_title">Яндекс</h3>
                        </v-col>
                        <v-spacer></v-spacer>
                        <v-col>
                            <v-layout justify-end>
                                <p class="rating">9.0</p>
                            </v-layout>
                        </v-col>
                    
                    </v-row>
                    <v-row>
                    <p class="card_text">Я́ндекс» — российская транснациональная компания в отрасли информационных технологий, чьё головное юридическое лицо зарегистрировано в Нидерландах, владеющая одноимённой системой поиска в интернете</p>
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
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
                <v-card outlined class="card">
                <v-col>
                    <v-row>
                        <v-col cols="6" class="colp">
                            <h3 class="card_title">Сбербанк</h3>
                        </v-col>
                        <v-spacer></v-spacer>
                        <v-col>
                            <v-layout justify-end>
                                <p class="rating">8.6</p>
                            </v-layout>
                        </v-col>
                    
                    </v-row>
                    <v-row>
                    <p class="card_text">ПАО «Сбербанк» — российский финансовый конгломерат, крупнейший транснациональный и универсальный банк России, Центральной и Восточной Европы. По итогам 2019 года у «Сбербанка» 96,2 млн активных частных клиентов...</p>
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
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card outlined class="card">
                <v-col>
                    <v-row>
                        <v-col cols="6" class="colp">
                            <h3 class="card_title">РосЭнерго</h3>
                        </v-col>
                        <v-spacer></v-spacer>
                        <v-col>
                            <v-layout justify-end>
                                <p class="rating">8.9</p>
                            </v-layout>
                        </v-col>
                    
                    </v-row>
                    <v-row>
                    <p class="card_text">Компания ООО «НСГ – «РОСЭНЕРГО» является участником холдинга «РОСЭНЕРГО», который представляет собой многопрофильную бизнес-структуру, объединяющую страховой, туристический и агробизнес, который участвует...</p>
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
                </v-card>
            </v-col>
        </v-row>
        <v-row>
           
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
  padding: 15px;
}

.colp{
    padding-left: 0;
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