<template>
  <div class='form'>
    <div id="signup" v-if='s'>
      <h1> {{ smsg }} </h1>

      <div class="top-row">
        <div class="field-wrap">
          <label v-bind:class='{active: first_name!=="" && first_name!==null, highlight: first_name!=="" && first_name!==null}'>
            First Name<span class="req">*</span>
          </label>
          <input type="text" v-model='first_name' required autocomplete="off" />
        </div>

        <div class="field-wrap">
          <label v-bind:class='{active: last_name!=="" && last_name!==null, highlight: last_name!=="" && last_name!==null}'>
            Last Name<span class="req">*</span>
          </label>
          <input type="text" v-model='last_name' required autocomplete="off"/>
        </div>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: address!=="" && address!==null, highlight: address!=="" && address!==null}'>
          Address<span class="req">*</span>
        </label>
        <input type="address" v-model='address' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: city!=="" && city!==null, highlight: city!=="" && city!==null}'>
          City<span class="req">*</span>
        </label>
        <input type="city" v-model='city' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: state!=="" && state!==null, highlight: state!=="" && state!==null}'>
          State<span class="req">*</span>
        </label>
        <input type="tel" v-model='state' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: zip!=="" && zip!==null, highlight: zip!=="" && zip!==null}'>
          Zip Code<span class="req">*</span>
        </label>
        <input type="text" v-model='zip' required autocomplete="off"/>
      </div>

      <button class="button button-block" v-on:click='sign_up()'>Use this address</button>

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
      email: null,
      first_name: null,
      last_name: null,
      address: null,
      city: null,
      state: null,
      zip: null,
      s: true,
      smsg: 'Please enter your shipping address'
    }
  },
  methods: {
  }
}
</script>

<style>
</style>
