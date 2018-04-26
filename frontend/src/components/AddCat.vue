<template>
  <div class='form'>
    <div id="addCat">
      <h1> {{ smsg }} </h1>

      <div class="top-row">
        <div class="field-wrap">
          <label v-bind:class='{active: cat_name!=="" && cat_name!==null, highlight: cat_name!=="" && cat_name!==null}'>
            Cat Name<span class="req">*</span>
          </label>
          <input type="text" v-model='cat_name' required autocomplete="off" />
        </div>
      </div>
      <br>
      <br>
      <div class="field-wrap">
        <label v-bind:class='{active: breed!=="" && breed!==null, highlight: breed!=="" && breed!==null}'>
          Breed<span class="req">*</span>
        </label>
        <input type="text" v-model='breed' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: color!=="" && color!==null, highlight: color!=="" && color!==null}'>
          Color<span class="req">*</span>
        </label>
        <input type="text" v-model='color' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: weight!=="" && weight!==null, highlight: weight!=="" && weight!==null}'>
          Weight<span class="req">*</span>
        </label>
        <input type="text" v-model='weight' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: age!=="" && age!==null, highlight: age!=="" && age!==null}'>
          Age<span class="req">*</span>
        </label>
        <input type="text" v-model='age' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: eye_color!=="" && eye_color!==null, highlight: eye_color!=="" && eye_color!==null}'>
          Eye Color<span class="req">*</span>
        </label>
        <input type="text" v-model='eye_color' required autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <label v-bind:class='{active: hometown!=="" && hometown!==null, highlight: hometown!=="" && hometown!==null}'>
          Hometown<span class="req">*</span>
        </label>
        <input type="text" v-model='hometown' required autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <label v-bind:class='{active: sex!=="" && sex!==null, highlight: sex!=="" && sex!==null}'>
          Sex<span class="req">*</span>
        </label>
        <input type="text" v-model='sex' required autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <label v-bind:class='{active: owner_email!=="" && owner_email!==null, highlight: owner_email!=="" && owner_email!==null}'>
          Owner Email<span class="req">*</span>
        </label>
        <input type="text" v-model='owner_email' required autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <label v-bind:class='{active: photo_path!=="" && photo_path!==null, highlight: photo_path!=="" && photo_path!==null}'>
          Photo Path<span class="req">*</span>
        </label>
        <input type="text" v-model='photo_path' required autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <label v-bind:class='{active: buy_it_now!=="" && buy_it_now!==null, highlight: buy_it_now!=="" && buy_it_now!==null}'>
          Buy it now Price<span class="req">*</span>
        </label>
        <input type="text" v-model='buy_it_now' required autocomplete="off"/>
      </div>
      <button class="button button-block" v-on:click='upload()'>Upload</button>

    </div>
    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
import Cat from '../scripts/cat.js'
export default {
  name: 'SignUp',
  data () {
    return {
      cat_name: null,
      cat_id: null,
      weight: null,
      breed: null,
      color: null,
      age: null,
      eye_color: null,
      hometown: null,
      sex: null,
      owner_email: null,
      photo_path: null,
      buy_it_now: null,
      s: true,
      smsg: 'Please enter cat information'
    }
  },
  methods: {
    Upload () {
      Cat.Upload({
        name: this.cat_name,
        color: this.cat_color,
        breed: this.breed,
        age: this.age,
        weight: this.weight,
        photo_path: this.photo_path,
        eye_color: this.eye_color,
        hometown: this.hometown,
        buy_it_now: this.buy_it_now,
        sex: this.sex
      }, (err, data) => {
        if (data.status && err == null) {
          this.smsg = 'Uploaded'
        } else {
          this.smsg = 'Upload fail'
        }
      })
    }
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
