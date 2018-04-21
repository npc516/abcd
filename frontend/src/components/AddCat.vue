<template>
  <div class="AddCat">
    <input type="file" @change="onFileSelected">
    <button @click="onUpload">Upload</button>
  </div>
</template>

<script>

import axios from 'axios'
export default {
  name: 'AddCat',
  data () {
    return {
      selectedFile: null
    }
  },
  methods: {
    onFileSelected (event) {
      this.selectedFile = event.target.files[0]
    },
    onUpload () {
      const fd = new FormData()
      fd.append('image', this.selectedFile, this.selectedFile.name)
      axios.post('', fd)
        .then(res => {
          console.log(res)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
