<template>
  <div class='form'>
    <div id="signup" v-if='s'>
      <h1> {{ smsg }} </h1>

      <div class="top-row">
        <div class="field-wrap">
          <label v-bind:class='{active: cat_name!=="" && cat_name!==null, highlight: cat_name!=="" && cat_name!==null}'>
            Cat Name<span class="req">*</span>
          </label>
          <input type="text" v-model='cat_name' required autocomplete="off" />
        </div>

        <div class="field-wrap">
          <label v-bind:class='{active: cat_id!=="" && cat_id!==null, highlight: cat_id!=="" && cat_id!==null}'>
            Cat Id<span class="req">*</span>
          </label>
          <input type="text" v-model='cat_id' required autocomplete="off"/>
        </div>
      </div>

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

      <button class="button button-block" v-on:click='sign_up()'>Search</button>

    </div>
    <div id="login" v-if='!s'>
      <h1> {{ lmsg }} </h1>

      <button class="button button-block" v-on:click='log_in()'>Log In</button>
    </div>
    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
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
      s: true,
      smsg: 'Please enter Searching information'
    }
  },
  methods: {
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
