from requests_html import HTMLSession
from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/Lam/Downloads/chromedriver/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://porkshop.vn/');
time.sleep(5)

list_pro = driver.find_elements_by_class_name('list-collection-index product-item mt15 clearfix col-xs-12 pd5')
for itm in list_pro:
    name = itm.find_element_by_class_name('product-info')
    print(name.text)

print(len(list_pro))
time.sleep(5) # Let the user actually see something!
driver.quit()

# session = HTMLSession()
# urls = 'https://tiki.vn/search?q=tai+nghe+bluetooth&ref=searchBar'
# page = 1
# for i in range(1,4):
#     print('--------page ',page,'-----------------')
#     response = session.get(urls+ str(i))
#     soup = BeautifulSoup(response.text,'html.parser')


#     list_title = soup.find_all('a',class_='product-item')



#     for itm in list_title:
#         info = itm.find('div', class_='info')

#         name = info.find('div',class_='name').text
#         rating = info.find('div',class_='review').text
#         price = info.find('div',class_='price-discount__price').text
#         print(name)
#         print(rating)
#         print(price)
#     page+=1