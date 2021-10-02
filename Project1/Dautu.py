from bs4 import BeautifulSoup
import requests
from xlwt import Workbook

response = requests.get('https://organicfood.vn/do-uong-huu-co')
soup = BeautifulSoup(response.text, 'html.parser')
list_title = soup.find('div', class_= 'products-category clearfix').find_all('div', class_='product-image-container')
rootlink = 'https://vinmart.com'


wb = Workbook()
sheet1 = wb.add_sheet('Gia cầm và trứng')
sheet1.write(0,0, 'ID')
sheet1.write(0,1, 'Title')
sheet1.write(0,2, 'Linkimg')
sheet1.write(0,3, 'Price')

# def getContent(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     contents = soup.find('div', class_='css-111s35w').text.strip()
#     return contents.replace('  ', '').replace('\n', '')
# def getTiming(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     timing = soup.find('div', class_='single-time').text.strip()
#     return timing.replace('  ', '').replace('\n', '')
def getTitle(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1').text.strip()
    return title.replace('  ', '').replace('\n', '')
def getPrice(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('span', class_='price-new').text.strip()
    return title.replace('  ', '').replace('\n', '')
num = 1
for itm in list_title:
    try:
        link =  itm.find('a')['href']
    except:
        print('Không link')
        continue
    img = itm.find('a').find('img')['data-src']
    print('===================================================================')
    print(getTitle(link))
    # print(link)
    print(img)
    # print(getContent(link))
    sheet1.write(num,0,num)
    sheet1.write(num,1,getTitle(link))
    sheet1.write(num,2,img)
    sheet1.write(num,3,getPrice (link))
    num=num+1
wb.save('Egg.xls')