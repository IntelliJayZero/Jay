import requests
from bs4 import BeautifulSoup

def connect_to_web(web_url, Agent='Mozilla/5.0'):
    try:
        r = requests.get(web_url, headers={'user-agent': Agent})
        r.raise_for_status()
        print('start connect'.center(48, '-'))
        print('connect to:' + str(r.request.url))
        print('encoded with:' + str(r.encoding))
        print('connected'.center(48, '-'))
        r.encoding = r.apparent_encoding
        return r
    except:
        print('404!'.center(48, '-'))

def download_resource(web_url, save_path=''):
    import os
    import time
    flag = connect_to_web(web_url)
    print('download start'.center(48, '-'))
    l = len(flag.content)
    k = l//1024
    m = k//1024
    g = m//1024
    print('length:{}GB {}MB {}KB {}B'.format(g%1024, m%1024, k%1024, l%1024))
    domain = web_url.split('/')
    name = domain[-1]
    if not save_path:
        p = name
        print('save to:' + os.getcwd() + '\\' + name)
    else:
        if not os.path.isdir(save_path):
            return 'NO PATH!!'
        p = save_path + '\\' + name
        print('save to:' + p)
    with open(p, 'wb') as f:
        f.write(flag.content)
    print('downloaded!'.center(48, '-'))
    print('')

def format_html(html_text):
    a_soap = BeautifulSoup(html_text, 'html.parser')
    return a_soap.prettify()