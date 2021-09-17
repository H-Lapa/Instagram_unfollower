import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import func
from selenium.common.exceptions import NoSuchElementException
import re
import random

def login (username, password, driver):
    #accept cookie button has been pressed
    cookie  = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
    cookie.send_keys(Keys.RETURN)

    #username and password details have been entered
    time.sleep(5)
    user = driver.find_element_by_name("username")
    pwb = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    user.clear()
    user.send_keys(username)
    pwb.clear()
    pwb.send_keys(password)
    submit.send_keys(Keys.RETURN)
    time.sleep(3)

    #check if details worked

    #This finds the error message and uses 'elements' to store elements in array but there should only be one
    check = driver.find_elements_by_id("slfErrorAlert") 
    
    #checks if the error element is there and acts on it
    if check == []:
        print("success")
    else:
        print("Details are incorrect!")
        driver.close()

def createUserList(driver, quantity, scrollbar, list):
    quantity = re.sub(",", "", quantity)
    print(quantity)


    for x in range(1, int(quantity) + 1):
        try:
            driver.find_element_by_css_selector("li.wo9IH:nth-child("+ str(x) +") > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)")
        except NoSuchElementException:
            scrollbar.send_keys(Keys.END)
            time.sleep(3)

        name = driver.find_element_by_css_selector("li.wo9IH:nth-child("+ str(x) +") > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)")
        user = name.get_attribute("title")
        print(user)
        list.append(user)

    print(list)

def unfollowList(list_a, list_b):
    unfollow = []
    for i in list_a:
        if i not in list_b:
            unfollow.append(i)
    return unfollow


def unfollowProcess(driver, list):
    while len(list) != 0:
        for x in range(len(list)):
            z = random.randint(6, 12)
            unfollows(driver, list)
            print(list)
            time.sleep(z * 60)

def unfollows(driver, list):
    x = list.pop()
    driver.get("https://www.instagram.com/" + x)
    time.sleep(5)
    unfollowButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button")
    unfollowButton.send_keys(Keys.RETURN)
    unfollowConfirm = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
    unfollowConfirm.send_keys(Keys.RETURN)
