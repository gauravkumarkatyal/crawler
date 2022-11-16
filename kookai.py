import requests
from bs4 import BeautifulSoup as bs
from requests import session
all_product=[]
s=session()
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.kookai.com.au/',
    'Content-Type': 'application/json',
    'searchspring-session-id': '70ee87f0-21ca-486e-a042-2a3315a7b468',
    'searchspring-user-id': '68ba3ab8-8187-40a4-a345-7c01dfc8b165',
    'searchspring-page-load-id': 'df67b83d-0e1f-41cc-971a-b224b64b570c',
    'Origin': 'https://www.kookai.com.au',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'siteId': 'm93bm6',
    'cart': '',
    'resultsFormat': 'native',
    'resultsPerPage': '48',
    'bgfilter.collection_handle': 'dresses',
    'page': '2',
    }
r=requests.get('https://m93bm6.a.searchspring.io/api/search/search.json', params=params, headers=headers)
js=r.json()
pro=js['results']
for i in pro:
        name=i['name']
        mrp=i['price']
        img=i['image']
        imges=i['images']
        url=i['url']
        d_url='https://www.kookai.com.au'+url
        
        r=s.get(d_url)
        soup=bs(r.text,'html.parser')
        pre=soup.find_all('div','product__header')
        for i in pre:
            size_colour=i.find('div','swatch-size-label').text.split()
            des=i.find('div',id='details').text



        d={'name':name,'mrp':mrp,'img':img,'imges':imges,'size_colour':size_colour,'des':des}
        
        print(d)
