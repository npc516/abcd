<template>
  <div class='formta'>
    <div id="trainer">
      <ul id="cattest">
        <li v-for="cat in cats" :key="cat.cat_id">
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
            <button class="button button-block" v-on:click='detail(cat.cat_id)'>Details</button>
            <br>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import Auth from '../scripts/auth.js'
import Router from '../router/index.js'
export default {
  data () {
    return {
      cats: null
    }
  },
  mounted: function () {
    Auth.user_cats((cats) => {
      this.cats = cats
      var cat
      for (cat of this.cats) {
        cat.min_price = null
      }
    })
  },
  methods: {
    loadImage (ipath) {
      return require('../assets/image/' + ipath + '.jpg')
    },
    detail (cid) {
      Router.push('/singlecat/' + cid)
    }
  }
}

</script>

<style>
@import '../../static/css/style.css';
</style>
