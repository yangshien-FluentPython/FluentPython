# -*- coding:utf-8 -*-

import json
import redis


number_list = ['1990-12-12', '1888-11-11']
signal = ['1', '-1']

rc = redis.StrictRedis(host='192.168.201.201', port='7307', db=5)
# for i in range(len(number_list)):
value_new = {'host': '192.168.201.203', 'port': 1245, 'user_id': 1888}
value_new = json.dumps(value_new)
rc.publish('c1', value_new)
