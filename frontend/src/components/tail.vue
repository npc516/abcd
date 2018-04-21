<template>
  <nav>
    <ul>
      <li><router-link to="/4">Insurance</router-link></li>
      <li><router-link to="/3">Sponsors</router-link></li>
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
  position: absolute; bottom: 50px;
}

li{
  display: inline-block;
  margin:0 30px;
}

a{
  color: #194D33;
  text-decoration: none;
  padding: 6px 8px;
  border-radius:10px;

}

.router-link-active{
  background: #eee;
  color: #ff1600;
}
</style>
