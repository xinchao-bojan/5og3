<template>
  <v-col>
    <v-row>
      <v-col cols="12">
        <v-card outlined class="card">
          <v-row>
            <v-col cols="6">
              <v-row class="colp">
                <v-col class="title_style">
                  <h3 class="card_title">
                    {{ student_data.user.user.first_name }}
                    {{ student_data.user.user.last_name }}
                  </h3>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="4">
                  <v-row>
                    <p class="heading">ВУЗ</p>
                  </v-row>
                  <v-row>
                    <p class="heading">Направление</p>
                  </v-row>
                </v-col>
                <v-col cols="4">
                  <v-row>
                    <p class="text_value">
                      {{ student_data.ed_organization.name }}
                    </p>
                  </v-row>
                  <v-row>
                    <p class="text_value">
                      Информатика и вычислительная техника
                    </p>
                  </v-row>
                </v-col>
              </v-row>
              <v-row class="buttons">
                <v-col cols="4" class="colp">
                  <v-btn color="#1319AD" outlined rounded class="btn_text"
                    >Профиль</v-btn
                  >
                </v-col>
                <v-col cols="4" class="colp">
                  <v-btn color="#1319AD" outlined rounded class="btn_text"
                    >Связаться</v-btn
                  >
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="6">
              <v-row class="colp">
                <v-col class="title_style">
                  <h3 class="card_title">Навыки</h3>
                </v-col>
              </v-row>
              <v-row>
                <p class="skill">{{ student_data.ed_competence[0].name }}</p>
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
  name: "StudentCard",
  components: {},
  props: {
    student_data: {
      type: Object,
      default() {
        return {};
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.card {
  border: 1px solid #202020;
  padding: 25px;
  border-radius: 10px;
  position: relative;
}

.colp {
  padding-left: 0;
  padding-bottom: 4%;
}

.title_style {
  padding-left: 0;
}

.card_title {
  font-family: Montserrat;
  font-style: normal;
  font-weight: bold;
  font-size: 22px;
  line-height: 27px;
  color: #1319ad;
}

.heading {
  font-family: Montserrat;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 22px;
}

.text_value {
  font-family: Montserrat;
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 20px;
}

.skill {
  font-family: Montserrat;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 17px;
  background: #e8e8f7;
  border: 1px solid #000000;
  box-sizing: border-box;
  border-radius: 50px;
  padding: 8px;
  margin-right: 3px;
}

.buttons {
  margin-top: 25px;
}

.v-btn__content {
  font-family: Montserrat;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 22px;
}

.bloks_inline {
  display: inline-flex;
}

.span {
  width: 1px;
  height: 100%;
  background-color: rgba(32, 32, 32, 0.5);
}

.btn_text {
  position: absolute;
  bottom: 0;
  margin-bottom: 2%;
}
</style>