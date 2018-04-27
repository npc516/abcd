<template>
  <nav>
    <ul>
      <li><router-link to="/MainPage" exact>UCC</router-link></li>
      <li><router-link to="/Match" exact>Tournament</router-link></li>
      <li><router-link to="/Cat" exact>All Cat</router-link></li>
      <li><router-link to="/AddCat" exact>Add a Cat</router-link></li>
      <li><router-link to="/CatSearch" exact>Cat Search</router-link></li>
      <li><router-link to="/Insurance">Insurance</router-link></li>
      <li><router-link to="/Sponsorship">Sponsors</router-link></li>
      <li><router-link to="/mycat"  exact>My cat</router-link></li>
      <li><router-link to="/auth"  exact>Sign Up/Log In</router-link></li>

    </ul>
  </nav>
</template>

<script>

export default{}

</script>

<style scoped>
ul{
  list-style-type:none;
  text-align:left;
  font-Size: 100;
  margin:0;
}

li{
  display: inline-block;
  margin:0 30px;
}

a{
  color: #fff;
  text-decoration: none;
  padding: 6px 8px;
  border-radius:10px;
}

nav{
  background: #444;
  padding: 14px 0;
  margin-bottom:40px;
}

.router-link-active{
  background: #eee;
  color: #ff1600;
}
</style>
