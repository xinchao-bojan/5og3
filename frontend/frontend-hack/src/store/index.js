import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axios from 'axios'
export default new Vuex.Store({
  state: {
    employers: [],
    token: localStorage.getItem('token') || '',
  },
  mutations: {
    SET_EMPLOYERS_TO_STATE: (state, employers) => {
      console.log("Hello from store.js SET_EMPLOYERS_TO_STATE")
      state.employers = employers
      console.log("steate", state.employers);
    },
    LOGOUT(state) {
      console.log("Hello from store.js LOGOUT")
      state.token = ''
  },
  },
  actions: {
    GET_EMPLOYERS_FROM_API({ commit }) {
      console.log("Hello from GET_EMPLOYERS_FROM_API")
      return axios('https://dafbb6132c6f.ngrok.io/api/test/', {
        method: "GET"
      })
        .then((employers) => {
          console.log("commit articles", employers.data);
          commit('SET_EMPLOYERS_TO_STATE', employers.data);
          console.log("commit articles", employers.data);
          return employers;
        },
          reason => {
            console.log("reason")
            console.log(reason)
          })
        .catch((error) => {
          console.log(error);
          return error;
        })
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
    ARTICLES(state) {
      return state.articles;
    },
    isAuthenticated: state => !!state.token,
  },
  modules: {
  }
})
