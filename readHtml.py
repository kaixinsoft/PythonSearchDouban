#coding=utf-8
import urllib2

def getHtml(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

html = getHtml("http://tieba.baidu.com")

print html

