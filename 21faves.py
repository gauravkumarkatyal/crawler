import requests
import pandas as pd
img=[]
all_product=[]
cookies = {
    'client_id': '1668404176328263',
    '_c_id': '1668404176328711053',
    'store_locale': 'en-US',
    'shoplazza_source': '%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.21faves.com%2Fcollections%2Fswimwear%3Fsort_by%3Dbest-selling%26gclid%3DCj0KCQiAyMKbBhD1ARIsANs7rEEZ3yBJIG7RHGgqq6xsyIHn5vFGgHn6A6j4N0TRYcY5YQQ-TaswCScaArgpEALw_wcB%22%2C%22%24latest_referrer_host%22%3A%22GoogleAds%22%2C%22expire%22%3A1669008976987%7D',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218474a368c41f0-0673b8ca1ca92d8-c535426-921600-18474a368c568d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%2218474a368c41f0-0673b8ca1ca92d8-c535426-921600-18474a368c568d%22%7D',
    '_ga': 'GA1.2.1253511941.1668404178',
    '_gid': 'GA1.2.501323891.1668404178',
    '_gac_UA-83020630-37': '1.1668504480.CjwKCAiAjs2bBhACEiwALTBWZUHQgxw79IPFlan_VzxVD8gwFjNts6kn0jEvLOhwpjfmuNcSoIDlGBoCm5QQAvD_BwE',
    '_identity_cart': '4569283a-ffae-479e-9298-c3dd7bc3046a',
    '_fbp': 'fb.1.1668404179396.910416853',
    '_identity_popups': '46533bc5-6554-422d-ad52-c4e35cd9bfd71668404191',
    '_identity_popups_bundle': 'e29b775a-0406-48d4-b0f3-7ca82dee54611668404191',
    'sw_session': '63735ba1cf5b7',
    '__cf_bm': 'TiG.SpzUzh1gi_I11Q8tc7XRhbVnxm45XShbkpPlJqs-1668504481-0-ARhvq8WOynOpOxCVej7rpLPlXKmAjfcbe87CQrsreHwr1Y+uCG1qUl50wfNcD0dgQW69Zb8z15z7n5P4R3hYsFU=',
    'session_id': '1668504478456452',
    '_pdv': '%5B%7B%22product_id%22%3A%22313e48bc-097d-451b-8e61-f01bc0e1224c%22%2C%22timestamp%22%3A1668504497785%7D%5D',
    '_gat_gtag_UA_83020630_37': '1',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Alt-Used': 'www.21faves.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.21faves.com/collections/one-pieces?spm=..collection_3e5a3368-5c50-460a-9fe1-9794511b89a9.header_1.1',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'client_id=1668404176328263; _c_id=1668404176328711053; store_locale=en-US; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.21faves.com%2Fcollections%2Fswimwear%3Fsort_by%3Dbest-selling%26gclid%3DCj0KCQiAyMKbBhD1ARIsANs7rEEZ3yBJIG7RHGgqq6xsyIHn5vFGgHn6A6j4N0TRYcY5YQQ-TaswCScaArgpEALw_wcB%22%2C%22%24latest_referrer_host%22%3A%22GoogleAds%22%2C%22expire%22%3A1669008976987%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218474a368c41f0-0673b8ca1ca92d8-c535426-921600-18474a368c568d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%2218474a368c41f0-0673b8ca1ca92d8-c535426-921600-18474a368c568d%22%7D; _ga=GA1.2.1253511941.1668404178; _gid=GA1.2.501323891.1668404178; _gac_UA-83020630-37=1.1668504480.CjwKCAiAjs2bBhACEiwALTBWZUHQgxw79IPFlan_VzxVD8gwFjNts6kn0jEvLOhwpjfmuNcSoIDlGBoCm5QQAvD_BwE; _identity_cart=4569283a-ffae-479e-9298-c3dd7bc3046a; _fbp=fb.1.1668404179396.910416853; _identity_popups=46533bc5-6554-422d-ad52-c4e35cd9bfd71668404191; _identity_popups_bundle=e29b775a-0406-48d4-b0f3-7ca82dee54611668404191; sw_session=63735ba1cf5b7; __cf_bm=TiG.SpzUzh1gi_I11Q8tc7XRhbVnxm45XShbkpPlJqs-1668504481-0-ARhvq8WOynOpOxCVej7rpLPlXKmAjfcbe87CQrsreHwr1Y+uCG1qUl50wfNcD0dgQW69Zb8z15z7n5P4R3hYsFU=; session_id=1668504478456452; _pdv=%5B%7B%22product_id%22%3A%22313e48bc-097d-451b-8e61-f01bc0e1224c%22%2C%22timestamp%22%3A1668504497785%7D%5D; _gat_gtag_UA_83020630_37=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'page': '1',
    'sort_by': 'manual',
    'limit': '48',
    'tags': '',
    'price': '',
}
r=requests.get('https://www.21faves.com/api/collections/047142f8-11fe-4923-a58d-17551eb1a1fe/products', params=params, cookies=cookies, headers=headers)

js=r.json()
pro=js['data']['products']
for i in pro:
    name=i['title']
    mrp=i['price']
    d=js['data']['products'][0]
    for i in d:
        url=i['images']['src']
        c_url='https:'+url
        img.append(c_url)
        # w_url=i['url']
        # p_url='https://www.21faves.com/'+w_url
        # r=s.get(p_url)
        print(c_url)

#         d={'name':name,'mrp':mrp,'img':img,'p_url':p_url}   
#         all_product.append(d) 
#     print(d)
# df=pd.DataFrame(all_product)
# df.to_excel('21_faves.xlsx',index=False)
    
    

    
    
    
    

    # print(name)    