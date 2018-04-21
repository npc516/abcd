import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/Index'
import Auth from '@/components/Auth'
import Buyitnow from '@/components/Buyitnow'
import Delivery from '@/components/Delivery'
import Bidding from '@/components/Bidding'

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
    }
  ]
})
