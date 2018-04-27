<template>
  <div class='formta'>
    <img style="position:absolute; top:2770px; left:710px; width:400px" src="../assets/image/icon.png">
    <h1 style="font-size:500px color:white font-family:arial">Check our professional trainers!</h1>
<div id="trainer" >


<ul id="traintest">
  <li v-for="trainer in trainers" :key='trainer.id'>
<div class='trainerform'>
<div style="display:inline; width:40; float:left; margin-right: 50px">
<img style='width:250px; height:300px; ' src="../assets/image/icon.png">
</div>
<div style=" text-align:left; display:inline; width:60px float:left">
<p style="color:white; text-align:left; font-size:30px">Trainer Name: </p>
<p style="color:white; text-align:left; font-size:30px">Trainer fee: </p>
  <p style="color:white; text-align:left; font-size:30px">Trainer license: </p>
    <p style="color:white; text-align:left; font-size:30px">Trainer routine: </p>
      <p style="color:white; text-align:left; font-size:30px">Trainer rating: </p>
</div>
<div style="text-align:center">
  <p style="color:white; text-align:left; font-size:30px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;Trainer experience: N/A</p>
</div><br><br>
<button class="button button-block" onclick="window.location.href='/Insurance'">choose</button>
<!--点击时连接上database里user的信息和trainer信息，并跳转到insurance页面。暂时只实现了跳转页面-->
</div>
</li>
</ul>
<br><br><br>
</div>
<p style="text-align:right; font-size:30px; font-color:white"><a href="/Insurance">skip this step</a></p>
</div>
</template>

<script>
export default {
  name: 'traintest',
  data () {
    return {
      trainers: [
        {
          path: 'jjj',
          id: '1',
          name: 'jackson wung',
          fee: '$0.07/h',
          license: '324723242',
          routine: 'walking',
          rating: '94/100'
        }
      ]
    }
  },
  methods: {
    loadImage (imagePath) {
      return require('../assets/image/' + imagePath + '.jpg')
    }
  }

}
</script>
<style>
  @import '../../static/css/style.css';
</style>
