<template>
  <div class='login'>
    <div>
      <span><b>Username:</b></span>
      <input v-model='email'>
    </div>
    <br>
    <div>
      <span><b>Password:</b></span>
      <input v-model='password'>
    </div>
    <br>
    <button class='btn btn-primary' v-on:click='login()'>Log In</button>
    <button class='btn btn-primary' v-on:click='logout()'>Log Out</button>
    <h2> {{ msg }} </h2>
  </div>
</template>

<script>
import Auth from '../scripts/auth'
export default {
  name: 'Login',
  data () {
    return {
      msg: null,
      email: null,
      password: null
    }
  },
  methods: {
    login () {
      this.msg = 'Attempting to log in...'
      Auth.login({
        email: this.email,
        password: this.password
      }, (err, data) => {
        if (data.status && err == null) {
          this.$router.replace({name: 'Index'})
        } else {
          this.msg = 'Unable to log in!'
        }
      })
    },
    logout () {
      Auth.logout()
    }
  }
}
</script>

<style>
</style>
