<template>
  <div class="container">
    <v-col>
      <v-row>
        <v-col cols="5" class="title">
          <h2>Поиск студентов</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="5">
          <v-text-field
            v-model="message"
            label="Поиск"
            outlined
            class="text_field"
          ></v-text-field>
        </v-col>
        <v-col cols="2" class="btn_cont">
          <v-btn @click="searchStudent(message)" outlined rounded class="btn">
            Найти
          </v-btn>
        </v-col>

        <v-col cols="2"> </v-col>
        <v-spacer></v-spacer>
      </v-row>
      <StudentCard
        v-for="item in this.STUDENTS.results"
        :key="item.id"
        :student_data="item"
      />
    </v-col>
    <div class="text-center">
      <v-pagination v-model="page" :length="6"></v-pagination>
    </div>
  </div>
</template>

<script>
import StudentCard from "./StudentCard.vue";

import { mapActions, mapGetters } from "vuex";
export default {
  name: "StudentSearchPage",
  components: {
    StudentCard,
  },
  data() {
    return {
      page: 1,
      searchInput: "",
      sortedList: [],
    };
  },
  methods: {
    ...mapActions(["GET_STUDENTS_FROM_API", "GET_SEARCH_VALUE_TO_VUEX"]),
    searchStudent(value) {
      console.log(value);
      this.GET_SEARCH_VALUE_TO_VUEX(value);
    },
    sortByComps(students){
      console.log("hello from sortByCategory students: ", students)
        
    }
  },
  computed: {
    ...mapGetters(["STUDENTS", "SEARCH_VALUE"]),
  },
  watch: {
    STUDENTS() {
      console.log(
        "WATCHER STUDENTS WATCHER STORE STATE",
        JSON.parse(JSON.stringify(this.$store.state.students))
      );
    },
  },
  mounted() {
    this.GET_STUDENTS_FROM_API();
    console.log(
      "THIS STORE STATE",
      JSON.parse(JSON.stringify(this.$store.state.employers))[0]
    );
    console.log(
      "AAAAAAAAAAAAAAAAAAAAAAAAAA",
      JSON.parse(JSON.stringify(this.$store.state))
    );
  },
};
</script>

<style lang="scss" scoped>
.container {
  margin: 0 auto;
  max-width: 970px;
}

.title {
  font-family: "Montserrat", sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 30px;
  line-height: 37px;
  color: #000;
  margin-top: 5%;
}

.text_field {
  border-radius: 10px;
}

.btn_cont {
  margin-top: 9px;
}

.btn {
  color: #fff;
  background-color: #1319ad;
  width: 100%;
}
</style>
