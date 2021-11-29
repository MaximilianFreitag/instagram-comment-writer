#Write a comment on instagram with python

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random as random
import emoji as emoji

url = 'YOUR_URL_HERE'
username = 'YOUR_USERNAME_HERE'
password = 'YOUR_PASSWORD'
driver = webdriver.Chrome('PATH/TO/YOUR/CHROMEDRIVER')


def login():
    driver.get(url)
    time.sleep(4)

    #click on following xpath1
    xpath1 = '/html/body/div[4]/div/div/button[1]'

    driver.find_element_by_xpath(xpath1).click()
    time.sleep(4)


    xpath2 = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    #driver.find_element_by_xpath(xpath2).click()

    driver.find_element_by_xpath(xpath2).send_keys(username)
    time.sleep(2)

    xpath3 = '//*[@id="loginForm"]/div/div[2]/div/label/input'

    driver.find_element_by_xpath(xpath3).send_keys(password)
    time.sleep(2)

    xpath4 = '//*[@id="loginForm"]/div/div[3]/button/div'
    driver.find_element_by_xpath(xpath4).click()

    time.sleep(5)
    xpath5 = '//*[@id="react-root"]/section/main/div/div/div/div/button'
    driver.find_element_by_xpath(xpath5).click()
    
    
    #Switch to the url
    driver.get(url)


    time.sleep(4)




def comment():
    xpath7 = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea'
    driver.find_element_by_xpath(xpath7).click()
    time.sleep(2)
    #generate random number
    random_number1 = random.randint(1,1000)
    random_number2 = random.randint(1,1000)
    random_number3 = random.randint(1,10)
    #choose a random +,-,*,/ for the random numbers
    random_operator = random.choice(['+','-','*','/'])
    result = eval(str(random_number1) + random_operator + str(random_number2) + random_operator + str(random_number3)) 
    
    message = str(random_number1) + str(random_operator) + str(random_number2) + str(random_operator) + str(random_number3) + '=' + str(result)  
    #send message in the textarea
    driver.find_element_by_xpath(xpath7).send_keys(message)

    time.sleep(4)

    xpath8 = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]'
    driver.find_element_by_xpath(xpath8).click()
    time.sleep(4)
    print('Writing comment done!')


login()

while True:

    def write():
        comment()
        time.sleep(50)
        print('Writing comment done!')
        
    write()
