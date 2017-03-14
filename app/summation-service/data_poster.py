import urllib2, urllib
import json
import base64

username='jake'
password='python'

def cleanData(dict):
    return dict['content'].encode('utf8')


for i in range(17, 18):
    print 'posting article ', i
    with open('resources/articles/article' + str(i) + '.json') as json_data:
        d = json.load(json_data)

        url = 'http://localhost:6200/process'

        d['content'] = cleanData(d)
        data = urllib.urlencode(d)

        print data
        req = urllib2.Request(url, data)
        base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
        req.add_header("Authorization", "Basic %s" % base64string)
        response = urllib2.urlopen(req)
        d = response.read()
        print d
