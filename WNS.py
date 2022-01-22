import os
from selenium import webdriver
import re
import time

driver = webdriver.Chrome()
driver.get(
    'https://cybersmart.wnscaresfoundation.org')
driver.maximize_window()

# TYPE NAME HERE

Z = ("Anita Dande")

# open wns website and click on students portal
Std_login = driver.find_element_by_xpath(
    '//*[@id="navbarResponsive"]/ul/li[1]/a')
Std_login.click()
time.sleep(5)
# click next button
clk_nxt = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div[2]/div/div/form/div[2]/button')
clk_nxt.click()

# Enter student name
Enter_Nm = driver.find_element_by_xpath(
    '//*[@id="Name"]')
Enter_Nm.send_keys(Z)

# Enter class
Enter_Cls = driver.find_element_by_xpath(
    '//*[@id="SelectedClassName"]')
a = Enter_Cls.find_element_by_xpath('//*[@id="SelectedClassName"]/option[4]')
a.click()
a.click()
a.click()
# Enter state name
# Select_cls = driver.find_element_by_xpath(
#     '//*[@id="SelectedClassName"]/option[4]').click()

Enter_state = driver.find_element_by_xpath(
    '//*[@id="SelectedLocationName"]')
b = Enter_state.find_element_by_xpath(
    '//*[@id="SelectedLocationName"]/option[15]')
b.click()
b.click()
b.click()
b.click()
e = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]')
e.click()

# Enter Partner name
# Select_state = driver.find_element_by_xpath(
#     '//*[@id="SelectedLocationName"]/option[15]').click()
# Hit next button
e.click()
# Hit next button
e.click()
# Hit next button
e.click()
# Hit next button
e.click()
e.click()
Enter_prt = driver.find_element_by_xpath(
    '//*[@id="PartnerShortCode"]')
c = Enter_prt.find_element_by_xpath(
    '//*[@id="PartnerShortCode"]/option[11]')
c.click()
c.click()
c.click()
c.click()


# Hit next button
e.click()
Hit_nxt = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div[2]/div/div/form/div[6]/button')
Hit_nxt.click()
time.sleep(5)

# Page 2 Starting

# welcome msg - Click next button
Hit_wlc = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div/div/a/div/img')
Hit_wlc.click()

# click next button and start 1st chapter
e = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div/div')
e.click()
time.sleep(5)
e.click()
e.click()
e.click()
e.click()
fe = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div[2]/button')
fe.click()

ff = 'https://cybersmart.wnscaresfoundation.org/Students/Video'
fg = re.sub('Video', 'CorrectAnswer#', ff)
driver.get(fg)

# Answer Questions of each module -
Ans1 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
# True =  /html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span
# False = /html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span
Ans1.click()

N1 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N1.click()

Ans1 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans1.click()

N1 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N1.click()

# False - //*[@id = "option"]/a/span


Ans1 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans1.click()

N1.click()
# Question 3 False

Ans1 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans1.click()

N1.click()

# Question 5 - 4 options


Ans1 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[3]/a/span')
Ans1.click()

N1.click()

# Module 2 starts

time.sleep(5)

N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div[2]/button')
N2.click()

ff = 'https://cybersmart.wnscaresfoundation.org/Students/Video'
fg = re.sub('Video', 'CorrectAnswer#', ff)
driver.get(fg)

# Q1
Ans2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans2.click()
# /html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button
N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N2.click()

# Q2
Ans2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans2.click()
# /html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button
N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N2.click()

# Q3
Ans2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[4]/a/span')
Ans2.click()
# /html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button
N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N2.click()

# Q4
Ans2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[4]/a/span')
Ans2.click()
# /html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button
N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N2.click()

# Q5
Ans2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans2.click()
# /html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button
N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N2.click()


# End of module 2
# Module 3 starts

time.sleep(5)

N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div[2]/button')
N2.click()


ff = 'https://cybersmart.wnscaresfoundation.org/Students/Video'
fg = re.sub('Video', 'CorrectAnswer#', ff)
driver.get(fg)


# Q1
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()

# Q2
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# Q3
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# Q4
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()

# Q5
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# End of Module 3
# Module 4 begins

time.sleep(5)

N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div[2]/button')
N2.click()

ff = 'https://cybersmart.wnscaresfoundation.org/Students/Video'
fg = re.sub('Video', 'CorrectAnswer#', ff)
driver.get(fg)


# Q1
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[3]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()

# Q2
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# Q3
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# Q4
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()

# Q5
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()

# End of module 4
# module 5 Begins

time.sleep(5)

N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div[2]/button')
N2.click()

ff = 'https://cybersmart.wnscaresfoundation.org/Students/Video'
fg = re.sub('Video', 'CorrectAnswer#', ff)
driver.get(fg)


# Q1
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()

# Q2
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[1]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# Q3
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[2]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# Q4
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[4]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()

# Q5
Ans3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li[3]/a/span')
Ans3.click()

N3 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/button')
N3.click()


# End of module 4
# Download Certificate

Clk2 = driver.find_element_by_xpath(
    '//*[@id="path-color_change"]')
driver.implicitly_wait(10)

N2 = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/div[2]/button')
N2.click()


DL = driver.find_element_by_xpath(
    '/html/body/section[1]/div[2]/div/div/div/div/div[2]/button')
DL.click()

Prnt = driver.find_element_by_xpath(
    '/html/body/print-preview-app//print-preview-sidebar//print-preview-button-strip//div/cr-button[1]')
Prnt.click()
