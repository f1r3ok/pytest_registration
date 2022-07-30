import os, time, random, allure, sys, pytest, urllib3, re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
# from pytest_bdd import scenario, given, when, then

url = "http://btcloopholepro.com/?TrackingID=1555"
lang = "English"
now = time.gmtime(time.time())
name = str(now.tm_hour) + ':' + str(now.tm_min) + ':' + str(now.tm_sec) + url + ' - ' + lang + ' - framework42'

capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False,
        "name": name,
        "screenResolution": "1280x1024x24"
        }
}


driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)


def capture_screenshot(title='captured_screenshot'):
    allure.attach(driver.get_screenshot_as_png(), name=f'{title}', attachment_type=allure.attachment_type.PNG)



def set_language(driver, language):
    driver.find_element_by_xpath('//div[@class="lang"]').click()
    driver.find_element_by_xpath('//*[text()="' + language + '"]').click()

# def test_Form_Is_submited():
#     print(url)
#     driver.get(url)
#     driver.maximize_window()
#     capture_screenshot('test_page_is_loaded')
#     set_language(driver,lang)
#     capture_screenshot("test_language_is_set")

def test_Page_Is_Loaded():
    print(url)
    driver.get(url)
    driver.maximize_window()
    try:
        driver.find_element_by_xpath('//a[@class="cw-close close"]').click()
    except:
        pass

def test_Language_Is_Set():
    print(url)
    set_language(driver,lang)
    capture_screenshot("test_language_is_set")


def test_Full_Name_Input():
    try:
        driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[full_name]"]').send_keys('test')
    except:
        pass

def test_First_Name_Input():
    try:
        driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[first_name]"]').send_keys('test')
    except:
        pass

def test_Last_Name_Input():
    try:
        driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[last_name]"]').send_keys('test')
    except:
        pass

def test_Email_Input_And_Submit():
    try:
        driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[email]"]').send_keys('qa_test_' + str(random.random())[2:] + '@test.com' + Keys.ENTER)
    except:
        pass

def test_Generate_Pass():
    sleep(1)
    try:
        driver.find_element_by_xpath('//div[@class="btn generate-pass"]').click()
    except:
        try:
            driver.find_element_by_xpath('//div[@class="nice-btn generate-pass"]').click()
        except:
            try:
                driver.find_element_by_xpath('//div[@class="generate-pass"]').click()
            except:
                try:
                    driver.find_element_by_xpath('//button[@class="btn generate-pass w-button"]').click()
                except:
                    try:
                        driver.find_element_by_xpath('//div[@class="btn-violet generate-pass"]').click()
                    except:
                        try:
                            driver.find_element_by_xpath('//div[@class="button color-white text-center generate-pass"]').click()
                        except:
                            driver.find_element_by_xpath('//a[@class="generate-pass w-button"]').click()

def test_Phone_Number():
    driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[phone_number]"]').send_keys('645587826')
    try:
        driver.find_element_by_xpath('//input[@type="checkbox"]').click()
    except:
        pass

def test_Last_Name_Input_Again():
    try:
        driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[last_name]"]').send_keys('test')
    except:
        pass
    capture_screenshot("screenshot")

    # driver.find_element_by_xpath('//button[@type="submit"]').click()

# def test_First_Name():
#     print(url)    
#     driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[first_name]"]').send_keys('test')

# def test_Last_Name():
#     print(url)
#     driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[last_name]"]').send_keys('test')

# def test_Email():
#     print(url)
#     driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[email]"]').send_keys('qa_test_' + str(random.random())[2:] + '@test.com')

# def test_Generate_Pass():
#     print(url)
#     try:
#         driver.find_element_by_xpath('//div[@class="btn generate-pass"]').click()
#     except:
#         try:
#             driver.find_element_by_xpath('//div[@class="nice-btn generate-pass"]').click()
#         except:
#             try:
#                 driver.find_element_by_xpath('//div[@class="generate-pass"]').click()
#             except:
#                 try:
#                     driver.find_element_by_xpath('//button[@class="btn generate-pass w-button"]').click()
#                 except:
#                     try:
#                         driver.find_element_by_xpath('//div[@class="btn-violet generate-pass"]').click()
#                     except:
#                         driver.find_element_by_xpath('//div[@class="button color-white text-center generate-pass"]').click()

# def test_Phone_Number():
#     print(url)
#     driver.find_element_by_xpath('//input[@name="FunnelRegistrationForm[phone_number]"]').send_keys('645587826')
#     capture_screenshot("screenshot")

def test_Submit():
    print(url)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

def test_Congratulations():
    print(url)
    sleep(3)
    capture_screenshot("screenshot")
    assert ('Congratulations' in driver.title)
    driver.quit()
