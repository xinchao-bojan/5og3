import Home from '../components/Home.vue'
import EmployersList from '../components/EmployersList.vue'
import StudentSearchPage from '../components/StudentSearchPage.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/EmployersList',
    name: 'EmployersList',
    component: EmployersList
  },
  {
    path: '/StudentSearchPage',
    name: 'StudentSearchPage',
    component: StudentSearchPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
