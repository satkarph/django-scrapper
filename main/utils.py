from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait


import time
import pandas
# import xlwt
# from xlwt import Workbook
# from tqdm import tqdm



def scraper_spectra(part_id):
    chrome_options = FirefoxOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=chrome_options)
    found_values = []
    driver.get('https://ecat.spectrapremium.com/')
    timeout = 10
    part_found = 1
    try:
        element_present = EC.presence_of_element_located((By.ID, "menu_vertical_interchanges_r"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Could not find anything for ID: " + part_id)
    time.sleep(2)
    print("hihihihihihih")
    # driver.save_screenshot(filename="nepal.jpg")
    driver.execute_script('$("#menu_vertical_interchanges_r").click()')
    # interchange_button.click()
    try:
        element_present = EC.presence_of_element_located((By.ID, "menu_vertical_interchanges_r_refcode"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    time.sleep(2)
    input_element = driver.find_element_by_xpath('//input[@id="menu_vertical_interchanges_r_refcode"]')
    input_element.send_keys(part_id)
    input_element.send_keys(Keys.ENTER)
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, "ligne"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        part_found = 0

    if (part_found == 1):
        # print(part_id)
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append(part_id)
        part_name = driver.find_element_by_class_name("ligne")
        # print(part_name.text)
        found_values[0].append(part_name.text)
        oe = driver.find_element_by_class_name("marque")
        # print(oe.text)
        found_values[0].append(oe.text)
    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found')

    driver.quit()
    return found_values

