<template>
  <div class='formta'>
    <img style='width:550px; height:500px; ' src='../assets/image/jackk.jpg'>
<div id="trainer" v-if='!s'>
  <div class='singleform' ><center>
    <div style="display:inline; width:30; float:left; margin-right: 50px; text-align:center">

    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Cat id: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Cat name: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Color: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Hometown: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Age: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Weight: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Breed: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Eye color: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Sex: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Ranking: </p>
      <p style="color:white; text-align:left; font-size:30px; text-align:center">Buy it now price: </p>
    </div>
 </center></div>
 <br>
 <div class='singleform'>
   <p style="color:white; text-align:left; font-size:30px">Username: </p>
   <div class='commentform'>
     <p>哦呵呵</p>
   </div>
 </div>
 <br>
 <div class='singleform'>
   <p style="color:white; text-align:left; font-size:30px">comment: </p>
     <input type="text"  required autocomplete="off" />
 </div>
</div>
</div>
</template>

<script>
import Cat from '../scripts/cat.js'
export default{
  data () {
    return {
      catid: null,
      name: null,
      color: null,
      hometown: null,
      age: null,
      weight: null,
      breed: null,
      eye: null,
      sex: null,
      rank: null,
      price: null,
      path: null,
      comment: null
    }
  },
  methods: {
    loadImage (imagePath) {
      return require('../assets/image' + imagePath + '.jpg')
    }
  }
}
</script>

<style>
  @import '../../static/css/style.css';
</style>
