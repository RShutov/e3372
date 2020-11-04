#!/usr/bin/env python

import sys
import pprint
import huaweisms.api.user
import keyring
import getpass
from huaweisms.api.common import (
    post_to_url,
    get_from_url,
    ApiCtx,
)

class HuaweiE3372(object):
  BASE_URL = 'http://{host}'
  XML_APIS = [
    '/api/device/information',
    '/api/device/signal',
    '/api/monitoring/status',
    '/api/monitoring/traffic-statistics',
    '/api/dialup/connection',
    '/api/global/module-switch',
    '/api/net/net-mode',
  ]

  def __init__(self, user, password, host='192.168.8.1'):
    self.host = host
    self.base_url = self.BASE_URL.format(host=host)
    self.ctx = huaweisms.api.user.quick_login(user, password)

  def get(self, url):
    # type: (ApiCtx) -> dict
    req = get_from_url(self.base_url + url, self.ctx)
    return req['response']

def main():
  user = input('Username: ')
  password = getpass.getpass()
  e3372 = HuaweiE3372(user, password)
  for path in e3372.XML_APIS:
    response = e3372.get(path)
    for key,value in response.items():
      print(key, value)

if __name__ == "__main__":
  main()
