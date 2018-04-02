<template>
  <div class='signup'>
    <div>
      <span><b>Email:</b></span>
      <input v-model='email'>
    </div>
    <br>
    <div>
      <span><b>Name:</b></span>
      <input v-model='name'>
    </div>
    <br>
    <div>
      <span><b>Password:</b></span>
      <input v-model='password'>
    </div>
    <br>
    <div>
      <span><b>Bank Account:</b></span>
      <input v-model='bank_account'>
    </div>
    <br>
    <div>
      <span><b>Phone number:</b></span>
      <input v-model='phone'>
    </div>
    <br>
    <div>
      <span><b>Address:</b></span>
      <input v-model='address'>
    </div>
    <br>
    <button class='btn btn-primary' v-on:click='sign_up()'>Sign Up</button>
    <h2> {{ msg }} </h2>
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
</style>
