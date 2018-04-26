import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AddCat from '@/components/AddCat'
import CatSearch from '@/components/CatSearch'
import Index from '@/components/Index'
import Auth from '@/components/Auth'
import Buyitnow from '@/components/Buyitnow'
import Delivery from '@/components/Delivery'
import Bidding from '@/components/Bidding'
import Match from '@/components/Match'
import Trainer from '@/components/Trainer'
import Insurance from '@/components/Insurance'
import Signupsuc from '@/components/Signupsuc'
import Sponsorship from '@/components/Sponsorship'
import MainPage from '@/components/MainPage'
import Cat from '@/components/Cat'
import test from '@/components/test'
import perireport from '@/components/perireport'
import singlecat from '@/components/singlecat'

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
      path: '/cat',
      name: 'Cat',
      component: Cat
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/AddCat',
      name: 'AddCat',
      component: AddCat
    },
    {
      path: '/CatSearch',
      name: 'CatSearch',
      component: CatSearch
    },
    {
      path: '/buyitnow',
      name: 'Buyitnow',
      component: Buyitnow
    },
    {
      path: '/delivery',
      name: 'Delivery',
      component: Delivery
    },
    {
      path: '/bidding',
      name: 'Bidding',
      component: Bidding
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
      path: '/MainPage',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/perireport',
      name: 'perireport',
      component: perireport
    },
    {
      path: '/singlecat',
      name: 'singlecat',
      component: singlecat
    }
  ]
})
