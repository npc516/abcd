<template>
  <div class='formcatchec'>
    <div id="trainer">
      <ul id="cattest">
        <li v-for="cat in cats" :key='cat.cat_id'>
          <div class='trainerform'>
            <div style="display:inline; width:40; float:left; margin-right: 50px">
            <img style='width:350px; height:300px;' :src="loadImage(cat.photo_path)">
            </div>
            <div style="text-align:left; display:inline; width:60px float:left">
              <p style="color:white; text-align:left; font-size:30px">Name: {{cat.name}}</p>
              <p style="color:white; text-align:left; font-size:30px">Age: {{cat.age}} </p>
              <p style="color:white; text-align:left; font-size:30px">Breed: {{cat.breed}} </p>
              <p style="color:white; text-align:left; font-size:30px">Weight: {{cat.weight}}</p>
              <p style="color:white; text-align:left; font-size:30px">Color: {{cat.color}} </p>
            </div>
            <br><br>
            <button class="button button-block" v-on:click='detail(cat.cat_id)'>Details</button>
            <br>
            <button v-if='logged_in && current_user != cat.owner_email && cat.buy_it_now' class="button button-block" v-on:click='buy_it_now(cat.cat_id)'>Buy it Now</button>
            <br>
            <button v-if='logged_in && current_user != cat.owner_email && has_auction.includes(cat.cat_id)' class="button button-block" v-on:click='bid(cat.cat_id)'>Enter Bidding</button>
          </div>
        </li>
      </ul>
    </div>
  </div>

</template>

<script>
import Cat from '../scripts/cat.js'
import Auth from '../scripts/auth.js'
import Router from '../router/index.js'
export default {
  name: 'cattest',
  data () {
    return {
      cats: null,
      logged_in: false,
      has_auction: [],
      current_user: null
    }
  },
  methods: {
    loadImage (imagePath) {
      return require('../assets/image/' + imagePath + '.jpg')
    },
    detail (cid) {
      Router.push('/singlecat/' + cid)
    },
    buy_it_now (cid) {
      Router.push('/buyitnow/' + cid)
    },
    bid (cid) {
      Router.push('/bidding/' + cid)
    }
  },
  mounted: function () {
    this.cats = this.$route.params.cats
    for (let i = 0; i < this.cats.length; ++i) {
      Cat.has_auction({
        cat_id: this.cats[i].cat_id
      }, (res) => {
        if (res.length !== 0) {
          this.has_auction.push(this.cats[i].cat_id)
        }
      })
    }
    this.logged_in = Auth.is_logged_in()
    this.current_user = Auth.current_user()
  }
}

</script>

<style>
@import '../../static/css/style.css';
</style>
