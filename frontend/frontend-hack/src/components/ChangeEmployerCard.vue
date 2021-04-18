<template>
    <div class="container">
      <v-col class="links">
          <v-row class="header">
              <v-spacer></v-spacer>
              <v-col cols="1">
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
              <v-col cols="5">
                <h3 class="title">Редактирование профиля</h3>
              </v-col>
              <v-spacer></v-spacer>
          </v-row>
          <v-row>
              <v-col cols="12" sm="3">
                    <div class="avatar">
                        <h5>Место для фото</h5>
                    </div>                    
                    <v-btn color="#1319AD" rounded class="btn">Изменить фото</v-btn>                                       
              </v-col>
              <v-col cols="9" >
                  <v-row class="input_field">
                        <v-text-field
                        label="Почта"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Фамилия"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Имя"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Отчество"
                        :rules1="rules1"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Пол"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Дата рождения"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Компания"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row class="input_field">
                        <v-text-field
                        label="Должность"
                        :rules="rules"
                        hide-details="auto"
                        outlined
                        ></v-text-field>
                  </v-row>
                  <v-row>
                      <v-spacer></v-spacer>
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
      rules1: [
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
    }),
}
</script>

<style lang="scss" scoped>
.container{
  margin: 0 auto;
  width: 770px;
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

.avatar{
    margin-bottom: 10%;
}

.input_field{
    margin-bottom: 2%;
}

.btn{
    color: #fff;
    width: 100%;
}

</style>
