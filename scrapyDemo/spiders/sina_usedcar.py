# -*- coding: utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request,FormRequest
from bs4 import BeautifulSoup
import json
import hashlib
import requests


class SinaUsedCarSpider(RedisSpider):
    name = 'sina_usedcar'
    url='http://usedcar.auto.sina.com.cn/buycar/b/%E5%A5%A5%E8%BF%AA'
    usedcar_url='http://usedcar.auto.sina.com.cn/index.php?s=/Api/Usedcar/search'
    datas='limit=12&map=&order=0&page=%d&token=%s'

    def start_requests(self):
        yield Request(self.url,callback=self.get_letter)

    def get_letter(self,response):
        soup=BeautifulSoup(response.body)
        token=soup.find('input',id="token").get('value')
        # page_amount=3
        # for page_num in range(1,page_amount+1):
        #     data=self.datas%(page_num,token)
        #     m = hashlib.md5()
        #     m.update(data)
        #     sign = m.hexdigest()
        #     print token
        #     print sign
        #     form_data={"token":token,"sign":sign,"page":str(page_num),"order":"0","limit":"12","map":""}
        #
        #     yield FormRequest(self.usedcar_url,headers={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.8','Connection':'keep-alive','Content-Length':'163','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'usedcar.auto.sina.com.cn','Origin':'http://usedcar.auto.sina.com.cn','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','X-Requested-With':'XMLHttpRequest'},formdata=form_data,callback=self.get_list)

        data = self.datas % (1, token)
        m = hashlib.md5()
        m.update(data)
        sign = m.hexdigest()
        form_data={"token":token,"sign":sign,"page":"1","order":"0","limit":"12","map":""}
        data_dumps = json.dumps(form_data)
        # r = requests.post(self.usedcar_url, data=data_dumps)
        # print r.text

        # Cookie = response.request.headers.getlist('Cookie')
        yield Request(self.usedcar_url, method='POST', body=data_dumps, callback=self.get_list)


    def get_list(self,response):
        soup=BeautifulSoup(response.body)
        print soup