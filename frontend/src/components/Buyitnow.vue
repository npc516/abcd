<template>
  <div class='form'>

    <div id="buy" v-if='s'>
      <h1> {{ smsg }} </h1>
      <h1> {{ pmsg }} </h1>

      <button class="button button-block" v-on:click='buy_it_now()'>Buy it now</button>

    </div>

    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
import Cat from '../scripts/cat.js'
import BuyItNow from '../scripts/buyitnow.js'
import Router from '../router/index.js'
export default {
  name: 'Buyitnow',
  data () {
    return {
      s: true,
      smsg: 'The Buy-It-Now price for this cat is',
      pmsg: 'TBD'
    }
  },
  mounted: function () {
    Cat.get_cat({'cat_id': this.$route.params.cat_id}, (res) => {
      this.pmsg = res['buy_it_now']
    })
  },
  methods: {
    buy_it_now () {
      BuyItNow.buy_it_now({'cat_id': this.$route.params.cat_id}, (res) => {
        Router.push('/delivery/' + this.$route.params.cat_id)
      })
    }
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
