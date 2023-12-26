import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


os.environ['PATH'] += r"C:/Users/Quadri/Downloads/chromedriver_win32"
driver = webdriver.Chrome()
driver.get('https://www.audible.in/adblbestsellers?ref=a_hp_t1_navTop_pl1cg0c1r0&pf_rd_p=4e150d5e-ca98-47fb-823b-f6fcb252aced&pf_rd_r=P60367SXM08DWMW8P6FS&pageLoadId=Z1DKrcY2LrIzGJRR&creativeId=2e6787a2-0cd0-4a6e-afe0-05766cd505e5')
driver.maximize_window()


 
pagination = driver.find_element(By.XPATH , '//ul[contains(@class , "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME , 'li')
last_pg = int(pages[-2].text)


current_pg = 1
book_name = []
book_Author = []
book_length = []



while current_pg <= last_pg :
    

    time.sleep(3)
    # container =  driver.find_element(By.XPATH , "//div[contains(@class , 'adbl-impression-container')]" )
    products = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH , "//div[@class='adbl-impression-container ']//li[contains(@class , 'productListItem')]" )))
    # products = container.find_elements(By.XPATH , "./li")
    # products = WebDriverWait(container, 30).until(EC.presence_of_all_elements_located((By.XPATH , ".//li[contains(@class , 'productListItem')")))

    for i in range(0,len(products)) :
        # book_Author.append(product)
        book_name.append(products[i].find_element(By.XPATH ,".//h3[contains(@class , 'bc-heading')]/a").text)
        book_Author.append(products[i].find_element(By.XPATH ,".//li[contains(@class , 'authorLabel')]").text)
        book_length.append(products[i].find_element(By.XPATH ,".//li[contains(@class , 'runtimeLabel')]/span").text)

        # print((block.find_element(By.XPATH , './/h3[contains(@class , "bc-heading")]').text))

    print(current_pg)
    current_pg = current_pg + 1
        
    try:
        next_pg_button = driver.find_element(By.XPATH , "//span[contains(@class , 'nextButton')]")
        # (driver.find_element(By.XPATH,'//a[contains(@aria-disabled , "true")]')) 
        next_pg_button.click()
    except:
        pass

print(book_name)
print(book_Author)
# print("muah")
         
driver.quit()

df = pd.DataFrame({'book Name' : book_name  , 'Author' : book_Author, 'length' : book_length})
df.to_csv('Books_data.csv' , index=False)


time.sleep(5)
        

    

# print(book_name)