#imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import func


#Make code run in the background
#can be minimised
#chrome runs in the background better, not mozilla


#setting up and loading the browser
driver = webdriver.Firefox(executable_path=r'C:\Users\tuxo9\Downloads\geckodriver\geckodriver.exe')
driver.get("https://www.instagram.com/")

#log in
username = "enter username"
password = "enter password"
func.login(username, password, driver)

#navigate to following list

#more efficient way of obtaining users following page
driver.get("https://www.instagram.com/" + username)


following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
following.send_keys(Keys.RETURN)
time.sleep(5)


followingList = []
quantityFollowing = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
scrollbar = driver.find_element_by_class_name("isgrP")


func.createUserList(driver, quantityFollowing, scrollbar, followingList)

followersList = []
followersQuantity = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text
followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.send_keys(Keys.RETURN)
scrollbar = driver.find_element_by_class_name("isgrP")


func.createUserList(driver, followersQuantity, scrollbar, followersList)


time.sleep(3)
unfollow = func.unfollowList(followingList, followersList)
print("No match elements: ", unfollow)
print(len(unfollow))

#find out a range of how many actions i can execute per hour on instagram - between 8 - 13
#ranomly generate number in that range, becoming the amount we unfollow in an hour
#select the users and unfollow them, then remove from the list
#continue untill the list length is zero

func.unfollowProcess(driver, unfollow)
        

#to do
#fix timings, using selenium, in code to make it work faster and more reliable
    


#the end
driver.close()


