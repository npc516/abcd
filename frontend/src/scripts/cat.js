import axios from 'axios'

var API = 'http://localhost:5000/api'

export default {
  upload (cred, cb) {
    var data = {status: false}

    axios.post(API + '/cats', cred).then((res) => {
      if (res.status === 201) {
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
        data.status = true
      }
      cb(null, data)
    }).catch((err) => {
      cb(err, data)
    })
  },

  get_all_cat (cb) {
    axios.get(API + '/cats').then((res) => {
      cb(res.data)
    })
  },

  count_all_cat (cb) {
    axios.get(API + '/cats').then((res) => {
      cb(res.data.length)
    })
  },

  get_cat (cred, cb) {
    axios.get(API + '/cats/' + cred['cat_id']).then((res) => {
      cb(res.data)
    })
  },

  get_comments (cred, cb) {
    axios.get(API + '/cats/comments/' + cred['cat_id']).then((res) => {
      cb(res.data)
    })
  }
}
