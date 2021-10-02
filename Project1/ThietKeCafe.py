from bs4 import BeautifulSoup
import requests
from xlwt import Workbook

response = requests.get("https://vneconomy.vn/tieu-dung/thi-truong.htm")
soup = BeautifulSoup(response.text, 'html.parser')
list_title = soup.find('div',class_='all').find_all('div', class_='item')
rootlink = 'https://vneconomy.vn'

wb = Workbook()
sheet1 = wb.add_sheet('ThiTruong')
sheet1.write(0,0, 'ID')
sheet1.write(0,1, 'Title')
sheet1.write(0,2, 'Linkimg')
sheet1.write(0,3, 'Contents')
sheet1.write(0,4, 'timing')
def getContent(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    contents = soup.find('div', class_='all-content').text.strip()
    return contents.replace('  ', '').replace('\n', '')
def getTiming(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    timing = soup.find('a', class_='date').text.strip()
    return timing.replace('  ', '').replace('\n', '')
num = 28
for itm in list_title:
    title = itm.text.strip()
    link = rootlink + itm.find('a')['href']
    img = itm.find('img')['src']
    # print('========================================================')
    # print(title)
    # print(img)
    # print(getContent(link))
    # print(getTiming(link))
    sheet1.write(num,0,num)
    sheet1.write(num,1,title)
    sheet1.write(num,2,img)
    sheet1.write(num,3,getContent(link))
    sheet1.write(num,4,getTiming(link))
    num=num+1
    
wb.save('ThiTruong2.xls')