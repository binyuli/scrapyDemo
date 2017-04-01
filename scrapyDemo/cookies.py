# encoding=utf-8
import requests
import logging

"""
选择多个汽车之家账号
"""
myAutohome = [
    {'no': 'pqlaowksiejd', 'psw': '1adbb3178591fd5bb0c248518f39bf6d'},
    {'no': 'sxgx109', 'psw': '1c1808e5d1503926b9c85a8ecf2b57a6'},
]
logging.basicConfig(filename='logger.log', level=logging.INFO)

def getCookies(autohome):
    """ 获取Cookies """
    cookieslist = list()
    url_login = 'http://account.autohome.com.cn/Login/ValidIndex'
    for elem in autohome:
        username = elem['no']
        password = elem['psw']
        postData = {
            "name": username,
            "pwd": password,
        }
        session = requests.Session()
        r = session.post(url_login, data=postData)
        data = r.json()
        if data["success"] == 1:
            logging.info("Get Cookie Success!( Account:%s )" % username)
            cookie = session.cookies.get_dict()
            logging.debug(cookie)
            cookieslist.append(cookie)
        else:
            logging.info("Failed!( Reason:%s )" % data['Msg'])
    return cookieslist

cookies = getCookies(myAutohome)
logging.info("Get Cookies Finish!( Num:%d)" % len(cookies))
