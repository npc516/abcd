import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  create_auction (cred, cb) {
    axios.post(API + '/auctions', cred).then((res) => {
      cb(res.data)
    })
  }
}
