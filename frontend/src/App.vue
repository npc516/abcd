<template>
  <div id="app">
    <app-header></app-header>
    <app-tail></app-tail>
    <router-view></router-view>
  </div>
</template>

<script>

import header from './components/header'
import tail from './components/tail'

export default {
  components: {
    'app-header': header,
    'app-tail': tail
  }
}
</script>

<style>
@import '../node_modules/bootstrap/dist/css/bootstrap.css';
@import './assets/css/style.css';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
