<template>
  <div class='formcatchec'>
    <div id="trainer">
      <ul id="cattest">
        <li v-for="cat in cats" :key='cat.id'>
          <div class='trainerform'>
            <div style="display:inline; width:40; float:left; margin-right: 50px">
            <img style='width:350px; height:300px;' :src="loadImage(cat.photo_path)">
            </div>
            <div style=" text-align:left; display:inline; width:60px float:left">
              <p style="color:white; text-align:left; font-size:30px">name: {{cat.name}}</p>
              <p style="color:white; text-align:left; font-size:30px">age: {{cat.age}} </p>
              <p style="color:white; text-align:left; font-size:30px">Breed: {{cat.breed}} </p>
              <p style="color:white; text-align:left; font-size:30px">Weight: {{cat.weight}}</p>
              <p style="color:white; text-align:left; font-size:30px">color: {{cat.color}} </p>
            </div>
            <br><br>
            <button class="button button-block" onclick="window.location.href='/buyitnow'">Buy it Now</button>
            <br>
            <button class="button button-block" onclick="window.location.href='/bidding'">Enter Bidding</button>
          </div>
        </li>
      </ul>
    </div>
    <div class='formchec'>
    </div>
  </div>

</template>

<script>
import Cat from '../scripts/cat.js'
export default {
  name: 'cattest',
  data () {
    return {
      cats: null
    }
  },
  methods: {
    loadImage (imagePath) {
      return require('../assets/image/' + imagePath + '.jpg')
    }
  },
  mounted: function () {
    Cat.get_all_cat((res) => {
      this.cats = res
    })
  }
}

</script>

<style>
@import '../../static/css/style.css';
</style>
