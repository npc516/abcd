<template>
  <div class='form'>

<<<<<<< HEAD
    <div id="buy" v-if='s'>
=======
    <div id="signup" v-if='s'>
>>>>>>> a7c5b0ad39a744ac11bf5a7252b1013aeef53206
      <h1> {{ smsg }} </h1>
      <h1> {{ pmsg }} </h1>

      <button class="button button-block" v-on:click='buy_it_now()'>Buy it now</button>

    </div>

    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
// import Auth from '../scripts/auth'
export default {
<<<<<<< HEAD
  name: 'Buy',
=======
  name: 'Buyitnow',
>>>>>>> a7c5b0ad39a744ac11bf5a7252b1013aeef53206
  data () {
    return {
      s: true,
      smsg: 'The current price for this cat is',
      pmsg: '[put price here]'
    }
  },
  methods: {
    buy_it_now () {
<<<<<<< HEAD
=======

>>>>>>> a7c5b0ad39a744ac11bf5a7252b1013aeef53206
    }
  }
}
</script>
<<<<<<< HEAD

<style>
</style>
=======
>>>>>>> a7c5b0ad39a744ac11bf5a7252b1013aeef53206
