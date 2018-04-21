import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  log_in (cred, cb) {
    localStorage.removeItem('token')

    var data = {status: false}

    axios.post(API + '/users/' + cred.email, cred).then((res) => {
      if (res.status === 200) {
        localStorage.setItem('token', 'Logged in')
        data.status = true
      }
      cb(null, data)
    }).catch((err) => {
      cb(err, data)
    })
  },

  sign_up (cred, cb) {
    var data = {status: false}

    axios.post(API + '/users', cred).then((res) => {
      if (res.status === 200) {
        localStorage.setItem('token', 'Logged in')
        data.status = true
      }
      cb(null, data)
    }).catch((err) => {
      cb(err, data)
    })
  }

//todo
  // update_price(cred,cb){

  // }
}
