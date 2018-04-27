import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  delivery (cred, cb) {
    axios.post(API + '/delivery', cred).then((res) => {
      cb(res.data)
    })
  }
}
