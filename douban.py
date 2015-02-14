#!/usr/bin/python
#coding=utf-8
import urllib2
import re
# 搜索tag为ios的所有书籍
html = urllib2.urlopen('http://book.douban.com/tag/ios').read()
# 正则表达式得出所有的页数链接
find_booklist = re.compile(r'/tag/ios\?start=\d+&amp;type=T',re.DOTALL)
# 用来寻找所有书名的正则表达式
find_bookName= re.compile(r'http://book.douban.com/subject/\d+/',re.DOTALL)
pageListLinkArray = find_booklist.findall(html)
# 去除相同结果
pageListLinkArray2 = set(pageListLinkArray)
print len(pageListLinkArray2)
print pageListLinkArray2 
