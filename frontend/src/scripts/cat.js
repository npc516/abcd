import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  upload (cred, cb) {
    var data = {status: false}

    axios.post(API + '/cats', cred).then((res) => {
      if (res.status === 200) {
        localStorage.setItem('token', 'uploaded')
        data.status = true
      }
      cb(null, data)
    }).catch((err) => {
      cb(err, data)
    })
  },
  catSearch (cred, cb) {
    var data = {status: false}

    axios.post(API + '/cats', cred).then((res) => {
      if (res.status === 200) {
        localStorage.setItem('token', 'uploaded')
        data.status = true
      }
      cb(null, data)
    }).catch((err) => {
      cb(err, data)
    })
  }
}
