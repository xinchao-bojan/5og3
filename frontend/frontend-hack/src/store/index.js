import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axios from 'axios'
export default new Vuex.Store({
  state: {
    employers: [],
    token: localStorage.getItem('token') || '',
    searchValue: '',
    students: [],
  },
  mutations: {
    SET_EMPLOYERS_TO_STATE: (state, employers) => {
      console.log("Hello from store.js SET_EMPLOYERS_TO_STATE", employers)
      state.employers = employers
      console.log("state", state.employers);
    },
    SET_STUDENT_TO_STATE: (state, students) => {
      console.log("Hello from store.js SET_STUDENTS_TO_STATE", students)
      state.students = students
      console.log("state students", state.students);
    },
    LOGOUT(state) {
      console.log("Hello from store.js LOGOUT")
      state.token = ''
    },
    SET_SEARCH_VALUE_TO_VUEX: (state, value) => {
      console.log("before SET_SEARCH_VALUE_TO_VUEX", state.searchValue)
      state.searchValue = value;
      console.log("after SET_SEARCH_VALUE_TO_VUEX", state.searchValue)
  },
  },
  actions: {
    GET_EMPLOYERS_FROM_API({ commit }) {
      console.log("Hello from GET_EMPLOYERS_FROM_API")
      console.log("token: ", localStorage.getItem('token'));
      return axios
        .request({
          url: "https://656873ee46cf.ngrok.io/api/listallinternship/",
          method: "GET",
          headers: {
            Authorization: "Bearer " + localStorage.getItem('token'),
          },
          data: {
            sex: this.sex,
            date: this.dateborn,
            ed_organization: this.institut,
          },
        }).then((employers) => {
          console.log("employers.data.results", employers.data.results[0].id);
          console.log("employers: ", employers);
          commit('SET_EMPLOYERS_TO_STATE', employers.data);
          console.log("commit articles", employers.data);
          return employers;
        }).catch(function (error) {
          console.error(error.response);
        });
    },
    GET_STUDENTS_FROM_API({ commit }) {
      console.log("Hello from GET_STUDENT_FROM_API")
      return axios
        .request({
          url: "https://656873ee46cf.ngrok.io/api/list/students/",
          method: "GET",
          headers: {
            Authorization: "Bearer " + localStorage.getItem('token'),
          }
        }).then((students) => {
          console.log("students.data.results", students.data.results[0].id);
          console.log("students: ", students);
          commit('SET_STUDENT_TO_STATE', students.data);
          console.log("commit articles", students.data);
          return students;
        }).catch(function (error) {
          console.error(error.response);
        });
    },
    GET_SEARCH_VALUE_TO_VUEX({ commit }, value) {
      commit('SET_SEARCH_VALUE_TO_VUEX', value)
    },
    LOGOUT({ commit }) {
      return new Promise((resolve) => {
        commit('LOGOUT')
        console.log("hello from logout")
        console.log(localStorage)
        localStorage.removeItem('token')
        delete axios.defaults.headers.authorization
        resolve()
      })
    },
  },
  getters: {
    EMPLOYERS(state) {
      return state.employers;
    },
    STUDENTS(state) {
      return state.students;
    },
    isAuthenticated: state => !!state.token,
  },
  modules: {
  }
})
