import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


os.environ['PATH'] += r"C:/Users/Quadri/Downloads/chromedriver_win32(latest)"
driver = webdriver.Chrome()
driver.get('https://twitter.com/animehub21')
driver.maximize_window()


def get_tweets(el):
    try:
        user = el.find_element(By.XPATH , './/span[contains(text() , "@")]').text
        text = el.find_element(By.XPATH , './/div[@data-testid="tweetText"]').text
        return([user , text])

    except:
        print("couldn't find any data nigga !!")

user_data =[]
text_data = []
tweet_ids = set()

Scrolling = True
while Scrolling:
    tweets = WebDriverWait(driver , 15).until(EC.presence_of_all_elements_located((By.XPATH , '//article[@data-testid="tweet"]')))
    for i in range(len(tweets)) :
        tweet_stuff = get_tweets(tweets[i])
        tweet_id = ' '.join(tweet_stuff)
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            user_data.append(tweet_stuff[0])
            text_data.append(" ".join(tweet_stuff[1].split()))

    #                                   infinite scrolling stuff
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0 , document.body.scrollHeight)')
        time.sleep(4)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            Scrolling = False
            break
        else:
            last_height = new_height
            break




time.sleep(4)

df = pd.DataFrame({"user data ": user_data , 'text data': text_data})
df.to_csv('tweet_data.csv' , index=False)

driver.quit()
