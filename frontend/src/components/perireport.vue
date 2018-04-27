<template>
<div class='formta'>
<h1 style="font-size:500px color:white font-family:arial">Peridoic Report</h1>
<div id="report">
<div class='trainerform'>
<div style="display:inline; width:40; float:left; margin-right: 50px">

</div>
<div style=" text-align:left; display:inline; width:60px float:left">
<p style="color:white; text-align:left; font-size:30px">Timestamp: {{timestamp}}</p>
<p style="color:white; text-align:left; font-size:30px">Number of recorded cats: {{numcat}}</p>
<p style="color:white; text-align:left; font-size:30px">Number of matches across this quarter: {{numquart}}</p>
<p style="color:white; text-align:left; font-size:30px">Number of trainers available: {{numtrainer}}</p>
<p style="color:white; text-align:left; font-size:30px">Number of sponsors available: {{numspon}}</p>
<p style="color:white; text-align:left; font-size:30px">Number of deliveries made: {{numdeli}}</p>

</div>
<br><br>
<button class="button button-block" v-on:click='count_cat()'>generate</button>
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
      numtrainer: null,
      numspon: null,
      numdeli: null
    }
  },
  methods: {
    count_cat () {
      Cat.count_all_cat((numcat) => {
        this.numcat = numcat
        this.timestamp = 'Spring 2018'
        this.numquart = 1000
        this.numtrainer = 3
        this.numspon = 3
        this.numdeli = 100
      })
    }
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
