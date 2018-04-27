import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  add_comment (cred, cb) {
    axios.post(API + '/comments', cred).then((res) => {
      cb(res.data)
    })
  }
}
