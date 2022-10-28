#insta follow requests bot
import csv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# the folder and the file we working on
os.chdir(r'C:\Users\hamza\Desktop\pythonProject\csvfile_test')
_file = "Book1.csv"
#---- open and reading the list of follow requests ----
def id_file():
    user_names_list = []
    with open(_file,"r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            user_names_list.append(row)
    
    return user_names_list

#----driver----
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com")

#----login----
def login(): 
#----connect account----
    username = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME,'username')))
    username.clear()
    username.send_keys("_hamza.py")
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,'password')))
    password.send_keys("init5EFPig")

    login = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    login.click()

#----passing the pop ups messages----
    notnow = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,'//button[contains(text(), "Not Now")]')))
    notnow.click()

    notnow2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,'//button[contains(text(), "Not Now")]')))
    notnow2.click()

#----search and unfollow ----
def find_people(fl_list):
    
    try:
        find = WebDriverWait(driver,10).until(EC.presence_of_element_located(
            (By.XPATH,"//div[a/@href='/explore/']")))
        find.click()
        search_click =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"_aaw9")))
        search_click.click()

        search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='text']")))
        search.clear()

        driver.implicitly_wait(10)
        search.send_keys(fl_list)

        search.send_keys('\ue007')
    
        #keywrd = "men_of_culture_1"
        #search.send_keys(keywrd)

        result = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f"//a[@href='/"+fl_list+"/']")))
        result.click()

        time.sleep(5)
        
        #----unfollow----
        unfollow_select = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Requested')]")))        
        unfollow_select.click()
        
        unfollow_confirme = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Unfollow')]")))
        unfollow_confirme.click()
            
        time.sleep(3)
        #follow_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Follow')]")))
            
    except:

        try_again = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'OK')]")))   
        try_again.click()
        find_people(fl_list)

#---------
def update_column(i):
    # reading the csv file
    df = pd.read_csv(_file)
    
    # updating the column value/data
    df.loc[i, 'state'] = 'unfollowed'
    
    # writing into the file
    df.to_csv(_file, index=False)

def unfollow_loop():
    users_list = id_file()
    for i in range(1,len(users_list)):
        find_people(users_list[i][0])
        update_column(i - 1)
        #test_condition
        #if(i == 3):
        #    break

login()
unfollow_loop()
