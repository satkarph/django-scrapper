from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd
import os

# Optional argument : if not specified WebDriver will search your system PATH environment variable for locating the chromedriver

# chrome_options = FirefoxOptions()
# fp = webdriver.FirefoxProfile()
# download_dir = "/home/oem/PycharmProjects/django-scrapper/"
# fp.set_preference("browser.download.folderList", 2)
# fp.set_preference("browser.download.manager.showWhenStarting", False)
# fp.set_preference("browser.download.dir", download_dir)
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--proxy-server='direct://'")
# chrome_options.add_argument("--proxy-bypass-list=*")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--headless")


import os

cwd = os.getcwd()
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": cwd}
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--proxy-server='direct://'")
chromeOptions.add_argument("--proxy-bypass-list=*")
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument("--window-size=1920,1080")
chromeOptions.add_argument("--headless")


def scrape_northville(part_id):
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    try:
        # driver = webdriver.Firefox(firefox_profile=fp)

        driver.get("https://dnow-gale-com.northvillelibrary.idm.oclc.org/dnow/?p=DNOW&u=lom_northvilledl")
        pasw = driver.find_element_by_xpath("/html/body/form/input[2]")
        pasw.send_keys('29013000550343')
        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()
        myElem = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'search-box')))

        print("hiiiiiiiii")
        # driver.get("https://dnow-gale-com.northvillelibrary.idm.oclc.org/dnow/?p=DNOW&u=lom_northvilledl")
        zipp = driver.find_element_by_xpath('//*[@id="search-box"]')
        zipp.click()
        zipp.send_keys(part_id)
        try:
            myElem2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'mdl-list__item-sub-title')))

        except TimeoutException:
            print("failed")
            driver.quit()
            return

        # time.sleep(5)
        zipp.send_keys(Keys.RETURN)

        driver.find_element_by_xpath('//*[@id="home"]/div/div/div[2]/section[1]/div/div[3]/a').click()
        driver.find_element_by_xpath('//*[@id="people-companies"]/div/div/section/div[2]/div/label[1]/i').click()
        print("------")
        driver.find_element_by_xpath('//*[@id="people-companies"]/div/div/section/div[2]/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="accordion0"]/ul/li[1]/span[2]/label/span[3]').click()
        driver.find_element_by_xpath('//*[@id="accordion1"]/ul/li[1]/span[2]/label/span[3]').click()
        driver.find_element_by_xpath('//*[@id="business-search"]/span').click()
        first_xpath = "/html/body/div[2]/div/main/section[2]/div/div/div[1]/div/div[3]/section/section/div[2]/div[1]/button"
        second_xpath = "/html/body/div[2]/div/main/section[2]/div/div/div[1]/div/div[3]/section/section/div[2]/div[1]/button[2]"
        time.sleep(15)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/main/section[2]/div/div/div[1]/div/div[3]/section/section/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[1]/label/span[3]').click()
        driver.find_element_by_xpath('//*[@id="business-tool-download"]').click()
        driver.find_element_by_xpath('//*[@id="business-list-download-form"]/div[1]/label[2]/span[4]').click()
        driver.find_element_by_xpath('//*[@id="business-list-download-form"]/div[2]/label[2]/span[1]').click()
        driver.find_element_by_xpath('//*[@id="business-list-download-dialog"]/div[2]/button[1]/span').click()
        dfs = []
        time.sleep(10)
        df = pd.read_csv('Business List.csv')
        dfs.append(df)
        while True:
            os.remove('Business List.csv')
            try:
                driver.find_element_by_xpath(first_xpath).click()
                time.sleep(10)
                driver.find_element_by_xpath(
                    '/html/body/div[2]/div/main/section[2]/div/div/div[1]/div/div[3]/section/section/div[2]/div[2]/div[1]/div[1]/div/table/thead/tr/th[1]/label/span[3]').click()
                driver.find_element_by_xpath('//*[@id="business-tool-download"]').click()
                driver.find_element_by_xpath('//*[@id="business-list-download-form"]/div[1]/label[2]/span[4]').click()
                driver.find_element_by_xpath('//*[@id="business-list-download-form"]/div[2]/label[2]/span[1]').click()
                driver.find_element_by_xpath('//*[@id="business-list-download-dialog"]/div[2]/button[1]/span').click()
                time.sleep(20)
                first_xpath = second_xpath
                while True:
                    try:
                        df2 = pd.read_csv('Business List.csv')
                        break
                    except:
                        pass
                dfs.append(df2)
            except NoSuchElementException:
                break
        driver.quit()
        return dfs
    except:
        driver.quit()
        return None

    # except:
    #     driver.quit()

    # return dfs



