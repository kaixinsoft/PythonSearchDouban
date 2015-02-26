#!/usr/bin/python
#coding=utf-8
import urllib2
import re
from BeautifulSoup import BeautifulSoup
import random

user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",

                    ] 

def fetchAllReadUsers(bookNumber, pageNumber):
    bookCollectionURL = 'http://book.douban.com/subject/%s/collections?start=%d' % (bookNumber,pageNumber) 
    #添加随机headers防止被forbidon
    req = urllib2.Request(bookCollectionURL)
    req.add_header('User-Agent', random.choice(user_agents))
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html)
    result = soup.findAll('div', id="collections_tab")
    result2 = result[0]
    result3 = result2.findAll('td',width="80")
    resultCount = len(result3)
    for userlink in result3:
        atag = userlink.find('a')
        link = atag.get('href')
        splitArray = link.split('/')
        userID = splitArray[-2]
        print userID
    if(resultCount>0):
        pageNumber+=20
        fetchAllReadUsers(bookNumber, pageNumber)

def fetchAllBookList(pageNumber):
    bookListURL = 'http://book.douban.com/tag/ios?start=%d&type=T' % pageNumber
    req = urllib2.Request(bookListURL)
    req.add_header('User-Agent', random.choice(user_agents))
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html)
    result = soup.findAll('li', attrs={"class":"subject-item"})
    print len(result)
    for subject in result:
        result3 = subject.findAll('a')
        realAtag = result3[1]
        realbooklink = realAtag.get('href') 
        realbooktitle = realAtag.get('title')
        splitArray = realbooklink.split('/')
        bookNumber = splitArray[-2]
#        print bookNumber
#        print realbooktitle
        
        fetchAllReadUsers(bookNumber,0)
    if(len(result)>0):
        print pageNumber
        pageNumber+=20
        fetchAllBookList(pageNumber)
                 
fetchAllBookList(0)
