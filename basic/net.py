#encoding=utf-8
import urllib2
for line in urllib2.urlopen("http://www.atguigu.com/download.shtml#oracle"):
    print line
