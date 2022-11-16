import requests
import pandas as pd
from requests import session
from bs4 import BeautifulSoup as bs
urls=[]
all_product=[]
s=session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
def crawl_listpage(p1,a,page):
    p1='https://www.next.co.uk/shop/gender-women-productaffiliation-swimwear/category-coverups?p={}#271.6833190917969'
    a=113
    page=int(a/12)
    for j in range(1,page+1):
        url=p1.format(j)

        r=s.get(url)
        soup=bs(r.text,'html.parser')
        pro= soup.find_all('div','produc2 produc1 components__TileCard-eziadi-0 jtGitx produc5')
        for i in pro:
            name=i.find('div','produc33 components__TileCardContent-eziadi-1 gFiots').find('h2').find('a').get('data-desc')
            mrp=i.find('a','produc40 produc34 produc36 components__LinkInlineBlock-sc-1l4gzfe-10 jjsGut produc49 produc63').find('span').text
            p_url=soup.find('a','produc40 produc34 produc36 components__LinkInlineBlock-sc-1l4gzfe-10 jjsGut produc49 produc63').get('href')
            urls.append({'name':name,'mrp':mrp,'url':p_url})
def crawl_detailpage(row):            
            r1=s.get(row.get('url'))
            soup2=bs(r1.text,'html.parser')
            imgurl=[]
            item=soup2.find('section',id='ProductViewer1').find('div','ThumbNailNavClip').find_all('li')
            for k in item:
                img=k.get('data-url')
                imgurl.append(img)

        
            d={'name':row.get('name'),'mrp':row.get('mrp'),'url':row.get('url'),'img':'|'.join(imgurl)}
            all_product.append(d)
            print(d)
p1='https://www.next.co.uk/shop/gender-women-productaffiliation-swimwear/category-coverups?p={}#271.6833190917969'
a=113
page=int(a/12)
urls = []
all_product=[]
crawl_listpage(p1, a, page)
for row in urls:
    crawl_detailpage(row)
