# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import simplejson as json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import hashlib
import types
import json
import  time
class test:
    def md5(str):
        if type(str) is types.StringType:
            m = hashlib.md5()
            m.update(str)
            return m.hexdigest()
            print """""", m.hexdigest
        else:
            return "ErrorType!"
    key = "&key=037F6F3127604B4FAE8AAD1AE4BE78E3"

    data ={"id":18,"monStart":"2017-07-30 00:00:00"}

    sort_data = sorted(data.items(),key=lambda d:d[0])
    print sort_data
    res = urllib.unquote(urllib.urlencode(sort_data))
    res1 = res.replace("+"," ")
    res2 = res1 +key
    print"MARK MARK MARK--- ", res2, " ---MARK MARK MARK"

    sign = md5(res2).upper()
    print sign
