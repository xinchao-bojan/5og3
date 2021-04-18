import Home from '../components/Home.vue'
import login from '../components/login.vue'
import registration from '../components/registration.vue'
import profile from '../components/Profile-student.vue'
import EmployersList from '../components/EmployersList.vue'
import StudentSearchPage from '../components/StudentSearchPage.vue'
import ChangeEmployerCard from '../components/ChangeEmployerCard.vue'
import ChangeStudentCard from '../components/ChangeStudentCard.vue'
import EducationalOrganization from '../components/EducationalOrganizations.vue'
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
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/registration',
    name: 'registration',
    component: registration
  },
  {
    path: '/profile',
    name: 'profile',
    component: profile
  },
  {
    path: '/EmployersList',
    name: 'employersList',
    component: EmployersList
  },
  {
    path: '/StudentSearchPage',
    name: 'StudentSearchPage',
    component: StudentSearchPage
  },
  {
    path: '/ChangeEmployerCard',
    name: 'ChangeEmployerCard',
    component: ChangeEmployerCard
  },
  {
    path: '/ChangeStudentCard',
    name: 'ChangeStudentCard',
    component: ChangeStudentCard
  },
  {
    path: '/EducationalOrganization',
    name: 'EducationalOrganization',
    component: EducationalOrganization
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
