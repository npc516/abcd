<template>
  <div>
      <img id= "CatBg" style="position:absolute; top:120px; left:500px; width:850px" :src='imageLoad()'>
      <button style="position:absolute; top:120px; left:1300px; width:100px" v-on:click='imageChange()'>Feeling Kitty</button>
      <p>Show me another cat!</p>
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
