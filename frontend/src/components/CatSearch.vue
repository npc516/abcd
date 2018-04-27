<template>
  <div class='form'>
    <div id="catSearch">
      <h1> {{ smsg }} </h1>
      <p style="position:relative; top:-20px">(at least enter one)</p>

      <div class="top-row">
        <div class="field-wrap">
          <label v-bind:class='{active: cat_name!=="" && cat_name!==null, highlight: cat_name!=="" && cat_name!==null}'>
            Cat Name<span class="req"></span>
          </label>
          <input type="text" v-model='cat_name' autocomplete="off" />
        </div>

        <div class="field-wrap">
          <label v-bind:class='{active: cat_id!=="" && cat_id!==null, highlight: cat_id!=="" && cat_id!==null}'>
            Cat Id<span class="req"></span>
          </label>
          <input type="text" v-model='cat_id' autocomplete="off"/>
        </div>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: breed!=="" && breed!==null, highlight: breed!=="" && breed!==null}'>
          Breed<span class="req"></span>
        </label>
        <input type="text" v-model='breed' autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: color!=="" && color!==null, highlight: color!=="" && color!==null}'>
          Color<span class="req"></span>
        </label>
        <input type="text" v-model='color' autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: weight!=="" && weight!==null, highlight: weight!=="" && weight!==null}'>
          Weight<span class="req"></span>
        </label>
        <input type="text" v-model='weight' autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: age!=="" && age!==null, highlight: age!=="" && age!==null}'>
          Age<span class="req"></span>
        </label>
        <input type="text" v-model='age' autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: eye_color!=="" && eye_color!==null, highlight: eye_color!=="" && eye_color!==null}'>
          Eye Color<span class="req"></span>
        </label>
        <input type="text" v-model='eye_color' autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <label v-bind:class='{active: hometown!=="" && hometown!==null, highlight: hometown!=="" && hometown!==null}'>
          Hometown<span class="req"></span>
        </label>
        <input type="text" v-model='hometown' autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <label v-bind:class='{active: sex!=="" && sex!==null, highlight: sex!=="" && sex!==null}'>
          Sex<span class="req"></span>
        </label>
        <input type="text" v-model='sex' autocomplete="off"/>
      </div>

      <button class="button button-block" v-on:click='catSearch()'>Search</button>

    </div>
    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
import Cat from '../scripts/cat.js'
import Router from '../router/index.js'
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
      smsg: 'Please enter Searching criteria'
    }
  },
  methods: {
    catSearch () {
      Cat.catSearch({
        name: this.cat_name,
        cat_id: this.cat_id,
        color: this.color,
        breed: this.breed,
        age: this.age,
        weight: this.weight,
        eye_color: this.eye_color,
        hometown: this.hometown,
        sex: this.sex
      }, (res) => {
        Router.push({name: 'SearchResult', params: {cats: res}})
      })
    }
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
