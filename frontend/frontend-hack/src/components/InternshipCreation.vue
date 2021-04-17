<template>
    <div class="container">
      <v-col class="links">
          <v-row class="header">
              <v-col cols="2">
                <router-link to="" class="link">
                    <v-icon
                    color="#000"
                    large
                    @click="next"
                    >
                        mdi-arrow-left
                    </v-icon>
                </router-link>
              </v-col>
              <v-col cols="6">
                <h3 class="title">Создание стажировки</h3>
              </v-col>
              <v-spacer></v-spacer>
          </v-row>
          <v-row>
              <v-col cols="12" >
                  <v-row class="input_field">
                        <v-text-field
                        label="Название организации"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Профессия"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Описание"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="competence">
                    <h3 class="title">Требуемые компетенции</h3>
                  </v-row>
                  <v-row>
                      <v-col cols="6">
                          <v-btn color="#1319AD" rounded class="btn">Добавить компетенцию</v-btn>
                      </v-col>
                      <v-spacer></v-spacer>
                  </v-row>
                  <v-row class="competence">
                    <h3 class="title">Срок стажировки</h3>
                  </v-row>
                  <v-row>
                      <v-col cols="6">
                          <v-text-field
                        label="Начало"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                      </v-col>
                      <v-col cols="6">
                          <v-text-field
                        label="Окончание"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                      </v-col>
                  </v-row>
                  <v-row>
                      <v-col cols="4">
                          <v-btn color="#1319AD" rounded class="btn">Сохранить</v-btn>
                      </v-col>
                      <v-spacer></v-spacer>
                  </v-row>
                
              </v-col>
          </v-row>
        
      </v-col>
    </div>
</template>

<script>
export default {
  data: () => ({
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
    }),
}
</script>

<style lang="scss" scoped>
.container{
  margin: 0 auto;
  width: 570px;
}

.link{
  text-decoration: none;
}

.header{
    margin-top: 5%;
}

.title{
    font-family: Montserrat;
    font-style: normal;
    font-weight: bold;
    font-size: 22px;
    line-height: 27px;
}

.competence{
    margin-top: 5%;
    margin-bottom: 3%;
}

.input_field{
    margin-bottom: 2%;
}

.btn{
    color: #fff;
    width: 100%;
}

</style>
