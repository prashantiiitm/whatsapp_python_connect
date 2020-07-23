# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:31:19 2020



@author: prashant.pandey
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket


# Replace below path with the absolute path 
# to chromedriver in your computer 
import os
try:
    filepath = os.path.abspath(os.path.dirname(__file__))
except:
    filepath = "D:\\Project Files\\ETL\\Whatsapp_Text"
os.chdir(filepath)
  
        


text='Test ! Sent from Python' # message you want to send
no_of_message=1 # no. of time you want the message to be send
moblie_no_list=[] # list of phone number can be of any length

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
chromepath = 'chromedriver'
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path=chromepath,chrome_options=options)
driver.get('https://web.whatsapp.com/')

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print(e)
        print("invailid phone no :"+str(phone_no))
for phone_no in moblie_no_list:
    try:
        send_whatsapp_msg(phone_no,text)

    except Exception as e:
        sleep(10)
        is_connected()
        

