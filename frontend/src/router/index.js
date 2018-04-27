import Vue from 'vue'
import Router from 'vue-router'
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
import mycat from '@/components/mycat'
import SearchResult from '@/components/SearchResult'

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
      name: 'MainPage',
      component: MainPage,
      alias: '/MainPage'
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
      path: '/buyitnow/:cat_id',
      name: 'Buyitnow',
      component: Buyitnow
    },
    {
      path: '/delivery/:cat_id',
      name: 'Delivery',
      component: Delivery
    },
    {
      path: '/bidding/:cat_id',
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
      path: '/searchresult',
      name: 'SearchResult',
      component: SearchResult
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
      path: '/singlecat/:cat_id',
      name: 'singlecat',
      component: singlecat
    },
    {
      path: '/mycat',
      name: 'mycat',
      component: mycat
    }
  ]
})
