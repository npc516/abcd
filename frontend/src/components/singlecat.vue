<template>
  <div class='formta' v-if='cat !== null'>
    <img style='width:550px; height:500px; ' :src="loadImage(cat.photo_path)">
    <br><br>
    <div id="trainer">
      <div class='singleform'>
        <center>
          <div style="display:inline; width:30; float:left; margin-right: 50px; text-align:center">
          </div>
          <div style=" text-align:left; display:inline; width:60px float:left">
            <p class='c'>Cat id: {{cat.cat_id}}</p>
            <p class='c'>Cat name: {{cat.name}}</p>
            <p class='c'>Color: {{cat.color}}</p>
            <p class='c'>Hometown: {{cat.hometown}}</p>
            <p class='c'>Age: {{cat.age}}</p>
            <p class='c'>Weight: {{cat.weight}}</p>
            <p class='c'>Breed: {{cat.breed}}</p>
            <p class='c'>Eye color: {{cat.eye_color}} </p>
            <p class='c'>Sex: {{cat.sex}}</p>
            <p v-if='cat.ranking !== null' class='c'>Ranking: {{cat.ranking}}</p>
            <p v-if='cat.buy_it_now !== null' class='c'>Buy it now price: {{cat.buy_it_now}}</p>
          </div>
        </center>
      </div><br>
      <div class='singleform'>
        <p style="color:white; text-align:left; font-size:30px">Bid Increment: </p>
        <input v-model='new_comment' required autocomplete="off" /><br>
        <p style="color:white; text-align:left; font-size:30px">Start Price: </p>
        <input v-model='new_comment' required autocomplete="off" /><br>
        <p style="color:white; text-align:left; font-size:30px">Start Date: </p>
        <input v-model='new_comment' required autocomplete="off" /><br>
        <p style="color:white; text-align:left; font-size:30px">Duration: </p>
        <input v-model='new_comment' required autocomplete="off" /><br><br>
        <button class='button button-block' v-on:click='submit()'>Start Auction</button>
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

    <br>
    <div class='singleform'>
      <p style="color:white; text-align:left; font-size:30px">Comment: </p>
      <textarea v-model='new_comment' required autocomplete="off" />
        <br>
        <button class='button button-block' v-on:click='submit()'>Submit</button>
    </div>
  </div>
</template>
<script>
import Cat from '../scripts/cat.js'
import Comment from '../scripts/comment.js'
import Auth from '../scripts/auth.js'
export default {
  data () {
    return {
      cat: null,
      comments: null,
      new_comment: null
    }
  },
  methods: {
    loadImage (imagePath) {
      return require('../assets/image/' + imagePath + '.jpg')
    },
    submit () {
      Comment.add_comment({'content': this.new_comment, 'cat_id': this.$route.params.cat_id, 'user_email': Auth.current_user()}, (res) => {})
      Cat.get_comments({'cat_id': this.$route.params.cat_id}, (res) => {
        this.comments = res
      })
    }
  },
  mounted: function () {
    Cat.get_cat({'cat_id': this.$route.params.cat_id}, (res) => {
      this.cat = res
    })
    Cat.get_comments({'cat_id': this.$route.params.cat_id}, (res) => {
      this.comments = res
    })
  }
}
</script>
<style scoped>
@import '../../static/css/style.css';

.c {
  color: white;
  text-align: left;
  font-size: 30px;
}

</style>
