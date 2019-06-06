
import requests
from bs4 import BeautifulSoup
import pandas as pd

#http request parameters
request_param  = {"station" : "467490" , "stname" : "%25E8%2587%25BA%25E4%25B8%25AD" , "datepicker":"2016-09"}
url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain'

result = requests.get('https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=467490&stname=%25E8%2587%25BA%25E4%25B8%25AD&datepicker=2016-09')
content = result.content
soup = BeautifulSoup(content , "html.parser")
title_tag = soup.title
table = soup.find('table',attrs={'id':'MyTable'})
column = soup.find('tr' , attrs={'class':'second_tr'})
columns = [th.text.replace('\n', '') for th in column.find_all('th')]
trs = table.find_all('tr')[3:]
rows = list()
for tr in trs:
    rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])

df = pd.DataFrame(data=rows, columns=columns)
df.head()
print(df)


