<template>
  <div class='formta'>

<div id="trainer" >

  <ul id="cattest">
<li v-for="item in items" :key="item.name">
  <div class='trainerform'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:350px; height:300px;' :src="loadImage(item.path)">
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

</div>
</template>
<script>
export default {
  name: 'cattest',
  data () {
    return {
      items: [
        {
          path: 'bosi',
          name: 'null',
          age: 'null',
          breed: 'null',
          weight: 'null',
          color: 'null'
        },
        {
          path: 'british-shorthair-cats',
          name: 'jack',
          age: '20',
          breed: 'human',
          weight: 'infinity',
          color: '???'
        },
        {
          path: 'ragdol',
          name: 'Aaron',
          age: '20',
          breed: 'human',
          weight: 'infinity',
          color: '???'
        }
      ]
    }
  },
  methods: {
    loadImage (imagePath) {
      return require('../assets/image/' + imagePath + '.jpg')
    }
  }
}

</script>

<style>
  @import '../../static/css/style.css';
</style>
