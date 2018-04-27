import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  get_high_bid (cred, cb) {
    axios.get(API + '/bids/' + cred['cat_id']).then((res) => {
      cb(res.data)
    })
  },

  bid (cred, cb) {
    axios.post(API + '/bids', cred).then((res) => {
      cb(res.data)
    })
  }
}
