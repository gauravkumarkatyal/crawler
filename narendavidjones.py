import requests
from bs4 import BeautifulSoup as bs
from requests import session
s=session()
cookies = {
    'visid_incap_1686039': '5lEDO1YJS/iMNWQdUsm+DEKRY2MAAAAAQ0IPAAAAAACAyBOoAWfUnKw7nylA2ClX4/Z3TOS3pmUq',
    '_gcl_au': '1.1.288583075.1667469636',
    '_ga_2LJLJKYZ3R': 'GS1.1.1667971126.13.1.1667971774.0.0.0',
    '_ga': 'GA1.2.588194849.1667469636',
    '_ga_7ZEZ2L98N2': 'GS1.1.1667971127.13.1.1667971774.58.0.0',
    'BVBRANDID': '93dffa88-0b74-4571-9ab8-fa832bfa9116',
    'FPID': 'FPID2.2.qy8MP0BCRfU3Zeky7uYdnXGp2RLxUC1UQfkuX8GrGuI%3D.1667469636',
    '_pin_unauth': 'dWlkPVpEZzBNRGRqWm1NdE9UVmpaUzAwTUdZekxUa3hNekV0WmpSbE5tVmhNR1U0TWpFNQ',
    'IR_PI': '5f6521a1-5b5e-11ed-8a73-a7ed7598257b%7C1668058173178',
    'inside-au': '1163667419-2d29d30ee21932dcd8fd5e557cf9d6783c60709e0435f3327437eac230d209cd-5-5',
    '_fbp': 'fb.1.1667469641077.1711691218',
    '_hjSessionUser_873034': 'eyJpZCI6ImVhZjA1NzQyLTdkZjgtNWVmZi1hNDc3LTE3ZDAwN2JiNGIxNCIsImNyZWF0ZWQiOjE2Njc0Njk2NDA5MTEsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gaexp': 'GAX1.2.OaEU5pZLQhGIWE1qu0c46g.19378.1',
    'BVBRANDSID': '5ce99c63-f587-402c-ab55-adcd488ff8ed',
    'FPLC': 'ahc6SkOLPM9F7501hYxoa7cwFuCCBFPWqACEsmJ95qb61i11kWLGijRHnDm23WjxkI9zT60U0XrM%2F1omUflOhjlrTCJCQWfKyo1dYh1fmkjdHPQcQp%2Fc01%2FlKJnG%2BQ%3D%3D',
    '_gid': 'GA1.2.745968449.1667971131',
    '_hjSession_873034': 'eyJpZCI6ImVlOTUzYjdlLTMyNzEtNGJlNC1hMzJiLTg1NGZlZDk3MmIwOSIsImNyZWF0ZWQiOjE2Njc5NzExMzA4NTksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'incap_ses_1132_1686039': 'bpX9cjYDqQGlVkTdz6y1Dyg6a2MAAAAA5WiU1TsBtlhKEl3MOeN9eg==',
    'IR_gbd': 'davidjones.com',
    'IR_5504': '1667971773178%7C406511%7C1667971773178%7C%7C',
    '_gat': '1',
    '_gat_UA-489931-23': '1',
    '_gat_UA-489931-18': '1',
    '_uetsid': 'fd47eae05fed11eda70321c1e4bbb696',
    '_uetvid': '5d2c5e005b5e11ed9c13ab5da23a5f16',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://www.davidjones.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.davidjones.com/',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'visid_incap_1686039=5lEDO1YJS/iMNWQdUsm+DEKRY2MAAAAAQ0IPAAAAAACAyBOoAWfUnKw7nylA2ClX4/Z3TOS3pmUq; _gcl_au=1.1.288583075.1667469636; _ga_2LJLJKYZ3R=GS1.1.1667971126.13.1.1667971774.0.0.0; _ga=GA1.2.588194849.1667469636; _ga_7ZEZ2L98N2=GS1.1.1667971127.13.1.1667971774.58.0.0; BVBRANDID=93dffa88-0b74-4571-9ab8-fa832bfa9116; FPID=FPID2.2.qy8MP0BCRfU3Zeky7uYdnXGp2RLxUC1UQfkuX8GrGuI%3D.1667469636; _pin_unauth=dWlkPVpEZzBNRGRqWm1NdE9UVmpaUzAwTUdZekxUa3hNekV0WmpSbE5tVmhNR1U0TWpFNQ; IR_PI=5f6521a1-5b5e-11ed-8a73-a7ed7598257b%7C1668058173178; inside-au=1163667419-2d29d30ee21932dcd8fd5e557cf9d6783c60709e0435f3327437eac230d209cd-5-5; _fbp=fb.1.1667469641077.1711691218; _hjSessionUser_873034=eyJpZCI6ImVhZjA1NzQyLTdkZjgtNWVmZi1hNDc3LTE3ZDAwN2JiNGIxNCIsImNyZWF0ZWQiOjE2Njc0Njk2NDA5MTEsImV4aXN0aW5nIjp0cnVlfQ==; _gaexp=GAX1.2.OaEU5pZLQhGIWE1qu0c46g.19378.1; BVBRANDSID=5ce99c63-f587-402c-ab55-adcd488ff8ed; FPLC=ahc6SkOLPM9F7501hYxoa7cwFuCCBFPWqACEsmJ95qb61i11kWLGijRHnDm23WjxkI9zT60U0XrM%2F1omUflOhjlrTCJCQWfKyo1dYh1fmkjdHPQcQp%2Fc01%2FlKJnG%2BQ%3D%3D; _gid=GA1.2.745968449.1667971131; _hjSession_873034=eyJpZCI6ImVlOTUzYjdlLTMyNzEtNGJlNC1hMzJiLTg1NGZlZDk3MmIwOSIsImNyZWF0ZWQiOjE2Njc5NzExMzA4NTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; incap_ses_1132_1686039=bpX9cjYDqQGlVkTdz6y1Dyg6a2MAAAAA5WiU1TsBtlhKEl3MOeN9eg==; IR_gbd=davidjones.com; IR_5504=1667971773178%7C406511%7C1667971773178%7C%7C; _gat=1; _gat_UA-489931-23=1; _gat_UA-489931-18=1; _uetsid=fd47eae05fed11eda70321c1e4bbb696; _uetvid=5d2c5e005b5e11ed9c13ab5da23a5f16',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
p1="https://www.davidjones.com/men/clothing/pyjamas-and-sleepwear?src=fh&size=90&offset={}"
for i in range(00,270,90):
    url=p1.format(i)
    r = s.get(url, cookies=cookies, headers=headers,)
    soup=bs(r.text,"html.parser")
    print(soup.prettify())
    pro=soup.find_all("div","item")
    for j in pro:
        durl=j.find("a","image-link").get("href")
        dr=s.get(durl)
        dsoup=bs(dr.text,"html.parser")
        


