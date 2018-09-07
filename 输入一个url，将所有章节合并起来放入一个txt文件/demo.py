# encoding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




url = 'http://www.quanben5.com/n/doushentianxia/xiaoshuo.html'

driver = webdriver.Chrome(
    executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# driver = webdriver.PhantomJS()
driver.get(url)
texts=[]
elements = driver.find_elements_by_xpath('//div[@class="box"]/ul/li/a')
time.sleep(1)
for x in range(len(elements)):
    ps = driver.find_elements_by_xpath('//div[@class="box"]/ul/li/a')
    ps[x].click()
    WebDriverWait(driver, 60).until(EC.visibility_of_any_elements_located((By.ID, 'content')))
    text = driver.find_elements_by_xpath('//*[@id="content"]/p')
    texts.append('\n'.join([p.text for p in text]))
    driver.back()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/h3/span')))
f = open('./text.txt', 'w', encoding='utf-8')
f.write('\n'.join(texts))
f.close()

