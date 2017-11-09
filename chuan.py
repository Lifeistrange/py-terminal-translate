#!/usr/bin/env python
#-*- coding=utf-8 -*-

import sys
import json
import random
import hashlib

import requests

def get_sign(appKey, q, salt, appSecret):

    return 

if __name__ == '__main__':
    text = sys.argv[1]

    from_lang = 'auto'
    to_lang = 'zh-CHS'
    appKey = ''
    appSecret = ''

    salt = int(random.random() * 100000000)

    sign = hashlib.md5(appKey + text + str(salt) + appSecret).hexdigest().upper()

    data = {'q': text,
            'from': from_lang,
            'to': to_lang,
            'appKey': appKey,
            'salt': salt,
            'sign': sign}

    resp = requests.post('http://openapi.youdao.com/api', data=data)
    result = json.loads(resp.content)
    print text+',',','.join(result['translation'])
    print ''
    for i in result['basic']['explains']:
        print '     '+i
