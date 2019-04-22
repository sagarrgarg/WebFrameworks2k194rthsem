import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

import Auth from '@/components/pages/Auth'
import Books from '@/components/pages/Books'
import CreateBook from '@/components/pages/CreateBook'
import CreateUser from '@/components/pages/createauth'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/books',
      name: 'Books',
      component: Books
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path:'/createbook',
      name: 'CreateBook',
      component: CreateBook
    },
    {
      path:'/createuser',
      name: 'CreateUser',
      component: CreateUser
    },
  ]
})
