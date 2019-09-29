#%%
import pyderman as driver
path = driver.install(browser=driver.chrome)
print('Installed geckodriver driver to path: %s' % path)

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml
#%%launch url

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
url = "https://shopee.co.id/Jeju-Natural-Mask-WELCOS--i.101515897.1715099836"

#%% create a new Firefox session
driver = webdriver.Chrome(path, options=chrome_options)
driver.implicitly_wait(30)
driver.get(url)

#%%
python_button = driver.find_elements_by_xpath("//div[@id='main']/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div/div/button[2]")[0]
#python_button = driver.find_element_by_id('product-variation') #FHSU
python_button.click() #click fhsu link

soup=BeautifulSoup(driver.page_source, 'html.parser')
page = soup.find("div", {"class": "flex items-center _1FzU2Y"}).getText()
print(page)
