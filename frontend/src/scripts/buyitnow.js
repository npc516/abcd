import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  buy_it_now (cred, cb) {
    axios.post(API + '/buyitnow', cred).then((res) => {
      cb(res.data)
    })
  }
}
