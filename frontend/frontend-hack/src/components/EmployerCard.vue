<template>
    <v-col>
        <v-row>
            <v-col cols="6">
                <v-card elevation="4" class="card">
                <v-col>
                    <v-row>
                    <p class="card_title">Mail.ru Group</p>
                    </v-row>
                    <v-row>
                    <p class="card_text">Mail.ru Group — это команда профессионалов в самых разных областях, объединенных общей целью — создание и совершенствование реалий повседневной жизни современного человека.</p>
                    </v-row>
                    <v-row>
                    <v-col cols="6">
                        <v-btn
                        color="#000"
                        elevation="2"
                        outlined
                        >Перейти к компаннии</v-btn>
                    </v-col>
                    <v-spacer cols="4">

                    </v-spacer>
                    <v-col cols="2">
                        <p>9.1</p>
                    </v-col>
                    </v-row>
                </v-col>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card elevation="4" class="card">
                <v-col>
                    <v-row>
                    <p class="card_title">Яндекс</p>
                    </v-row>
                    <v-row>
                    <p class="card_text">«Яндекс» — российская транснациональная компания в отрасли информационных технологий, чьё головное юридическое лицо зарегистрировано в Нидерландах, владеющая одноимённой системой поиска в интернете, интернет-порталом и веб-слу...</p>
                    </v-row>
                    <v-row>
                    <v-col cols="6">
                        <v-btn
                        color="#000"
                        elevation="2"
                        outlined
                        >Перейти к компаннии</v-btn>
                    </v-col>
                    <v-spacer cols="4">

                    </v-spacer>
                    <v-col cols="2">
                        <p>9.0</p>
                    </v-col>
                    </v-row>
                </v-col>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
                <v-card elevation="4" class="card">
                <v-col>
                    <v-row>
                    <p class="card_title">РосЭнерго</p>
                    </v-row>
                    <v-row>
                    <p class="card_text">Компания ООО «НСГ – «РОСЭНЕРГО» является участником холдинга «РОСЭНЕРГО», который представляет собой многопрофильную бизнес-структуру, объединяющую страховой, туристический и агробизнес, который участвует собственными средствам...</p>
                    </v-row>
                    <v-row>
                    <v-col cols="6">
                        <v-btn
                        color="#000"
                        elevation="2"
                        outlined
                        >Перейти к компаннии</v-btn>
                    </v-col>
                    <v-spacer cols="4">

                    </v-spacer>
                    <v-col cols="2">
                        <p>8.9</p>
                    </v-col>
                    </v-row>
                </v-col>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card elevation="4" class="card">
                <v-col>
                    <v-row>
                    <p class="card_title">Сбербанк</p>
                    </v-row>
                    <v-row>
                    <p class="card_text">ПАО «Сбербанк» — российский финансовый конгломерат, крупнейший транснациональный и универсальный банк России, Центральной и Восточной Европы. По итогам 2019 года у «Сбербанка» 96,2 млн активных частных клиентов и 2,6 млн...</p>
                    </v-row>
                    <v-row>
                    <v-col cols="6">
                        <v-btn
                        color="#000"
                        elevation="2"
                        outlined
                        >Перейти к компаннии</v-btn>
                    </v-col>
                    <v-spacer cols="4">
                    </v-spacer>
                    <v-col cols="2">
                        <p>8.6</p>
                    </v-col>
                    </v-row>
                </v-col>
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
  padding: 10px;
}

.card_title{
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  line-height: 21px;
  padding-left: 15px;
}

.card_text{
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 19px;
}

</style>