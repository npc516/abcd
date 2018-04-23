<template>
  <div class='form'>
  <img style="position:absolute; top:2365px; left:710px; width:400px" src="../assets/image/icon.png">
    <ul class="tab-group">
      <li class="tab" v-bind:class='{active:s}'> <a href="#match" v-on:click='s=true'>MATCH INFORMATION</a></li>
    </ul>
    <br><br>
    <div style="text-align:center">
      <p style="color:white; font-size: 23px">AUDITION:</p>
      <p style="color:white; font-size: 30px">  March 18th 2018 12:00-16:00</p>
      <p style="color:white; font-size: 23px">ELIMINATION:</p>
      <p style="color:white; font-size: 30px">April 2nd 2018 9:30-16:30</p>
      <p style="color:white; font-size: 23px">ROUND ONE:</p>
      <p style="color:white; font-size: 30px">April 10th 19:30-22:30</p>
      <p style="color:white; font-size: 23px">SEMIFINAL:</p>
      <p style="color:white; font-size: 30px">April 17th 19:30-21:30</p>
      <p style="color:white; font-size: 23px">FINAL:</p>
      <p style="color:white; font-size: 30px">April 25th 19:30-21:30</p>
    </div>
    <br><br><br><br>
    <div id="match" >
<br><br><br>
      <img style='width:1550px' src="../assets/image/maomao.png" usemap="#catmap" alt="catmatch">
        <map name="catmap" id="catmap">
          <area
            shape="circle"
            coords="760,60,70"
            href="www.baidu.com"
            target="blank"
            alt="champ">

        <area
          shape="circle"
          coords="440,320,70"
          href="www.baidu.com"
          target="blank"
          alt="yazuo">
      <area
        shape="circle"
        coords="1140,320,70"
        href="www.baidu.com"
        target="blank"
        alt="yayou">
      <area
        shape="circle"
        coords="260,590,70"
        href="www.baidu.com"
        target="blank"
        alt="3-1">
        <area
          shape="circle"
          coords="620,590,70"
          href="www.baidu.com"
          target="blank"
          alt="3-2">
          <area
            shape="circle"
            coords="960,590,70"
            href="www.baidu.com"
            target="blank"
            alt="3-3">
            <area
              shape="circle"
              coords="1320,590,70"
              href="www.baidu.com"
              target="blank"
              alt="3-4">
              <area
                shape="circle"
                coords="180,860,70"
                href="www.baidu.com"
                target="blank"
                alt="4-1">
                <area
                  shape="circle"
                  coords="360,860,70"
                  href="www.baidu.com"
                  target="blank"
                  alt="4-2">
                  <area
                    shape="circle"
                    coords="540,860,70"
                    href="www.baidu.com"
                    target="blank"
                    alt="4-3">
                    <area
                      shape="circle"
                      coords="700,860,70"
                      href="www.baidu.com"
                      target="blank"
                      alt="4-4">
                      <area
                        shape="circle"
                        coords="880,860,70"
                        href="www.baidu.com"
                        target="blank"
                        alt="4-5">
                        <area
                          shape="circle"
                          coords="1060,860,70"
                          href="www.baidu.com"
                          target="blank"
                          alt="4-6">
                          <area
                            shape="circle"
                            coords="1240,860,70"
                            href="www.baidu.com"
                            target="blank"
                            alt="4-7">
                            <area
                              shape="circle"
                              coords="1400,860,70"
                              href="www.baidu.com"
                              target="blank"
                              alt="4-8">
<!--图片上每个猫都做了map，用户点击时应该会连接到相应的猫的信息。准备在猫的界面用ID解决-->
</map>
    </div>

    <br><br><br>
    <ul class="tab-group">
      <button class="button button-block" onclick="window.location.href='/Trainer'">JOIN THE MATCH NOW!</button>
  <!--当用户已经login，direct到trainer界面，如果没login就转到login界面。
  //据说是用session实现，尝试了一下但没写出来。。-->
    </ul>
  </div>
</template>

<script>

</script>

<style>
  @import '../../static/css/match.css';
</style>
