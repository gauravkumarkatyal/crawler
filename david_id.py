import requests
from requests import session
s=session()
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.davidjones.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.davidjones.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}


r=requests.get('https://api.bazaarvoice.com/data/statistics.json?apiversion=5.4&passkey=caXpIomrCFZkazN7d3kXpyYLVHjz2eoemvbq9l2a0pSl0&stats=Reviews&filter=ContentLocale:en_AU,en*&filter=ProductId:25324861,25274714,25304095,25324863,25274709,25206837,24970589,25304094,24970579,24970659,25206334,24965528,24970669,24965512,24701611,24970629,24701612,24965504,24970639,24970619,24962820,24723473,24701615,24723474,24701614,25304096,25051512,24965520,24723472,24970679,24547772,24406460,23746273', headers=headers)
r.json()
js=r.json()
pro=js['Results'][0]['ProductStatistics']
for i in pro:
    id=i['ProductId']
     
    
    print(id)