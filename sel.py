import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options


#<----------------------- for headless mode ---------------------->

# options = Options()
# options.headless = True
#driver = webdriver.Chrome(options=options)

#<--------------------------              -------------------------->


os.environ['PATH'] += r"C:/Users/Quadri/Downloads/chromedriver_win32"
driver = webdriver.Chrome()
driver.get('https://www.adamchoi.co.uk/overs/detailed')
driver.maximize_window()


all_matches_button=driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches_button.click()

time.sleep(3)

dropdown = Select(driver.find_element(By.ID , 'country'))
dropdown.select_by_visible_text('Portugal')


matches = driver.find_elements(By.TAG_NAME, 'tr')

date=[]
home_team = []
score=[]
away_team = []

for match in matches :
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

# print(score[0:20])

df = pd.DataFrame({'date' : date  , 'hometeam' : home_team , 'score' : score , 'awayteam' : away_team})
df.to_csv('Portugal_football_data.csv' , index=False)


time.sleep(5)


