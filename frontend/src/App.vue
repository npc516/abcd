<template>
  <div id="app">
    <app-header></app-header>
    <router-view></router-view>
  </div>
</template>

<script>

import header from './components/header'

export default {
  components: {
    'app-header': header
  }
}
</script>

<style>
@import '../node_modules/bootstrap/dist/css/bootstrap.css';
@import './assets/css/style.css';
@import '../static/css/style.css';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
