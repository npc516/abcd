<template>
  <div class='form'>
    <div id="signup">   
      <h1>Sign Up for Free</h1>

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
          <input type="text" v-model='last_name'required autocomplete="off"/>
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

      <button type="submit" class="button button-block">Get Started</button>

    </div>
  </div>
</template>

<script>
import Auth from '../scripts/auth'
export default {
  name: 'SignUp',
  data () {
    return {
      msg: null,
      email: null,
      first_name: null,
      last_name: null,
      password: null,
      bank_account: null,
      phone: null,
      address: null
    }
  },
  methods: {
    sign_up () {
      this.msg = null
      Auth.sign_up({
        email: this.email,
        name: this.first_name + ' ' + this.last_name,
        password: this.password,
        bank_account: this.bank_account,
        phone: this.phone,
        address: this.address
      }, (err, data) => {
        if (data.status && err == null) {
          this.msg = 'Sign up successful!'
        } else {
          this.msg = 'Sign up failed!'
        }
      })
    }
  }
}
</script>

<style>
@import '../assets/style.css';
</style>
