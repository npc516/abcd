import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  log_in (cred, cb) {
    localStorage.removeItem('token')

    var data = {status: false}

    axios.post(API + '/users/' + cred.email, cred).then((res) => {
      if (res.status === 200) {
        localStorage.setItem('token', cred['email'])
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
        localStorage.setItem('token', cred['email'])
        data.status = true
      }
      cb(null, data)
    }).catch((err) => {
      cb(err, data)
    })
  },

  is_logged_in () {
    return localStorage.getItem('token') === null
  },

  current_user () {
    return localStorage.getItem('token')
  },

  // todo
  // update_price(cred,cb){

  // }

  user_cats (cb) {
    axios.get(API + '/users/cats/' + localStorage.getItem('token')).then((res) => {
      cb(res.data)
    })
  }
}
