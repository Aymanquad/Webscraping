from bs4 import BeautifulSoup
import requests
import time


inputs_number = int(input("Enter the number of skills u are unfamiliar with ..."))

inputs = input("Enter the skills u are unfamiliar (in Comma seperated order) ...")
unfamiliar =[]
unfamiliar.append(inputs.split(','))

print(unfamiliar)


html_part = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup( html_part , 'lxml' )
jobs = soup.find_all('li' , class_='clearfix job-bx wht-shd-bx')

for index , job in enumerate(jobs):
    flag = 0
    posting_date = job.find('span' , class_='sim-posted').span.text
    if 'few' in posting_date and flag==0 :
        company_name = job.find('h3' , class_='joblist-comp-name').text.replace(' ','')
        keyskills = job.find('span' , class_='srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        flag = 1


    def check():
        for i in range(inputs_number):
            if unfamiliar[0][i] in keyskills:
                return False
        return True



    if flag==1 and check() == True :
        print(f" job number: {index + 1}")
        print(f" Company Name: {company_name.strip()} ")
        print(f" Required Skills : {keyskills.strip()} ")  
        print(f" More Related info : {more_info}")
        print(' ')

        time.sleep(1)