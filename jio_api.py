# from pickle import APPEND
import requests
import pandas as pd
from requests import session
all_product=[]
s=session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.jiomart.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Referer': 'https://www.jiomart.com/',
    'Connection': 'keep-alive',
}
for i in range(0,8):

    data = '{"requests":[{"indexName":"prod_mart_fashion_products_popularity","params":"ruleContexts=%5B%22PLP%22%5D&query=&filters=category_ids%3A496%20AND%20availability_status%3AA%20AND%20(available_stores%3APANINDIAFASHION)%20AND%20(store_wise_mrp.PANINDIAFASHION.available%3Atrue)%20AND%20(inventory_stores%3AALL%20OR%20inventory_stores%3Afashion_zone%20OR%20inventory_stores%3Ageneral_zone%20OR%20inventory_stores%3A8080%20)&clickAnalytics=true&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page='+str(i)+'&maxValuesPerFacet=50&facets=%5B%22in_stock%22%2C%22category_level.level2%22%2C%22category_level.level4%22%2C%22size%22%2C%22brand%22%2C%22productgroups%22%2C%22colour%22%2C%22fit%22%2C%22fabrictype%22%2C%22pattern%22%2C%22neckline%22%2C%22sleeve%22%2C%22waistrise%22%2C%22distress%22%2C%22sport%22%2C%22sizegroup%22%2C%22style%22%2C%22mood%22%2C%22washcare%22%2C%22dresslength%22%2C%22skirtlength%22%2C%22avg_selling_price%22%2C%22avg_discount_pct%22%5D&tagFilters="}]}'
    response = requests.post('https://3yp0hp3wsh-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.5.1)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=aace3f18430a49e185d2c1111602e4b1&x-algolia-application-id=3YP0HP3WSH', headers=headers, data=data)
    js=response.json()
    pro=js['results'][0]['hits']
    for i in pro:
        name=i['display_name']
        mrp=i['avg_mrp']
        brand=i['brand']
        pro_code=i['product_code']
        img_url=i['image_url']
        d={'name':name,'mrp':mrp,'brand':brand,'pro_code':pro_code,'img_url':img_url}
        all_product.append(d)
        print(d)



        
df=pd.DataFrame(all_product)
df.to_excel('jio_mart.xlsx',index=False)