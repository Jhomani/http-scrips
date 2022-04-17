import json
from Fetcher import Fetcher

# req = Fetcher('http://localhost:9000')
# req = Fetcher('https://9sdn09p4e8.execute-api.us-east-1.amazonaws.com/dev/')
key_server = ' AAAAa07TFHs:APA91bGAfxbwa0M0_Q9QFvufAk5hCAb5jc8xAlRQBR5YlmdMjG48zBDBhqSFd5b0l2JZoFJCLhsmwtVy2E3edvjHjQY58BDyFmzFz5_jqKF34RT_2Vo-O__0oqmiR0kVON8qEGNh7mfD'

req = Fetcher('https://fcm.googleapis.com')
# req = Fetcher('https://backalcaldia.blockchainconsultora.com')

filtery = {
  # limit: 1,
  # "where": {
    # "enable": False 
    # "between":  ['2022-01-30T00:00:00.000Z', '2022-02-05T23:00:00.000Z']
  # }
}

# body = {
#   'email': 'jhomanidev@gmail.com',
#   'password': 'Test1235',
#   'name': 'Juan Carlos',
#   'avatar': 'https://i.imgur.com/PMTZXgc.png',
# }

body = {
  "ci": "3232",
  "expedido": "LPZ",
  "nombres": "jj",
  "paterno": "jj",
  "materno": "jj",
  "telefono": "5353",
  "movil": "0",
  "correo": "jhomanidev@gmail.com",
  "sistema": 'WEB_FORO',
}

usuario = {
  'usuario': '5970947',
  'clave': '6952'
}
token = 'dFPeadvYT36OT_69vLfkgz:APA91bHOUOZx1lrnQOte82YPh231piVSW8VoXI9CRcOOle8K4MrK9PY-vo6dd5rwsWk7k0RxVjqetnerCRGQxtA34_FlShyeuJTVCUKY2O-znqhObW7duySzzS52mySQnQWIeO5W6hhQ'

body = { 
  "message": {
    # "topic": "news",
    "token": token,
    "notification": {
      "title": "Breaking News",
      "body": "New news story available."
    },
    "android":{
      "notification":{
        "icon":"stock_ticker_update",
        "click_action":"news_intent",
        "color":"#7e55c3"
      }
     }
  }
}

res = req.post('/v1/projects/portfolio-490c0/messages:send', body)

print(json.dumps(res, indent=2))


# LOGIN
# body = {'email': 'josetorres@gmail.com', 'password': 'Test1235'}
# res = req.get('/voting/72288b76-8c62-4348-8368-9db96007b0d2?userId=ebcfa943-b173-465d-af7b-54f9b5149963&filter={}')
# res = req.get('/voting/72288b76-8c62-4348-8368-9db96007b0d2')
# res = req.post('/vote/072b262f-a7bc-49f3-9518-d44c1d36eba8', {})


# f = open('./token', 'w')
# f.write(res['token'])
# f.close()

# res = req.get('/whoAmI')

# res = req.get('/verify-hash/432ba3e613a73f9f1d4a2bfa2cdb19667a429a4a089ebf7c54a4c4805e3e1d8a')
# res = req.post('/.gov/wsPC/crearCiudadano', body)
# res = req.post('/users/signup', body)
# res = req.get('/region-prices/c43070e7-c41a-404b-9ef0-ffe1b153ccef')
# res = req.patch('/region-prices/c43070e7-c41a-404b-9ef0-ffe1b153ccef', body)
# res = req.patch('/region-prices/c43070e7-c41a-404b-9ef0-ffe1b153ccef/prices', price)
# res = req.delete('/region-prices/c43070e7-c41a-404b-9ef0-ffe1b153ccef/prices/0')
# res = req.delete('/region-prices/8c390ae0-ac14-4777-9c40-268e5d34b453')

# price = {
#   'redirect': "http://seguros.intercitytours.com/pay-page/pay",
#   'userData': {
#     'address': "dsdsds",
#     'birthdate': 329886000000,
#     'city': "dsd",
#     'email': "jhomanideveloper@gmail.com",
#     'firstName': "dasdad",
#     'gender': True,
#     'nationality': "Armenia-AM",
#     'phone': "+5132323",
#     'postalcode': "0",
#   },
#   'payData': {
#     'arriveDate': 1674855857000,
#     'cost': 249,
#     'days': "300",
#     'endSend': 1674769457000,
#     'startDate': 1648935857000,
#     'startSend': 1648935857000,
#   }
# }


# print(json.dumps(res, indent=2));
