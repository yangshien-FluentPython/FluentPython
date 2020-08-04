# -*- coding:utf-8 -*-

import json
import redis


rc = redis.StrictRedis(host='192.168.201.201', port='7307', db=5)
ps = rc.pubsub()
ps.subscribe('test')
for item in ps.listen():
    if item['type'] == 'message':
        print item['channel']
        print item['data']
        data = json.loads(item['data'])
        print data
        print data['host'], data['port']

