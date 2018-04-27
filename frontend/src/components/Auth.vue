<template>
  <div class='form'>
    <ul class="tab-group">
      <li class="tab" v-bind:class='{active:s}'><a href="#signup" v-on:click='s=true'>Sign Up</a></li>
      <li class="tab" v-bind:class='{active:!s}'><a href="#login" v-on:click='s=false'>Log In</a></li>
    </ul>
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
        <label v-bind:class='{active: email!=="" && email!==null, highlight: email!=="" && email!==null}'>
          Email Address<span class="req">*</span>
        </label>
        <input type="email" v-model='email' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: password!=="" && password!==null, highlight: password!=="" && password!==null}'>
          Set A Password<span class="req">*</span>
        </label>
        <input type="password" v-model='password' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: phone!=="" && phone!==null, highlight: phone!=="" && phone!==null}'>
          Phone Number<span class="req">*</span>
        </label>
        <input type="tel" v-model='phone' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: bank_account!=="" && bank_account!==null, highlight: bank_account!=="" && bank_account!==null}'>
          Bank Account<span class="req">*</span>
        </label>
        <input type="text" v-model='bank_account' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: address!=="" && address!==null, highlight: address!=="" && address!==null}'>
          Address<span class="req">*</span>
        </label>
        <input type="text" v-model='address' required autocomplete="off"/>
      </div>

      <button class="button button-block" v-on:click='sign_up()'>Get Started</button>

    </div>
    <div id="login" v-if='!s'>
      <h1> {{ lmsg }} </h1>

      <div class="field-wrap">
        <label v-bind:class='{active: login_email!=="" && login_email!==null, highlight: login_email!=="" && login_email!==null}'>
          Email Address<span class="req">*</span>
        </label>
        <input type="email" v-model='login_email' required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label v-bind:class='{active: login_password!=="" && login_password!==null, highlight: login_password!=="" && login_password!==null}'>
          Password<span class="req">*</span>
        </label>
        <input type="password" v-model='login_password' required autocomplete="off"/>
      </div>

      <button class="button button-block" v-on:click='log_in()'>Log In</button>
    </div>
    <img style="position:absolute; top:150px; left:980px; width:800px" src="../assets/image/icon.png">
  </div>
</template>

<script>
import Auth from '../scripts/auth'
import Router from '../router/index.js'
export default {
  name: 'SignUp',
  data () {
    return {
      email: null,
      first_name: null,
      last_name: null,
      password: null,
      bank_account: null,
      phone: null,
      address: null,
      login_email: null,
      login_password: null,
      s: true,
      smsg: 'Sign up for free!',
      lmsg: 'Welcome back!'
    }
  },
  methods: {
    log_in () {
      Auth.log_in({
        email: this.login_email,
        password: this.login_password
      }, (err, data) => {
        if (data.status && err == null) {
          this.lmsg = 'Log in successful!'
          Router.go()
          Router.push('/MainPage')
        } else {
          this.lmsg = 'Email or password incorrect!'
        }
      })
    },
    sign_up () {
      Auth.sign_up({
        email: this.email,
        name: this.first_name + ' ' + this.last_name,
        password: this.password,
        bank_account: this.bank_account,
        phone: this.phone,
        address: this.address
      }, (err, data) => {
        if (data.status && err == null) {
          this.smsg = 'Sign up successful!'
        } else {
          this.smsg = 'Sign up failed!'
        }
      })
    }
  }
}
</script>

<style>
@import '../../static/css/style.css';
</style>
