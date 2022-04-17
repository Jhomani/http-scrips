import requests
import json

class Fetcher:
  server: str
  headers: dict

  def __init__(self, server:str) -> None:
    self.server = server
    f = open('./token', 'r');
    token = f.readline();
    f.close()

    self.headers = {
      'content-type': 'application/json',
      'authorization': f'Bearer {token}',
    }

  def get(s, url:str, filter = {}):
    stringify = json.dumps(filter)

    params = {
      'filter': stringify
    }

    path = s.server + url;

    fetched = requests.get(
      url=path,
      headers=s.headers,
      params=params
    ) 

    return fetched.json() 

  def post(s, url: str, body: dict):
    path = s.server + url

    fetched = requests.post(
      url=path,
      headers=s.headers,
      data=json.dumps(body)
    ) 
    print(fetched.status_code)

    return fetched.json() 

  def uploadFile(s, url: str, key,  filepath):
    path = s.server + url
    files = {key: open(filepath, 'rb')}

    f = open('./token', 'r');
    token = f.readline();
    f.close()

    headers = {
      'authorization': f'Bearer {token}',
    }

    fetched = requests.post(
      url=path,
      headers=headers,
      files=files
    ) 

    return fetched.json() 

  def put(s, url: str, body: dict):
    path = s.server + url

    fetched = requests.put(
      url=path,
      headers=s.headers,
      data=json.dumps(body)
    ) 

    print(fetched.status_code)

    return fetched.json() 

  def patch(s, url: str, body: dict):
    path = s.server + url

    fetched = requests.patch(
      url=path,
      headers=s.headers,
      data=json.dumps(body)
    ) 

    print(fetched.status_code)

    return fetched.json() 

  def delete(s, url: str):
    path = s.server + url;

    fetched = requests.delete(
      url=path,
      headers=s.headers,
    ) 

    print(fetched.status_code)

    return fetched.json() 
