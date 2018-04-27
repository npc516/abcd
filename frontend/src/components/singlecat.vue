<template>
  <div class='formta'>
    <img style='width:550px; height:500px; ' src="loadImage(cat.path)">
    <div id="trainer">
      <div class='singleform'>
        <center>
          <div style="display:inline; width:30; float:left; margin-right: 50px; text-align:center">
          </div>
          <div style=" text-align:left; display:inline; width:60px float:left">
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Cat id: {{catid}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Cat name: {{name}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Color: {{color}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Hometown: {{hometown}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Age: {{age}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Weight: {{weight}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Breed: {{breed}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Eye color:{{eye}} </p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Sex: {{sex}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Ranking: {{rank}}</p>
            <p style="color:white; text-align:left; font-size:30px; text-align:center">Buy it now price: {{price}}</p>
          </div>
        </center>
      </div>
      <br>
      <ul class='singleform'>
        <li v-for='comment in comments' :key='comment.comment_id'><br>
          <div class='usercommentform'><br>
          <div class="userform">
          <p style="color:white; text-align:left; font-size:40px">{{comment.user_email}} </p>
        </div>
        <br>
          <div class='commentform'>
            <p style="color:white; font-size:35px">{{comment.content}}</p>
          </div><br>
        </div><br>
        </li>
      </ul>
    </div>
    <br>
    <div class='singleform'>
      <p style="color:white; text-align:left; font-size:30px">comment: </p>
      <input type="text" required autocomplete="off" />
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      catid: null,
      name: null,
      color: null,
      hometown: null,
      age: null,
      weight: null,
      breed: null,
      eye: null,
      sex: null,
      rank: null,
      price: null,
      path: null,
      comments: [{
        'comment_id': 1,
        'content': 'helloasdasdffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',
        'user_email': 'abcd',
        'cat_id': 1
      },
      {
        'comment_id': 1,
        'content': 'helloasdasdffffffffffffffffffffffffffffffffffffffff',
        'user_email': 'abcddddd',
        'cat_id': 1
      }
    ],
      username: null
    }
  },
  methods: {
    loadImage (imagePath) {
      return require('../assets/image' + imagePath + '.jpg')
    }
  }
}
</script>
<style>
@import '../../static/css/style.css';
</style>
