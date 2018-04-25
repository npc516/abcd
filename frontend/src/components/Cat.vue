<template>
  <div class='formta'>

<div id="trainer" v-if='!s'>
  <div class='trainerform' id='1'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:350px; height:300px; ' src='../assets/image/british-shorthair-cats.jpg'>
    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px">Cat Name: Aaron</p>
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
  <div class='trainerform' id='2'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:350px; height:300px; ' src='../assets/image/ragdol.jpg'>
    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px">Cat Name: Bob</p>
      <p style="color:white; text-align:left; font-size:30px">age: 3</p>
        <p style="color:white; text-align:left; font-size:30px">Breed: Ragdoll</p>
        <p style="color:white; text-align:left; font-size:30px">Weight: 17 pounds</p>
        <p style="color:white; text-align:left; font-size:30px">color: black&white</p>
    </div>
    <br><br>
    <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
    <br>
    <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
 </div>
 <div class='trainerform' id='3'>
   <div style="display:inline; width:40; float:left; margin-right: 50px">
    <img style='width:350px; height:300px; ' src='../assets/image/blue_cat.jpg'>
   </div>
   <div style=" text-align:left; display:inline; width:60px float:left">
     <p style="color:white; text-align:left; font-size:30px">Cat Name: Jocky</p>
     <p style="color:white; text-align:left; font-size:30px">age: 3 months</p>
       <p style="color:white; text-align:left; font-size:30px">Breed: Russian Blue</p>
       <p style="color:white; text-align:left; font-size:30px">Weight: 5 pounds</p>
       <p style="color:white; text-align:left; font-size:30px">color: grey</p>
   </div>
   <br><br>
   <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
   <br>
   <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
</div>
<div class='trainerform' id='4'>
  <div style="display:inline; width:40; float:left; margin-right: 50px">
   <img style='width:350px; height:300px; ' src='../assets/image/bosi.jpg'>
  </div>
  <div style=" text-align:left; display:inline; width:60px float:left">
    <p style="color:white; text-align:left; font-size:30px">Cat Name: Jackson</p>
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
<div class='trainerform' id='5'>
  <div style="display:inline; width:40; float:left; margin-right: 50px">
   <img style='width:350px; height:300px; ' src='../assets/image/jackmao.jpg'>
  </div>
  <div style=" text-align:left; display:inline; width:60px float:left">
    <p style="color:white; text-align:left; font-size:30px">Cat Name: Noah</p>
    <p style="color:white; text-align:left; font-size:30px">age: 2</p>
      <p style="color:white; text-align:left; font-size:30px">Breed: ???</p>
      <p style="color:white; text-align:left; font-size:30px">Weight: 85 pounds</p>
      <p style="color:white; text-align:left; font-size:30px">color: white</p>
  </div>
  <br><br>
  <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
  <br>
  <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
</div>
<div class='trainerform' id='6'>
  <div style="display:inline; width:40; float:left; margin-right: 50px">
   <img style='width:350px; height:300px; ' src='../assets/image/yellow.jpg'>
  </div>
  <div style=" text-align:left; display:inline; width:60px float:left">
    <p style="color:white; text-align:left; font-size:30px">Cat Name: Jerry</p>
    <p style="color:white; text-align:left; font-size:30px">age: 3</p>
      <p style="color:white; text-align:left; font-size:30px">Breed: grimalkin</p>
      <p style="color:white; text-align:left; font-size:30px">Weight: 15 pounds</p>
      <p style="color:white; text-align:left; font-size:30px">color: Yellow</p>
  </div>
  <br><br>
  <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
  <br>
  <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
</div>
<div class='trainerform' id='7'>
  <div style="display:inline; width:40; float:left; margin-right: 50px">
   <img style='width:350px; height:300px; ' src='../assets/image/A-Siamese-cat.jpg'>
  </div>
  <div style=" text-align:left; display:inline; width:60px float:left">
    <p style="color:white; text-align:left; font-size:30px">Cat Name: Mia</p>
    <p style="color:white; text-align:left; font-size:30px">age: 2</p>
      <p style="color:white; text-align:left; font-size:30px">Breed: Siamese</p>
      <p style="color:white; text-align:left; font-size:30px">Weight: 15 pounds</p>
      <p style="color:white; text-align:left; font-size:30px">color: white&black</p>
  </div>
  <br><br>
  <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
  <br>
  <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
</div>
<div class='trainerform' id='8'>
  <div style="display:inline; width:40; float:left; margin-right: 50px">
   <img style='width:350px; height:300px; ' src='../assets/image/dog.jpg'>
  </div>
  <div style=" text-align:left; display:inline; width:60px float:left">
    <p style="color:white; text-align:left; font-size:30px">Cat Name: jake</p>
    <p style="color:white; text-align:left; font-size:30px">age: 1</p>
      <p style="color:white; text-align:left; font-size:30px">Breed: Dog</p>
      <p style="color:white; text-align:left; font-size:30px">Weight: 15 pounds</p>
      <p style="color:white; text-align:left; font-size:30px">color: white&yellow</p>
  </div>
  <br><br>
  <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
  <br>
  <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
</div>
<div id="trainer" >

  <ul id="cattest">
<li v-for="item in items" :key="item.name">
  <div class='trainerform'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:350px; height:300px; ' src='../assets/image/british-shorthair-cats.jpg'>
    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px">name: {{item.name}}</p>
      <p style="color:white; text-align:left; font-size:30px">age:{{item.age}} </p>
        <p style="color:white; text-align:left; font-size:30px">Breed:{{item.breed}} </p>
        <p style="color:white; text-align:left; font-size:30px">Weight:{{item.weight}}</p>
        <p style="color:white; text-align:left; font-size:30px">color:{{item.color}} </p>
    </div>
    <br><br>
    <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
    <br>
    <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
  </div>
</li>
</ul>

</div>

<br><br><br>
</div>

</div>
</template>
<script>
export default {
  name: 'cattest',
  data () {
    return {
      items: [
        {
          name: 'null',
          age: 'null',
          breed: 'null',
          weight: 'null',
          color: 'null'
        },
        {
          name: 'jack',
          age: '20',
          breed: 'human',
          weight: 'infinity',
          color: '???'
        }
      ]
    }
  }
}

</script>

<style>
  @import '../../static/css/style.css';
</style>
