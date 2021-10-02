import pymysql
from bs4 import BeautifulSoup
import requests


response = requests.get('https://cafef.vn/')
soup = BeautifulSoup(response.text,'html.parser')
list_title1 = soup.find('div',class_='top_noibat clearfix').find_all('h2')
list_title2 = soup.find('div',class_='box-nha-dau-tu-content').find_all('li')
list_title3 = soup.find('ul', class_='listchungkhoannew').find_all('li')
list_title = list_title1 + list_title2 + list_title3
rootlink = 'https://cafef.vn'
num = 1
driver = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='datanckh'
)

cursor = driver.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS `datacafef`.`datacafe`(
	id AUTO_INCREMENT,
    title varchar(255),
    linkimg varchar(255),
    content varchar(255),
    PRIMARY KEY(id)
)

''')
insert = 'INSERT INTO datacafe (title,linkimg, content) VALUES (%s, %s,%s)'
def getContent(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    contents = soup.find('div', class_='content_cate wp1040 clearfix').text.strip()
    return contents.replace('  ','').replace('\n','')

for itm in list_title:
	title = itm.text.strip()
	link = rootlink+ itm.find('a')['href'] 
	linkimg = itm.parent.find('img')['src']
	# print(title)
	# print(link)
	content = getContent(link)
    # data = (title,linkimg, getContent(link))
    # cursor.execute(insert, data)
    # driver.commit()
    #num+=1

    
	