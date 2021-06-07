import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd 


sosok = 0       # 0 코스피  / 1 코스닥 
count = 0 

result = []
for page in range(1, 11):
    url = f'https://finance.naver.com/sise/sise_market_sum.nhn?sosok={sosok}&page={page}'
    orginal_url = 'https://finance.naver.com'
    
    res = requests.get(url)
    soup_data = BeautifulSoup(res.content,'html.parser')
    
    for item in soup_data.select('.type_2 tbody tr'):  
        for title in item.select('td:not(.center) a'):   
            count+=1
            print('item_name = ',title.text) 
            print('종합정보 주소:', orginal_url + title['href'])

            code = title['href'][-6:]    
            print('item_code =',code)
            sise_url = f'https://finance.naver.com/sise/sise_market_sum.nhn?code={code}'
            print('시세탭 주소:', sise_url)
            result.append([title.text, code, sise_url]) 
    

df = pd.DataFrame(result, columns=['title', 'code', 'sise_url'])  
df.to_csv('sise_market_sum1.csv')
