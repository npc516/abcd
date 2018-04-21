<template>
  <div class='form'>

    <div id="Bid" v-if='s'>
      <h1> {{ smsg }} </h1>
      <h1> {{ pmsg }} </h1>

          <div class="field-wrap">
        <label v-bind:class='{active: newprice!=="" && newprice!==null, highlight: newprice!=="" && newprice!==null}'>
          Your Price <span class="req">*</span>
        </label>
        <input type="tel" v-model='newprice' required autocomplete="off"/>
      </div>

      <button class="button button-block" v-on:click='bid()'>Bid</button>

    </div>

    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
import Auth from '../scripts/auth'
export default {
  name: 'Bid',
  data () {
    return {
      newprice:null,
      s: true,
      smsg: 'The highest bidding for this cat is',
      pmsg: '[put price here]'
    }
  },
  methods: {
     update_price() {
      Auth.update_price({
      newprice:this.newprice
      },
      (err, data) => {
        if (newprice<=oldprice && err == null) {
          this.lmsg = 'Low Price!'
        } else {
          this.lmsg = 'Bidding Succesful!'
        }
    })
    }
}
}
</script>
