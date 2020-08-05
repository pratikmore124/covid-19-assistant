from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

try:
    re=requests.get('https://www.mygov.in/covid-19')
    soup=BeautifulSoup(re.content,'html.parser')
except Exception as e:
    print(e)


data=soup.find('div',{'class':'information_block'})

total_active_cases=data.find('span',class_='icount').text
total_recover=data.find('div',class_='iblock discharge').find('span',class_='icount').text
total_death=data.find('div',class_='iblock death_case').find('span',class_='icount').text

state=data.find_all('div',class_='views-row')

state_name=[]
total_case=[]
died=[]
recover=[]
active_case=[]

for i in state:
    name = i.find('span', attrs={'class': 'st_name'})
    confirm = i.find('div', class_='tick-confirmed')
    active = i.find('div', class_='tick-active')
    discharge = i.find('div', class_='tick-discharged')
    death = i.find('div', class_='tick-death')

    state_name.append(name.text)
    total_case.append(confirm.text.split()[1])
    recover.append(discharge.text.split()[1])
    died.append(death.text.split()[1])
    active_case.append(active.text.split()[1])

    # print(confirm.text.split('Confirmed')[1])
    # print(active.text.split('Active')[1])
    # print(discharge.text.split('Recovered')[1])
    # print(death.text.split('Deceased')[1])



a=zip(state_name,total_case,died,recover,active_case)
covid_database={}
for i in a:
    covid_database[str(i[0])]={'total case':int(i[1].replace(',','')),'died':int(i[2].replace(',','')),'recover':int(i[3].replace(',','')),'active':int(i[4].replace(',',''))}



covid_database['Total-Active-Cases']=total_active_cases
covid_database['Total-Recover']=total_recover
covid_database['Total-Death']=total_death



