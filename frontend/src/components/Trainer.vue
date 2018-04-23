<template>
  <div class='formta'>
    <img style="position:absolute; top:2670px; left:710px; width:400px" src="../assets/image/icon.png">
    <h1 style="font-size:500px color:white font-family:arial">Check our professional trainers!</h1>
<div id="trainer" v-if='!s'>
  <div class='trainerform'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:250px; height:300px; ' src='../assets/image/jack.jpg'>
    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px">Trainer Name: Jack Weng</p>
      <p style="color:white; text-align:left; font-size:30px">Trainer fee: $0.05/h</p>
        <p style="color:white; text-align:left; font-size:30px">Trainer license: 034813482</p>
          <p style="color:white; text-align:left; font-size:30px">Trainer routine: sleeping</p>
            <p style="color:white; text-align:left; font-size:30px">Trainer rating: 59/100</p>
    </div>
    <div style="text-align:center">
        <p style="color:white; text-align:left; font-size:30px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;Trainer experience: N/A</p>
    </div><br><br>
      <button class="button button-block" onclick="window.location.href='/Insurance'">choose</button>
      <!--点击时连接上database里user的信息和trainer信息，并跳转到insurance页面。暂时只实现了跳转页面-->
 </div>
<br><br><br>
<div class='trainerform'>
<div style="display:inline; width:40; float:left; margin-right: 50px">
<img style='width:250px; height:300px; ' src='../assets/image/jacky.jpg'>
</div>
<div style=" text-align:left; display:inline; width:60px float:left">
<p style="color:white; text-align:left; font-size:30px">Trainer Name: Jacky Wong</p>
<p style="color:white; text-align:left; font-size:30px">Trainer fee: $0.06/h</p>
  <p style="color:white; text-align:left; font-size:30px">Trainer license: 034813562</p>
    <p style="color:white; text-align:left; font-size:30px">Trainer routine: running</p>
      <p style="color:white; text-align:left; font-size:30px">Trainer rating: 56/100</p>
</div>
<div style="text-align:center">
  <p style="color:white; text-align:left; font-size:30px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Trainer experience: N/A</p>
</div><br><br>
<button class="button button-block" onclick="window.location.href='/Insurance'">choose</button>
<!--点击时连接上database里user的信息和trainer信息，并跳转到insurance页面。暂时只实现了跳转页面-->
</div>
<br><br><br>
<div class='trainerform'>
<div style="display:inline; width:40; float:left; margin-right: 50px">
<img style='width:250px; height:300px; ' src='../assets/image/jjj.jpg'>
</div>
<div style=" text-align:left; display:inline; width:60px float:left">
<p style="color:white; text-align:left; font-size:30px">Trainer Name: Jackson Wung</p>
<p style="color:white; text-align:left; font-size:30px">Trainer fee: $0.07/h</p>
  <p style="color:white; text-align:left; font-size:30px">Trainer license: 254813482</p>
    <p style="color:white; text-align:left; font-size:30px">Trainer routine: walking</p>
      <p style="color:white; text-align:left; font-size:30px">Trainer rating: 94/100</p>
</div>
<div style="text-align:center">
  <p style="color:white; text-align:left; font-size:30px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;Trainer experience: N/A</p>
</div><br><br>
<button class="button button-block" onclick="window.location.href='/Insurance'">choose</button>
<!--点击时连接上database里user的信息和trainer信息，并跳转到insurance页面。暂时只实现了跳转页面-->
</div>
<br><br><br>
</div>
<p style="text-align:right; font-size:30px; font-color:white"><a href="/Insurance">skip this step</a></p>
</div>
</template>

<style>
  @import '../../static/css/style.css';
</style>
