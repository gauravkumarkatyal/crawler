from bs4 import BeautifulSoup as bs
from requests import session
s=session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
url='https://www.jiomart.com/c/fashion/men/496'

r=s.get(url)
print(r)
soup=bs(r.text,'html.parser')
products=soup.find_all('div','col-md-3 p-0')
for product in products:
    d={}
    name=product.find('span','clsgetname').text
    # price=product.find('span',id='final_price').text
    off=product.find('span','dis_section').text
    url2= product.find('a','category_name prod-name').get('href')
    d_url='https://www.jiomart.com'+url2
    r1=s.get(d_url)
    soup2=bs(r1.text,'html.parser')
    item=soup2.find_all('div','new_product')
    for i in item:
        des=i.find('div','feat_detail').text
        refund=i.find('section',id='return_policy').text
    d={'name':name,'off':off,'des':des,'refund':refund}
    print(d)