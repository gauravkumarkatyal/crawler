from bs4 import BeautifulSoup as bs
import pandas as pd
from requests import session
all_pro=[]
s=session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
url='https://www.jiomart.com/c/homeandkitchen/disposables/8660'

r=s.get(url)
print(r)
soup=bs(r.text,'html.parser')
products=soup.find_all('div','col-md-3 p-0')
for product in products:
    
    name=product.find('span','clsgetname').text
    # price=product.find('span',id='final_price').text
    if product.find('strike',id='price'):
        mrp=product.find('strike',id='price').text
    else:
        'no'    

    # mrp=product.find('strike',id='price').text
    if product.find('span','dis_section'):
        off=product.find('span','dis_section').text
    else: 
        'no'   
    # off=product.find('span','dis_section').text
    url2= product.find('a','category_name prod-name').get('href')
    d_url='https://www.jiomart.com'+url2
    r1=s.get(d_url)
    soup2=bs(r1.text,'html.parser')
    item=soup2.find_all('div','new_product')
    for i in item:
        des=i.find('div','feat_detail').text
           

        # refund=i.find('section',id='return_policy').text
    d={'name':name,'mrp':mrp,'d_url':d_url,'des':des,}
    all_pro.append(d)
    print(d)
df=pd.DataFrame(all_pro)
df.to_excel('jio_mart universal crawler.xlsx')