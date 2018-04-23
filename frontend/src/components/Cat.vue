<template>
  <div class='formta'>

<div id="trainer" v-if='!s'>
  <div class='trainerform'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:350px; height:300px; ' src='../assets/image/british-shorthair-cats.jpg'>
    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px">Cat Name: Bob</p>
      <p style="color:white; text-align:left; font-size:30px">age: 3</p>
        <p style="color:white; text-align:left; font-size:30px">Breed: British Shorthair</p>
        <p style="color:white; text-align:left; font-size:30px">Weight: 15 pounds</p>
        <p style="color:white; text-align:left; font-size:30px">color: grey</p>
    </div>
    <br><br>
    <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
    <br>
    <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
 </div>
<br><br><br>
</div>

</div>
</template>

<style>
  @import '../../static/css/style.css';
</style>
