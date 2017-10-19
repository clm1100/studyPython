import urllib2
file = urllib2.urlopen('http://www.baidu.com')
message = file.read()
print message