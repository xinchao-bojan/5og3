import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axios from 'axios'
export default new Vuex.Store({
  state: {
    employers: ['asdasdads', 'asdsadads'],
    token: localStorage.getItem('token') || '',
  },
  mutations: {
    SET_EMPLOYERS_TO_STATE: (state, employers) => {
      console.log("Hello from store.js SET_EMPLOYERS_TO_STATE", employers)
      state.employers = employers
      console.log("state", state.employers);
    },
    LOGOUT(state) {
      console.log("Hello from store.js LOGOUT")
      state.token = ''
    },
  },
  actions: {
    GET_EMPLOYERS_FROM_API({ commit }) {
      console.log("Hello from GET_EMPLOYERS_FROM_API")
      console.log("token: ", localStorage.getItem('token'));
      return axios
        .request({
          url: "https://9021260458c0.ngrok.io/api/practice/all/",
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
          console.log("employers.data", employers.data);
          console.log("employers: ", employers);
          commit('SET_EMPLOYERS_TO_STATE', employers.data);
          console.log("commit articles", employers.data);
          return employers;
        }).catch(function (error) {
          console.error(error.response);
        });
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
    isAuthenticated: state => !!state.token,
  },
  modules: {
  }
})
