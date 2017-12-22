#coding=utf-8
import re
import requests
import time

url = 'https://s.taobao.com/search'
payload = {'q': 'python','s': '1','ie':'utf8'}  #字典传递url参数    
file = open('taobao_test.txt','w')
s = requests.session()
s.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 100
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
#http://www.xicidaili.com/nn/ 从这个网站可以获取代理IP地址，防止被taobao封禁
proxies = {'https':'https://14.221.165.43:9797',
            'https':'https://110.73.52.16:8123',
            'https':'https://122.72.18.35:80',
            'http':'http://218.106.98.166:53281',
            'http':'http://61.155.164.109:3128',
            'http':'http://61.135.217.7:80',
            'http':'http://125.46.0.62:53281',
            'http':'http://60.191.134.165:9999',
            'http':'http://118.187.58.34:53281',
            'http':'http://61.155.164.110:3128',
            'http':'http://101.247.67.9:53281',
            'http':'http://115.183.11.158:9999',
            'http':'http://171.37.170.124:8123',
            'http':'http://27.46.42.13:9797',
            'http':'http://221.214.214.144:53281'}

for k in range(0,1):        #100次，就是100个页的商品数据
    x=0
    while (x==0):
        try:
            print('call sleep')
            time.sleep(5)  #sleep 5s 延时 ，防止频繁访问被封禁
            print('sleep end')

            payload ['s'] = 44*k+1   #此处改变的url参数为s，s为1时第一页，s为45是第二页，89时第三页以此类推                          
            resp = requests.get(url, params = payload,headers=headers,proxies = proxies) #
            print(resp.url)          #打印访问的网址
            resp.encoding = 'utf-8'  #设置编码
            title = re.findall(r'"raw_title":"([^"]+)"',resp.text,re.I)  #正则保存所有raw_title的内容，这个是书名，下面是价格，地址
            price = re.findall(r'"view_price":"([^"]+)"',resp.text,re.I)    
            loc = re.findall(r'"item_loc":"([^"]+)"',resp.text,re.I)
            paynum=re.findall(r'"view_sales":"([^"]+)"',resp.text,re.I)
            x = len(title)           #每一页商品的数量
        
            resp.close
        except:
            print("error")
            continue
    for i in range(0,x) :    #把列表的数据保存到文件中
        file.write(str(k*44+i+1)+'书名：'+title[i]+'\n'+'价格：'+price[i]+'\n'+'地址：'+loc[i]+'\n'+'已付款：'+paynum[i]+'\n\n')
     
file.close()