<template>
  <div class='formta'>
    <h1 style="font-size:500px color:white font-family:arial">CHOOSE YOUR INSURANCE PLAN!</h1>
<div id="trainer" v-if='!s'>
  <div class='trainerform'>
    <div style="display:inline; width:40; float:left; margin-right: 50px">
     <img style='width:350px; height:300px; ' src='../assets/image/icon.png'>
    </div>
    <div style=" text-align:left; display:inline; width:60px float:left">
      <p style="color:white; text-align:left; font-size:30px">Insurance Name: UCC full-cover</p>
      <p style="color:white; text-align:left; font-size:30px">Company name: niconico</p>
        <p style="color:white; text-align:left; font-size:30px">Insurance fee: $998</p>
          <p style="color:white; text-align:left; font-size:30px">Policy: TBD </p>

    </div>
    <br><br><br><br><br>
      <button class="button button-block" onclick="window.location.href='/Signupsuc'">choose</button>
      <!--点击时连接上database里user的信息和insurance信息，并跳转到signupsuc页面。暂时只实现了跳转页面-->
 </div>
<br><br><br>
<div class='trainerform'>
<div style="display:inline; width:40; float:left; margin-right: 50px">
<img style='width:350px; height:300px; ' src='../assets/image/catlogo.png'>
</div>
<div style=" text-align:left; display:inline; width:60px float:left">
  <p style="color:white; text-align:left; font-size:30px">Insurance Name: UCC full-cover</p>
  <p style="color:white; text-align:left; font-size:30px">Company name: miaomiaomiao</p>
    <p style="color:white; text-align:left; font-size:30px">Insurance fee: $798</p>
      <p style="color:white; text-align:left; font-size:30px">Policy: TBD </p>
</div>
<br><br>
<button class="button button-block" onclick="window.location.href='/Signupsuc'">choose</button>
<!--点击时连接上database里user的信息和insurance信息，并跳转到signupsuc页面。暂时只实现了跳转页面-->
</div>
<br><br><br>
</div>

</div>
</template>

<style>
  @import '../../static/css/style.css';
</style>
