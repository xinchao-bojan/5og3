<template>
  <footer class="footer">
    <div class="container">
      <v-col class="links">
        <v-row>
          <v-col cols="3">
            <v-row>
              <p class="text">Студентам</p>
            </v-row>
            <v-row>
              <p class="text">Амбассадоры</p>
            </v-row>
          </v-col>
          <v-col cols="3">
            <v-row>
              <p class="text">Работодателям</p>
            </v-row>
            <v-row>
              <p class="text">Связаться с нами</p>
            </v-row>
          </v-col>
          <v-col cols="3">
            <v-row>
              <p class="text">Преподавателям</p>
            </v-row>
            <v-row>
              <p class="text">Пресс-центр</p>
            </v-row>
          </v-col>
          <v-col cols="3">
            <v-row>
              <v-col cols="3">
                <v-icon
                color="#000"
                  large
                  @click="next"
                >
                  mdi-instagram
                </v-icon>
              </v-col>
              <v-col cols="3">
                <v-icon
                color="#000"
                  large
                  @click="next"
                >
                  mdi-twitter
                </v-icon>
              </v-col>
              <v-col cols="3">
                <v-icon
                color="#000"
                  large
                  @click="next"
                >
                  mdi-facebook
                </v-icon>
              </v-col>
              <v-col cols="3">
                <v-icon
                color="#000"
                  large
                  @click="next"
                >
                  mdi-vk
                </v-icon>
              </v-col>

            </v-row>

          </v-col>
        </v-row>
      </v-col>
    </div>
    <div class="footer_bottom">
      <div class="container">
        <v-col>
          <v-row>
            <v-col cols="3" class="copyright"> 
                <p class="footer_text">Copyright © BustUP , 2021</p>
              <v-layout justify-end>
                <div class="span"></div>
              </v-layout>
            </v-col>
            <v-col cols="3">
              <p class="footer_text">Политика конфиденциальности</p>
            </v-col>
          </v-row>
        </v-col>

      </div>

    </div>
  </footer>
</template>

<script>
export default {
  setup () {

  },
  methods: {
    next () {
        
    },
  },
}
</script>

<style lang="scss" scoped>
.footer{
  border-top: 1px solid #000000;
}

.container{
  margin: 0 auto;
  width: 1170px;
}

.links{
  padding-top: 5%;
  padding-bottom: 5%;
}

.text{
  font-family: Montserrat;
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 20px;
}

.footer_bottom{
  background-color: #1319AD;
}

.copyright{
  display: inline-flex;
}

.footer_text{
  font-family: Montserrat;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 17px;
  color: #fff;
  margin: 0;
}

.span{
  width: 2px;
  height: 100%;
  background-color: #fff;
}
</style>
