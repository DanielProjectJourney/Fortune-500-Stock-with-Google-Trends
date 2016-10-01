import os,re
import time
from urllib import request
from bs4 import BeautifulSoup

response = request.urlopen('http://www.barchart.com/stocks/sp500.php?_dtp1=0')
soup = BeautifulSoup(response,"html.parser")
table = soup.select('table#dt1')[0].get('data-info')

company = table[8:]
company_array = company.split(';')

timeStr = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

file = open(timeStr + ' Fortune500.txt','w')
file.write(company_array[0])



