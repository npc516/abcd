<template>
  <div class='form'>
    <div id="addCat">
      <h1> {{ smsg }} </h1>

      <div class="field-wrap">
        <div class="field-wrap">
          <label v-bind:class='{active: cat_name!=="" && cat_name!==null, highlight: cat_name!=="" && cat_name!==null}'>
            Cat Name<span class="req">*</span>
          </label>
          <input type="text" v-model='cat_name' required autocomplete="off" />
        </div>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: cat_color!=="" && cat_color!==null, highlight: cat_color!=="" && cat_color!==null}'>
          Cat Color<span class="req">*</span>
        </label>
        <input type="cat_color" v-model='cat_color' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: breed!=="" && breed!==null, highlight: breed!=="" && breed!==null}'>
          Breed<span class="req">*</span>
        </label>
        <input type="breed" v-model='breed' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: age!=="" && age!==null, highlight: age!=="" && age!==null}'>
          Age<span class="req">*</span>
        </label>
        <input type="tel" v-model='age' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: weight!=="" && weight!==null, highlight: weight!=="" && weight!==null}'>
          Weight<span class="req">*</span>
        </label>
        <input type="text" v-model='weight' required autocomplete="off"/>
      </div>
      <div class="field-wrap">
        <input type="file" @change="onFileSelected">
      </div>
      <button class="button button-block" v-on:click='upload()'>Upload</button>

    </div>
    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>

</template>

<script>
import Cat from '../scripts/cat.js'
export default {
  name: 'AddCat',
  data () {
    return {
      cat_name: null,
      cat_color: null,
      breed: null,
      age: null,
      weight: null,
      s: true,
      selectedFile: null,
      smsg: 'Please enter information of your cat'
    }
  },
  methods: {
    upload () {
      Cat.upload({
        name: this.cat_name,
        color: this.cat_color,
        breed: this.breed,
        age: this.age,
        weight: this.weight,
        photo_path: this.selectedFile
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
