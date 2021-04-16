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
      
    </v-row>
  </v-col>
</template>

<script>

export default {
  name: 'Home',
  components: {
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
