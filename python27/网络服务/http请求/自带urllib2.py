# -*- coding: UTF-8 -*-
#python自带库urllib2使用的比较多，简单使用如下
#简单的get请求
import urllib2
url='http://localhost:8080/jenkins/api/json?pretty=ture'
response = urllib2.urlopen(url)
print response.read()

#简单的post请求
import urllib2
import urllib
post_data = urllib.urlencode({})
response = urllib2.urlopen('http://localhost:8080/', post_data)
print response.read()
print response.getheaders()