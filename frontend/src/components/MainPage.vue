<template>
  <div>
      <img id= "CatBg" style="position:absolute; top:120px; left:500px; width:850px" :src='imageLoad()'>
      <button class="button button-block" style="position:absolute; top:620px; left:500px; width:400px" v-on:click='imageChange()'>Feeling Kitty</button>
      <p style="position:absolute; top:180px; left:50px; width:400px; font-size: 150%">Welcome to Ultimate Cat-Fighting Championship</p>
      <p style="position:absolute; top:400px; left:50px; width:400px; font-size: 150%">Enjoy your Cat Adventure</p>
  </div>
</template>

<script>
export default {
  data () {
    return {
      ipath: '1'
    }
  },
  methods: {
    imageChange () {
      this.ipath = Math.floor(Math.random() * (4 - 1 + 1)) + 1
    },
    imageLoad () {
      return require('../assets/image/' + this.ipath + '.jpg')
    }
  }
}
</script>

<style>
  @import '../../static/css/style.css';
</style>
