# -*- coding:utf-8 -*-
from lxml import etree
import requests
import urllib

__author__ = 'monkey'

# 题目要求：
# 用Pyhton写一个爬图片的程序，爬这个链接里的日本妹子图片
# 地址：http://tieba.baidu.com/p/2166231880

# 获取url地址，对页面进行爬去
def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    picitems = []
    picitems = selector.xpath('//div[@id="post_content_29397251028"]/img[@class="BDE_Image"]')
    print(len(picitems));

    i = 0
    for pic in picitems:
        url = pic.xpath('@src')[0]
        print(url)
        dir = './%d.jpg'%i
        download_Image(url, dir)
        i += 1



def download_Image(url, save_path):
    urllib.request.urlretrieve(url, save_path)


if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/2166231880"
    spider(url)