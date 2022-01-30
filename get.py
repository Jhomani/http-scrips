import json
from Fetcher import Fetcher

req = Fetcher('http://172.17.0.3:9000')
# req = Fetcher('http://54.176.145.227:8001')

filter = {
  # 'limit': 5,
  # 'module': 'discussion',
  # 'state': 'WAITING',
  # 'complaintType': 'answer',
  'skip': 0,
  # 'order': 'ASC'
  "where": {
    # "enable": False 
    "between":  ['2022-01-10T00:00:00.000Z', '2022-01-29T23:00:00.000Z']
  }
}

# properties = {
#   "userId": '12f2040b-3c32-4680-8f8e-0950bbbfe5ad',
#   "message": "this user is very creasy",
#   "reviewerId": 'c34e42fa-988b-4b96-9c56-4fa206b3647d',
# }
body = {
  "commentId": "13e7e574-cbf6-4c02-8596-7d7615d2137c",
  "userId": "efc8b1bd-36b8-4a49-8ce4-e204bf722d56",
  "type": 'SPAM',
}

#body = {
#      "title": "this i s updated conetnt",
#      "content": "fds fdf  fs fs",
#  }
# LOGIN
# body = {'email': 'master@gmail.com', 'password': 'Test1235'}
# body = {'email': 'thecrack@gmail.com', 'password': 'Test1235'}
# body = {'email': 'josetorres@gmail.com', 'password': 'Test1235'}
# res = req.post('/users/login', body)
# print(json.dumps(res, indent=2));

# f = open('./token', 'w')
# f.write(res['token'])
# f.close()

# res = req.get('/access-controls', filter)
#res = req.delete('/access-controls/3bd7e783-4922-4d07-9384-31419c45f4b4')

# res = req.delete('/announcements/20634f85-b0e6-4794-923e-8da20781a078')
# res = req.get('/announcements/20634f85-b0e6-4794-923e-8da20781a078')

# res = req.post('/users/signup', body)
# res = req.patch('/article/21dc4310-7541-11ec-8821-8b841a0fe331', body)

# res = req.get('/permissions', filter)

# res = req.patch('/access-controls/6692b85c-6cb0-11ec-b8a4-bc5ff47cc136/assign-permissions', body)
#res = req.get('/access-controls')

# ATTAINMENTS
# body = {
#   "title": "this is a patch example",
  # "content": "Carlos fugit magnam. Nulla nesciunt voluptatum explicabo ipsam illum minima modi voluptatum. Dolores autem ut aspernatur vel. Vitae aut ratione molestiae dolores et labore suscipit.",
  # "state": "CREATING"
# }
# res = req.get('/attainments', filter)
# res = req.get('/attainments/69f078fb-5b40-4652-8549-6b5164c76f48', filter)
# res = req.post('/attainments', body)
# res = req.get('/attainments/c369b560-760d-11ec-b79c-cd6a1ac1c111')
# res = req.delete('/attainments/3bd7e783-4922-4d07-9384-31419c45f4b4')

# res = req.get('/announcements/20634f85-b0e6-4794-923e-8da20781a078/proposals/count', filter)

# res = req.post('/users/lock', properties)
# res = req.get('/whoAmI', filter)

# VOTING
# res = req.get('/voting', filter)
# res = req.get('/voting/7f768d79-0369-45ef-aa7c-8278708b5115', filter)
# res = req.get('/voting/4gf4ec50-04a1-04a1-04a1-dfe2fef12c65', filter)

# res = req.post('/complaints', body)

# PROPOSAL 
# res = req.get('/announcements/20634f85-b0e6-4794-923e-8da20781a078/admin-proposals', filter)
# res = req.get('/announcements', filter)

# res = req.get('/complaints/count', filter)
# res = req.get('/landing-page', filter)
# res = req.get('/users/12f2040b-3c32-4680-8f8e-0950bbbfe5ad', filter)

# res = req.get('/announcements/1c0d6660-7bb5-11ec-9504-716dd58e924e/admin-proposals', filter)
# res = req.get('/announcements/e4672dc7-7b89-4335-8dd6-b104f6807e45/admin-proposals', filter)

# announcements/1c0d6660-7bb5-11ec-9504-716dd58e924e/admin-proposals

# res = req.get('/statistics/normatives/c9c2e5ed-bd68-4147-9474-a1715d69ede8', filter)

# res = req.get('/statistics/discussions/39be0e9f-5b07-4a8e-bddb-63fb5acb3c80', filter)

res = req.get('/statistics/voting/1c89061b-5a2e-495f-822d-e1f7fdb45dd1', filter)

# res = req.get('/statistics/announcements/4000b5ac-8ef8-4eee-b0ee-5837a7424179', filter)

# res = req.get('/posts/39085293-0a1a-465f-abd5-2685488d1f14/discussion', filter)

print(json.dumps(res, indent=2));
