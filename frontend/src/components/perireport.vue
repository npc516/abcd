<template>
<div class='formta'>
<h1 style="font-size:500px color:white font-family:arial">Peridoic Report</h1>
<div id="report">
<div class='trainerform'>
<div style="display:inline; width:40; float:left; margin-right: 50px">

</div>
<div style=" text-align:left; display:inline; width:60px float:left">
<p style="color:white; text-align:left; font-size:30px">Timestamp: {{timestamp}}</p>
<p style="color:white; text-align:left; font-size:30px">Number of Recorded Cats: {{numcat}}</p>
<p style="color:white; text-align:left; font-size:30px">Numer of Matches across This Quarter: {{numquart}}</p>
<p style="color:white; text-align:left; font-size:30px">Numer of Trainers Available: {{numtrainer}}</p>
</div>
<br><br>
<button v-on:click='count_cat()'>generate</button>
</div>
</div>

</div>
</template>

<script>
import Cat from '../scripts/cat.js'
export default{
  data () {
    return {
      numcat: null,
      timestamp: null,
      numquart: null,
      numtrainer: null
    }
  },
  methods: {
    count_cat () {
      Cat.count_all_cat((numcat) => {
        this.numcat = numcat
        this.timestamp = 'Spring 2018'
        this.numquart = 1000
        this.numtrainer = 3
      })
    }
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
