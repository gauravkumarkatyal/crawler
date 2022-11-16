import requests
from requests import session
s=session()
from bs4 import BeautifulSoup as bs
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
url='https://www.21faves.com/collections/swimwear?sort_by=best-selling&gclid=CjwKCAiAjs2bBhACEiwALTBWZUHQgxw79IPFlan_VzxVD8gwFjNts6kn0jEvLOhwpjfmuNcSoIDlGBoCm5QQAvD_BwE'
r=s.get(url)
soup=bs(r.text,'html.parser')
pro=soup.find_all('div','product-snippet')
for i in pro:
    name=i.find('a','product-snippet__title-normal two_line_text_truncate dj_skin_product_list_title').text
    mrp=i.find('span','text-truncate dj_skin_product_price money').text
    url=i.find('a','product-snippet__title-normal two_line_text_truncate dj_skin_product_list_title').get('href')
    p_url='https://www.21faves.com'+url
    r2=s.get(p_url)
    soup2=bs(r2.text,'html.parser')
    pro2=soup2.find_all('div','product-image__thumbs')
    for j in pro2:
        
        d={'price':price}
       
        print(d)