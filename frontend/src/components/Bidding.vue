<template>
  <div class='form'>

    <div id="Bid" v-if='s'>
      <h1> {{ smsg }} </h1>
      <h1> {{ pmsg }} </h1>

      <div class="field-wrap">
        <label v-bind:class='{active: newprice !== "" && newprice !== null, highlight: newprice !== "" && newprice !== null}'>
          Your Price <span class="req">*</span>
        </label>
        <input type="tel" v-model='newprice' required autocomplete="off"/>
      </div>

      <button class="button button-block" v-on:click='bid()' :disabled='newprice <= pmsg'>Bid</button>

    </div>

    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
import Bidding from '../scripts/bidding.js'
import Auth from '../scripts/auth.js'
export default {
  name: 'Bid',
  data () {
    return {
      newprice: null,
      s: true,
      smsg: 'The highest bidding for this cat is',
      pmsg: null,
      user_email: null
    }
  },
  mounted: function () {
    Bidding.get_high_bid({'cat_id': this.$route.params.cat_id}, (res) => {
      this.pmsg = res['price']
    })
    this.user_email = Auth.current_user()
  },
  methods: {
    bid () {
      Bidding.bid({
        cat_id: this.$route.params.cat_id,
        price: this.newprice,
        user_email: this.user_email
      }, (res) => {
        this.pmsg = res['price']
        // Router.push('/delivery/' + this.$route.params.cat_id)
      })
    }
  }
}
</script>
<style scope>
@import '../../static/css/style.css';

.button[disabled] {
  background: #cccccc
}

</style>
