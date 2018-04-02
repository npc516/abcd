<template>
  <div class='form'>
    <div id="signup">   
      <h1>Sign Up for Free</h1>

      <div class="top-row">
        <div class="field-wrap">
          <label>
            First Name<span class="req">*</span>
          </label>
          <input type="text" required autocomplete="off" />
        </div>

        <div class="field-wrap">
          <label>
            Last Name<span class="req">*</span>
          </label>
          <input type="text"required autocomplete="off"/>
        </div>
      </div>

      <div class="field-wrap">
        <label>
          Email Address<span class="req">*</span>
        </label>
        <input type="email"required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label>
          Set A Password<span class="req">*</span>
        </label>
        <input type="password"required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label>
          Phone Number<span class="req">*</span>
        </label>
        <input type="tel"required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label>
          Bank Account<span class="req">*</span>
        </label>
        <input type="text"required autocomplete="off"/>
      </div>

      <div class="field-wrap">
        <label>
          Address<span class="req">*</span>
        </label>
        <input type="text"required autocomplete="off"/>
      </div>

      <button type="submit" class="button button-block"/>Get Started</button>

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
      name: null,
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
        name: this.name,
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
