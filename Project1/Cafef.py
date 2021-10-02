from bs4 import BeautifulSoup
import requests
# import pymysql
from xlwt import Workbook

response = requests.get('https://vneconomy.vn/tieu-dung/thi-truong.htm')
soup = BeautifulSoup(response.text, 'html.parser')
list_title = soup.find('div', class_='wtdmc-main-content').find_all('div', class_='item')

rootlink = 'https://vneconomy.vn'



wb = Workbook()
sheet1 = wb.add_sheet('TieuDung')
sheet1.write(0,0, 'ID')
sheet1.write(0,1, 'Title')
sheet1.write(0,2, 'Linkimg')
sheet1.write(0,3, 'Contents')
sheet1.write(0,4, 'timing')
# driver = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='datacafef'
# )

# cursor = driver.cursor()
# cursor.execute("CREATE TABLE datacafe(id INT PRIMARY KEY AUTO_INCREMENT,title varchar(255),linkimg varchar(255),content varchar(1000000000))")

# insert = 'INSERT INTO datacafe (title, linkimg, content) VALUES (%s,%s,%s)'


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
num = 1
for itm in list_title:
    title = itm.text.strip()
    link = rootlink + itm.find('a')['href']
    img = itm.parent.find('img')['src']
    print(title)
    print(link)
    print(img)
    print(getContent(link))
    print(link)
    sheet1.write(num,0,num)
    sheet1.write(num,1,title)
    sheet1.write(num,2,img)
    sheet1.write(num,3,getContent(link))
    sheet1.write(num,4,getTiming(link))
    num=num+1
#     # data = (title,img, getContent(link))
#     # cursor.execute(insert, data)
#     # driver.commit()
wb.save('TieuDung.xls')