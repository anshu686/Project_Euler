from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, os,random

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/home/anshu/Downloads/chromedriver')

 # URL of your homepage you want to scrape
driver.get("https://www.mptax.mp.gov.in/")
wait = WebDriverWait(driver, 600)

print("we are now at the Home page")
time.sleep(random.uniform(6, 10))

#xpath for Dealer..
x_arg = '//*[@id="mainsection"]/form/table[1]/tbody/tr[3]/td[3]/a'
x_arg1 = driver.find_element_by_xpath('//*[@id="mainsection"]/form/table[1]/tbody/tr[3]/td[3]/a')
wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
x_arg1.click()
print ("Clicked on the Dealer")

time.sleep(random.uniform(6, 10))   #wait time of 6-10 sec...
x_arg1.click()  #clicked again.. in case it got lost in the first attempt

z_arg = '//*[@id="dropmenudiv"]/a[1]'
z_arg1 = driver.find_element_by_xpath('//*[@id="dropmenudiv"]/a[1]')
wait.until(EC.presence_of_element_located((
    By.XPATH, z_arg)))
z_arg1.click()
print("Clicked on the dealer search option")
time.sleep(random.uniform(6, 8))   #wait time of 6-8 sec...

print("Wait time of 6 seconds to minimize any discrepancy")

#Xpath of 'First name'--- the radio button
by_name = '//*[@id="byName"]'
by_name1 = driver.find_element_by_xpath('//*[@id="byName"]')
wait.until(EC.presence_of_element_located((
    By.XPATH, by_name)))
by_name1.click()

target = input("Enter the name of Company: ")
target1 = str(target)

search = '//*[@id="showNameField"]/td[2]/input'

input_y = wait.until(EC.presence_of_element_located((
     By.XPATH, search)))
input_y.send_keys(target1 + Keys.ENTER)
