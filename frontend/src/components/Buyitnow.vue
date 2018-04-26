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
export default {
  name: 'Buyitnow',
  data () {
    return {
      s: true,
      smsg: 'The current price for this cat is',
      pmsg: 'TBD'
    }
  },
  methods: {
    buy_it_now () {
    }
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
