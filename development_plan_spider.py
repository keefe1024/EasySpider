# -*- coding: utf-8 -*-
# @Time    : 2020-04-08 5:13
# @Author  : Keefe
# @FileName: development_plan_spider.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
信安之路小白成长计划爬虫
'''
import requests
from lxml import etree


def write_txt(name_list, content):
    with open('E:/py/信安之路小白成长计划/'+name_list+'.txt', 'wb') as a:
        a.write(content)
        a.close()

def get_content(url,headers,cookies,n):
    # 发送get请求
    response = requests.get(url, cookies=cookies, headers=headers).text
    # 获取解析结果
    tree = etree.HTML(response)
    name_list = tree.xpath('.//div[@class="panel-lead"]/h3/text()')
    content = tree.xpath('.//div[@class="panel-lead"]/div//text()')
    write_txt(str(n)+'.'+''.join(name_list),''.join(content).encode('utf-8'))



def main():
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Referer':'http://www.myh0st.cn/user/task/index/taskid/1.html?ref=addtabs'
    }
    cookies = {'PHPSESSID': 'XXX', 'HTTP_TOKEN': 'XXX'}
    # 设置url
    # 从1开始循环
    n = 53
    for i in range(1,n):
        url = "http://www.myh0st.cn/user/task/index/taskid/"+str(i)+".html?ref=addtabs"
        get_content(url,headers,cookies,i)

if __name__ == '__main__':
   main()