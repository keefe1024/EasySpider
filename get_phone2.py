# -*- coding: utf-8 -*-
# @Time    : 2020-04-10 19:18
# @Author  : Keefe
# @FileName: get_phone2.py
# @Software: PyCharm
# @Blog    ：http://www.aiyuanzhen.com/
'''
爬取某接码平台网站的手机号
'''
import requests
from lxml import etree

def write_txt(phone_list):
    with open('phone.txt', 'a+') as a:
        for i in range(len(phone_list)):
            print(phone_list[i])
            a.write('{:}\n'.format(phone_list[i]))
        a.close()


def get_phone(url,headers,cookies):
    # 发送get请求
    response = requests.get(url, cookies=cookies, headers=headers).text
    # 获取解析结果
    tree = etree.HTML(response)
    phone_list = tree.xpath('.//p[@class="layuiadmin-big-font card-phone"]//@id')
    print(phone_list)
    write_txt(phone_list)

def get_more_pages(start,end):
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Referer':'https://www.yinsiduanxin.com/china-phone-number/verification-code-16732046739.html'
    }
    cookies = {'__atuvc': '2%7C15', '__atuvs': '5e9025794eaf8376001', 'Hm_lvt_d996097358a29488805c055065a932cb': '1586505082', 'Hm_lpvt_d996097358a29488805c055065a932cb': '1586505268', '_ga': 'GA1.2.744251253.1586505083', '_gid': 'GA1.2.1119968756.1586505083', '__gads': 'ID=7867e4d06182da4a:T=1586505085:S=ALNI_MYC60-R53Ta_fM_KaMu2xYD3yu0Aw', '_gat_gtag_UA_148166685_3': '1'}
    for i in range(start,end):
        url = 'https://www.yinsiduanxin.com/china-phone-number/page/'+str(i)
        get_phone(url,headers,cookies)

def main():
    get_more_pages(1,47)

if __name__ == '__main__':
    main()

