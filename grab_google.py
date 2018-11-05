import urllib2
import re
import os

class Spider:

    # 初始化
    def __init__(self):
        self.siteURL = 'http://www.google.com'

    # 把谷歌搜索页面抓下来
    def getPage(self):
        url = self.siteURL
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    # 获取页面上所有链接
    def getLinks(self):
        data = getPage()
        links = re.findall('(?<=href=")[^"]*', data)
        for url in links:
            saveLink(url)
        return contents

    # 保存链接
    def saveLink(self,iconURL,name):
        splitPath = iconURL.split('.')
            fTail = splitPath.pop()
            fileName = name + "/icon." + fTail
            self.saveImg(iconURL,fileName)

#传入起止页码即可
path = 'C'
if not os.path.exists(path):
    os.makedirs(path)
spider = Spider()
