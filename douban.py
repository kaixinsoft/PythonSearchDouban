#!/usr/bin/python
#coding=utf-8
import urllib2
import re
# 去除数组重复数据的函数
def unique(old_list):
    newList = []
    for x in old_list:
        if x not in newList:
            newList.append(x)
        return newList


# 搜索tag为ios的所有书籍
html = urllib2.urlopen('http://book.douban.com/tag/ios').read()
# 正则表达式得出所有的页数链接
find_booklist = re.compile(r'/tag/ios\?start=\d+&amp;type=T',re.DOTALL)
# 用来寻找所有书名的正则表达式
find_bookName= re.compile(r'http://book.douban.com/subject/\d+/',re.DOTALL)
# 得到所有页数链接
pageListLinkArray = find_booklist.findall(html)
# 去除相同结果
pageListLinkArray2 = unique(pageListLinkArray) 

# 找到当前页的所有书的链接并且去除重复链接
#currentPageBook = find_bookName.findall(currentHtml)
realSite = "http://book.douban.com"+ pageListLinkArray2[0] 
print realSite 
currentHtml = urllib2.urlopen(realSite).read()

bookList = find_bookName.findall(currentHtml)
firstBookLink = bookList[0]
firstBookContent = urllib2.urlopen(firstBookLink).read()
# 创建寻找在读链接的正则表达式
find_doingpeople = re.compile(r'http://book.douban.com/subject/\d+/doings',re.DOTALL)
readedpeoplelink = find_doingpeople.findall(firstBookContent)

print readedpeoplelink 
