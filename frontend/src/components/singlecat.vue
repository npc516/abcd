<template>
  <div class='formta' v-if='cat !== null'>
    <img style='width:550px; height:500px; ' :src="loadImage(cat.photo_path)">
    <br><br>
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
    </div>
    <br>

    <center>
      <div class='form' v-if='cat.owner_email === current_user'>
        <div class="field-wrap">
          <label :class='{active: bid_increment, highlight: bid_increment}'>Bid Increment<span class='req'>*</span></label>
          <input v-model='bid_increment' required autocomplete="off" /><br>
        </div>
        <div class="field-wrap">
          <label :class='{active: start_price, highlight: start_price}'>Start Price<span class='req'>*</span></label>
          <input v-model='start_price' required autocomplete="off" /><br>
        </div>
        <div class="field-wrap">
          <label :class='{active: start_time, highlight: start_time}'>Start Date<span class='req'>*</span></label>
          <input v-model='start_time' required autocomplete="off" /><br>
        </div>
        <div class="field-wrap">
          <label :class='{active: duration, highlight: duration}'>Duration<span class='req'>*</span></label>
          <input v-model='duration' required autocomplete="off" /><br><br>
        </div>
        <button class='button button-block' v-on:click='auction()'>Start Auction</button>
      </div>
    </center>

    <br>
    <ul class='singleform' v-if='comments && comments.length !== 0'>
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
    <br>

    <br>
    <div class='singleform' v-if='current_user'>
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
import Auction from '../scripts/auction.js'
export default {
  data () {
    return {
      cat: null,
      comments: null,
      new_comment: null,
      bid_increment: null,
      start_price: null,
      start_time: null,
      duration: null,
      current_user: null
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
    },
    auction () {
      Auction.create_auction({
        'bid_increment': this.bid_increment,
        'start_price': this.start_price,
        'start_time': this.start_time,
        'duration': this.duration,
        'cat_id': this.cat.cat_id
      }, (res) => {
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
    this.current_user = Auth.current_user()
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
