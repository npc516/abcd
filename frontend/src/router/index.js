import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/Index'
import Auth from '@/components/Auth'
import Match from '@/components/Match'
import Trainer from '@/components/Trainer'
import Insurance from '@/components/Insurance'
import Signupsuc from '@/components/Signupsuc'
import Sponsorship from '@/components/Sponsorship'
import Cat from '@/components/Cat'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '*',
      name: 'Star',
      component: Index
    },
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/index',
      name: 'Index',
      component: Index
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/match',
      name: 'Match',
      component: Match
    },
    {
      path: '/trainer',
      name: 'Trainer',
      component: Trainer
    },
    {
      path: '/insurance',
      name: 'Insurance',
      component: Insurance
    },
    {
      path: '/signupsuc',
      name: 'Signupsuc',
      component: Signupsuc
    },
    {
      path: '/Sponsorship',
      name: 'Sponsorship',
      component: Sponsorship
    },
    {
      path: '/Cat',
      name: 'Cat',
      component: Cat
    }

  ]
})
