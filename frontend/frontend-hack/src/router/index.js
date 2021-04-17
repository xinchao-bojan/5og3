import Home from '../components/Home.vue'
import EmployersList from '../components/EmployersList.vue'
import StudentSearchPage from '../components/StudentSearchPage.vue'
import ChangeStudentCard from '../components/ChangeStudentCard.vue'
import ChangeEmployerCard from '../components/ChangeEmployerCard.vue'
import EducationalOrganizations from '../components/EducationalOrganizations.vue'
import InternshipCreation from '../components/InternshipCreation.vue'
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
  },
  {
    path: '/ChangeStudentCard',
    name: 'ChangeStudentCard',
    component: ChangeStudentCard
  },
  {
    path: '/ChangeEmployerCard',
    name: 'ChangeEmployerCard',
    component: ChangeEmployerCard
  },
  {
    path: '/EducationalOrganizations',
    name: 'EducationalOrganizations',
    component: EducationalOrganizations
  },
  {
    path: '/InternshipCreation',
    name: 'InternshipCreation',
    component: InternshipCreation
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
