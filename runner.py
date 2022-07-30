import os, time, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


capabilities = {
  "browserName": "chrome",
  "browserVersion": "100.0",
  "selenoid:options": {
  "enableVNC": True,
  "enableVideo": False,
  "screenResolution": "1280x1024x24"
  }
}

driver = webdriver.Remote(command_executor="http://46.166.138.15:4444/wd/hub", desired_capabilities=capabilities)

driver.maximize_window()

bash_script = 'python3 -m pytest -v --alluredir=./allure_result &'

links = open("links.txt", "r")

old_path = './test_pages_lang.py'

for x in links:
    link = x.strip()
    driver.get(link)
    langs = driver.find_elements_by_xpath('//div[@class="languageSelect-list-item"]/a/div[2]')
    for l in langs:
        lang = l.get_attribute("textContent")
        link_name = link[7:]
        link_name = link_name[:-21]
        new_name = 'test_' + link_name + '_' + lang + '.py'
        new_path = './' + new_name
        os.rename(old_path, new_path)
        old_path = new_path
        test_opener = open(new_name, 'r')
        test_tmp = test_opener.read()
        test_list = test_tmp.splitlines(True)
        test_opener.close()
        test_list[11] = 'url = "' + link + '"' + '\n'
        test_list[12] = 'lang = "' + lang + '"' + '\n'
        test_opener = open(new_name, 'w')
        for n in test_list:
            test_opener.write(n)
        test_opener.close()
        os.system(bash_script)
        sleep(30)


links.close()
driver.quit()