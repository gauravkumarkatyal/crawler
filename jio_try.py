from bs4 import BeautifulSoup as bs
from requests import session
s=session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
url='https://www.jiomart.com/c/fashion/men/496'
print("dd")
r=s.get(url)
soup=bs(r.text,'html.parser')
products=soup.find_all('div','col-md-3 p-0')
for product in products:
    d={}
    name=product.find('span','clsgetname').text
    d={'name':name}
    # print(d)