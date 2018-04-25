<template>
  <div class='formta'>

<div id="trainer" >
<li v-for='name in [1,2,3,4,5,6,7,8]'>
  <div class='trainerform'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:350px; height:300px; ' src='../assets/image/british-shorthair-cats.jpg'>
    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px">name: </p>
      <p style="color:white; text-align:left; font-size:30px">age: </p>
        <p style="color:white; text-align:left; font-size:30px">Breed: </p>
        <p style="color:white; text-align:left; font-size:30px">Weight:</p>
        <p style="color:white; text-align:left; font-size:30px">color: </p>
    </div>
    <br><br>
    <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
    <br>
    <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
  </div>
</li>

</div>

</div>
</template>

<style>
  @import '../../static/css/style.css';
</style>
