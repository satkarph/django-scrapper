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


def airtex(part_id):


    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://www.showmetheparts.com/airtex/')
    found_values = []
    part_found = 1
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.ID, "tab-1248-btnInnerEl"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    crossreference_button = driver.find_element_by_id("tab-1248-btnInnerEl")
    crossreference_button.click()
    try:
        element_present = EC.presence_of_element_located((By.ID, "button-1005-btnInnerEl"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    ok_button = driver.find_element_by_id("button-1005-btnInnerEl")
    ok_button.click()

    driver.implicitly_wait(5)
    input_element = driver.find_element_by_xpath('//input[@id="textfield-1138-inputEl"]')
    input_element.send_keys(part_id)
    input_element.send_keys(Keys.ENTER)

    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, "PartsViewLabel"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        part_found = 0
        print("Timed out waiting for page to load")

    if (part_found == 1):
        found_values.append([])
        # print(part_id)
        found_values[0].append(part_id)
        part_number = driver.find_element_by_class_name("PartsViewPartNumberLink")
        # print(part_number.text)
        found_values[0].append(part_number.text)
        part_manufacturer = driver.find_element_by_xpath('//*[@id="dataview-1129"]/div[1]/div[2]/div[1]')
        # print(part_manufacturer.text[14:])
        found_values[0].append(part_manufacturer.text[14:])
        part_type = driver.find_element_by_xpath('//*[@id="dataview-1129"]/div[1]/div[2]/div[4]')
        # print(part_type.text[11:])
        found_values[0].append(part_type.text[11:])
    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found')

    driver.quit()
    return found_values


def scraper_usmotorworks(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('http://www.usmotorworks.com/catalog/')
    found_values = []
    part_found = 1
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.ID, "advanced_iframe"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    driver.switch_to.frame(driver.find_element_by_id("advanced_iframe"))

    xref_button = driver.find_element_by_id("ui-id-3")
    xref_button.click()
    try:
        element_present = EC.presence_of_element_located((By.ID, "crossRefSearch"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    input_element = driver.find_element_by_id("crossRefSearch")
    input_element.send_keys(part_id)
    input_element.send_keys(Keys.ENTER)

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="interchange"]/tbody/tr[1]/td[3]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        part_found = 0

    if (part_found == 1):
        table = driver.find_elements_by_xpath('//*[@id="interchange"]/tbody/tr')
        for i in range(len(table)):
            found_values.append([])
            # print(part_id)
            found_values[i].append(part_id)
            table_element_one = driver.find_element_by_xpath(
                '//*[@id="interchange"]/tbody/tr[' + str(i + 1) + ']/td[1]')
            table_element_two = driver.find_element_by_xpath(
                '//*[@id="interchange"]/tbody/tr[' + str(i + 1) + ']/td[3]')
            # print(table_element_one.text)
            found_values[i].append(table_element_one.text)
            # print(table_element_two.text)
            found_values[i].append(table_element_two.text)

        part_button = driver.find_element_by_xpath('//*[@id="interchange"]/tbody/tr[1]/td[1]')
        part_button.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="part_number"]/tbody/tr/td[1]'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        product_line = driver.find_element_by_xpath('//*[@id="part_number"]/tbody/tr/td[1]')

        for i in range(len(found_values)):
            # print(product_line.text)
            found_values[i].append(product_line.text)
    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')

    driver.quit()
    return found_values


def scraper_densoautoparts(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://densoautoparts.com/find-my-part.aspx')
    part_found = 1
    found_values = []
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.ID, "btnCrossReference"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    time.sleep(4)
    crossreference_button = driver.find_element_by_id("btnCrossReference")
    crossreference_button.click()
    try:
        element_present = EC.presence_of_element_located((By.ID, "fieldCrossReference"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    try:
        input_element = driver.find_element_by_id('fieldCrossReference')
        input_element.send_keys(part_id)
        input_element.send_keys(Keys.ENTER)
    except:
        part_found = 0

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="PartsList"]/tbody/tr[2]/td[4]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        part_found = 0
    if (part_found == 1):
        found_values.append([])
        driver.implicitly_wait(2)
        # print(part_id)
        found_values[0].append(part_id)
        part_manufacturer = driver.find_element_by_xpath('//*[@id="PartsList"]/tbody/tr[2]/td[1]')
        # print(part_manufacturer.text)
        found_values[0].append(part_manufacturer.text)
        part_manufacturer = driver.find_element_by_xpath('//*[@id="PartsList"]/tbody/tr[2]/td[2]')
        # print(part_manufacturer.text)
        found_values[0].append(part_manufacturer.text)
        part_manufacturer = driver.find_element_by_xpath('//*[@id="PartsList"]/tbody/tr[2]/td[4]')
        # print(part_manufacturer.text[:-7])
        found_values[0].append(part_manufacturer.text[:-8])
    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')

    driver.quit()
    return found_values


def scraper_carter(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://carter.opticatonline.com/')
    part_found = 1
    found_values = []
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/header/div[1]/div[2]/div/div[1]/form/div/input'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    input_element = driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/div[1]/form/div/input')
    input_element.send_keys(part_id)
    input_element.send_keys(Keys.ENTER)

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/div[2]/table/tbody/tr[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        part_found = 0

    if (part_found == 1):
        table_elements = driver.find_elements_by_xpath('/html/body/section/div/div/div[2]/table/tbody/tr')
        for i in range(len(table_elements)):
            found_values.append([])
            #print(part_id)
            found_values[i].append(part_id)
            article_number = driver.find_element_by_xpath('/html/body/section/div/div/div[2]/table/tbody/tr['+str(i+1)+']/td[3]/a')
            #print(article_number.text)
            found_values[i].append(article_number.text)
            desired_values = driver.find_elements_by_xpath('/html/body/section/div/div/div[2]/table/tbody/tr['+str(i+1)+']/td[5]/div')
            j=0
            for value in desired_values:
                j+=1
                if('OE' in value.text):
                    #print(value.text)
                    found_values[i].append(value.text[11:])
                if(j==1):
                    print(value.text)
                    found_values[i].append(value.text)
    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')

    driver.quit()
    return found_values


def scraper_opticat(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://www.opticatonline.com/')
    part_found = 1
    found_values = []
    timeout = 10
    time.sleep(5)
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, '/html/body/header/div[1]/div[2]/div/div[1]/form/div/input'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    input_element = driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/div[1]/form/div/input')
    input_element.send_keys(part_id)
    input_element.send_keys(Keys.ENTER)

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/div[2]/table/tbody/tr'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        part_found = 0

    if (part_found == 1):
        table_elements = driver.find_elements_by_xpath('/html/body/section/div/div/div[2]/table/tbody/tr')

        for i in range(len(table_elements)):
            found_values.append([])
            # print(part_id)
            found_values[i].append(part_id)
            article_number = driver.find_element_by_xpath(
                '/html/body/section/div/div/div[2]/table/tbody/tr[' + str(i + 1) + ']/td[4]/a')
            # print(article_number.text)
            found_values[i].append(article_number.text)
            desired_values = driver.find_elements_by_xpath(
                '/html/body/section/div/div/div[2]/table/tbody/tr[' + str(i + 1) + ']/td[6]/div')
            j = 0
            for value in desired_values:
                j += 1
                if ('OE' in value.text):
                    # print(value.text)
                    found_values[i].append(value.text[11:])
                if (j == 1):
                    # print(value.text)
                    found_values[i].append(value.text)

    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')

    driver.quit()
    return found_values


def scraper_standard(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://ecatalog.smpcorp.com/std/#/vehicles')
    part_found = 1
    found_values = []
    timeout = 10
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="header-view"]/div[3]/input[2]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    checkbox = driver.find_element_by_xpath('//*[@id="header-view"]/div[3]/input[2]')
    checkbox.click()

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="header-view"]/div[3]/input[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    input_element = driver.find_element_by_xpath('//*[@id="header-view"]/div[3]/input[1]')
    input_element.send_keys(part_id)
    input_element.send_keys(Keys.ENTER)

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="catFilterContainer"]/li/a/span'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        part_found = 0
        print("Timed out waiting for page to load")

    if (part_found == 1):
        # print(part_id)
        part_type = driver.find_element_by_xpath('//*[@id="catFilterContainer"]/li/a/span')
        # print(part_type.text)
        table_elements = driver.find_elements_by_xpath(
            '//*[@id="searchresults-view"]/div[3]/div/div/div[2]/div[2]/ul/li')
        for i in range(len(table_elements)):
            found_values.append([])
            found_values[i].append(part_id)
            found_values[i].append(part_type.text)
            mfg_part = driver.find_element_by_xpath(
                '//*[@id="searchresults-view"]/div[3]/div/div/div[2]/div[2]/ul/li[' + str(
                    i + 1) + ']/div[2]/div[1]/a/span')
            # print(mfg_part.text)
            found_values[i].append(mfg_part.text)
            product = driver.find_element_by_xpath(
                '//*[@id="searchresults-view"]/div[3]/div/div/div[2]/div[2]/ul/li[' + str(
                    i + 1) + ']/div[2]/div[1]/span[2]')
            # print(product.text)
            found_values[i].append(product.text)
            manufacturer = driver.find_element_by_xpath(
                '//*[@id="searchresults-view"]/div[3]/div/div/div[2]/div[2]/ul/li[' + str(
                    i + 1) + ']/div[2]/div[2]/small[2]/span')
            # print(manufacturer.text)
            found_values[i].append(manufacturer.text)
    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')

    driver.quit()
    return found_values


def scraper_BWD(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://www.bwdbrand.com/en')
    part_found = 1
    found_values = []
    timeout = 15
    if len(part_id)>3:
        try:
            element_present = EC.presence_of_element_located(
                (By.XPATH, '//*[@id="dynEcat"]/div/div[2]/div[2]/div[2]/div/input'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        input_element = driver.find_element_by_xpath('//*[@id="dynEcat"]/div/div[2]/div[2]/div[2]/div/input')
        driver.save_screenshot("opticat.png")

        input_element.send_keys(part_id)
        driver.save_screenshot("opticat1.png")

        input_element.send_keys(Keys.ENTER)
        driver.save_screenshot("opticat.png")
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_id("eCatFrame"))

        try:
            element_present = EC.presence_of_element_located((By.XPATH,'//*[@id="eCat"]/div/section/div/div[1]/div/div[4]/div[2]/div[1]/div[1]/div[2]/a/p'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            part_found = 0
            print("Timed out waiting for page to load")
        if (part_found == 1):
            time.sleep(2)
            #print(part_id)
            table_elements = driver.find_elements_by_xpath('//*[@id="eCat"]/div/section/div/div[1]/div/div[4]/div[2]/div[1]/div')
            for i in range(len(table_elements)):
                found_values.append([])
                found_values[i].append(part_id)
                mfg_part = driver.find_element_by_xpath('//*[@id="eCat"]/div/section/div/div[1]/div/div[4]/div[2]/div[1]/div['+str(i+1)+']/div[2]/a/p')
                #print(mfg_part.text)
                found_values[i].append(mfg_part.text)
                product_type = driver.find_element_by_xpath('//*[@id="eCat"]/div/section/div/div[1]/div/div[4]/div[2]/div[1]/div['+str(i+1)+']/div[2]/div[1]/p')
                #print(product_type.text)
                found_values[i].append(product_type.text)
                manufacturer = driver.find_element_by_xpath('//*[@id="eCat"]/div/section/div/div[1]/div/div[4]/div[2]/div[1]/div['+str(i+1)+']/div[2]/div[5]/ul/li[1]/span[2]')
                #print(manufacturer.text)
                found_values[i].append(manufacturer.text)
                product_number = driver.find_element_by_xpath('//*[@id="eCat"]/div/section/div/div[1]/div/div[4]/div[2]/div[1]/div['+str(i+1)+']/div[2]/div[5]/ul/li[2]/span[2]')
                #print(product_number.text)
                found_values[i].append(product_number.text)
        else:
            found_values.append([])
            found_values[0].append(part_id)
            found_values[0].append('Nothing found.')

    driver.quit()
    return found_values


def scraper_WVE(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://wvebrand.com/parts/')
    item_found = 1
    found_values = []
    timeout = 10
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="XPART_NO"]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    input_element = driver.find_element_by_xpath('//*[@id="XPART_NO"]')
    input_element.send_keys(part_id)
    input_element.send_keys(Keys.ENTER)

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="products-0"]/div/table/tbody/tr/th[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        item_found = 0
        print("Timed out waiting for page to load")

    if (item_found == 1):
        found_values.append([])
        # print(part_id)
        found_values[0].append(part_id)
        brand = driver.find_element_by_xpath('//*[@id="products-0"]/div/table/tbody/tr/th[1]')
        # print(brand.text)
        found_values[0].append(brand.text)
        number = driver.find_element_by_xpath('//*[@id="products-0"]/div/table/tbody/tr/th[2]')
        # print(number.text)
        found_values[0].append(number.text)
        wve = driver.find_element_by_xpath('//*[@id="products-0"]/div/table/tbody/tr/td[1]/a')
        # print(wve.text)
        found_values[0].append(wve.text)
        description = driver.find_element_by_xpath('//*[@id="products-0"]/div/table/tbody/tr/td[2]')
        # print(description.text)
        found_values[0].append(description.text)
    else:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')

    driver.quit()
    return found_values




def scraper_oreillyautoparts(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://www.oreillyauto.com/search/cross-reference?q={0}'.format(part_id))
    part_found = 1
    found_values = []
    timeout = 10
    time.sleep(10)

    # try:
    # print("hiiiiiiiiiiiiiiiiiiiiiiiiii")
    # interchange= driver.find_element_by_xpath('body > div.site-container > div > div.row.js-product-list > div.main-primary.col-md-9 > div > div > div.plp-header > div.interchange-banner > a')
    # interchange.click()
    # print("nnnnnnnnnnnnnnnnnnnn")
    # time.sleep(7)
    try:
        name = driver.find_elements_by_class_name('js-product-name')
        linecode = driver.find_elements_by_class_name('line-code')
        item_number = driver.find_elements_by_class_name('item-number')
        replaced = driver.find_elements_by_class_name('manufacturer-replacement')

        for it, na, line, rep in zip(item_number, name, linecode, replaced):
            data = []
            data.append(part_id)
            data.append(it.text)
            data.append(na.text)
            data.append(line.text)
            print(it.text)
            print(na.text)
            print(line.text)
            atag = rep.find_elements_by_tag_name('a')
            repp = ""
            for a in atag:
                atext = a.text
                repp = atext + repp

            data.append(repp)
            found_values.append(data)

        # found_values.append([])
        # #print(part_id)
        # found_values[0].append(part_id)
        # description = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/article/div[2]/div[1]/h2/a')
        # #print(description.text)
        # found_values[0].append(description.text)
    except:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')

    driver.quit()
    return found_values






def scraper_autozone(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://www.autozone.com/')
    driver.delete_all_cookies()
    a = driver.find_element_by_id('deskTopSearchInput')
    a.send_keys(part_id)
    a.send_keys(Keys.ENTER)

    part_found = 1
    found_values = []
    timeout = 10
    print("hooo")
    time.sleep(11)

    try:
        print("kkkkkkkk")
        try:
            tick = driver.find_element_by_xpath('//*[@id="bx-element-1063397-UabrI5x"]/button')
            print("ddoooo")
            tick.click()
        except:
            pass
            print("bobobobobob")
        time.sleep(4)
        image = driver.find_element_by_css_selector('#search-result-list > article > a > div> img')
        print("llllllllllllllllllllllllll")
        a = image.click()
        time.sleep(4)
        driver.save_screenshot("hello12.png")
        names = driver.find_elements_by_xpath('//*[@id="productTitle"]')
        price = driver.find_elements_by_xpath('//*[@id="priceContainer"]/div[1]/div[2]')
        print(price)
        p = ([p.text for p in price])
        print(p)
        price = list(filter(None, p))
        print(price)

        for na, price in zip(names, price):
            data = []
            name = na.text
            part = name.split(' ')[-1]
            data.append(part_id)
            data.append(part)
            data.append(name)
            data.append("$" + price)
            found_values.append(data)
    except:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')
    driver.quit()
    return found_values


def scraper_advanceautoparts(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    driver.get('https://shop.advanceautoparts.com/')
    driver.delete_all_cookies()

    part_found = 1
    found_values = []
    timeout = 10
    try:
        input_element = driver.find_element_by_xpath('//*[@id="aap-primary-search-input"]')
        input_element.send_keys(part_id)
        input_element.send_keys(Keys.ENTER)
        time.sleep(3)
        prices = driver.find_elements_by_class_name('red-price')
        href_links=driver.find_elements_by_class_name('pdp-link')
        parts= []
        for sd in href_links:
            url =sd.get_attribute('href')
            part = url.split("/")[-2]
            part = part.split('-')[-1]
            parts.append(part)

        bigname = driver.find_elements_by_class_name('aap-pl-item__pname--h1')
        smallname = driver.find_elements_by_class_name('aap-pl-item__pname--h2')


        for b, s, pa, pc in zip(bigname, smallname, parts, prices):
            data = []
            name = b.text + " " + s.text
            part = pa
            price = pc.text
            data.append(part_id)
            data.append(part)
            data.append(name)
            data.append(price)
            found_values.append(data)

    except:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')
    driver.quit()
    return found_values



def webscraper_nepalonline(part_id):
    driver = webdriver.Firefox(firefox_options=chrome_options)
    part_found = 1
    found_values = []
    timeout = 10
    try:
        driver.get('https://www.napaonline.com/en/search?text={0}&isInterchange=true&referer=interchange'.format(part_id))
        time.sleep(3)
        parts = driver.find_elements_by_class_name('listing-detail-text-part')
        oe = driver.find_elements_by_class_name('listing-detail-text-product')
        name = driver.find_elements_by_class_name('ada-plp-h2-to-a-adjustment')
        pclass = "listing-price-value"
        prices = driver.find_elements_by_class_name(pclass)
        for pa ,na ,o,pr in zip(parts,name,oe,prices):
            data=[]
            data.append(part_id)
            data.append(pa.text)
            data.append(na.text)
            data.append(o.text)
            data.append(pr.text)
            found_values.append(data)

    except:
        found_values.append([])
        found_values[0].append(part_id)
        found_values[0].append('Nothing found.')
    driver.quit()
    return found_values


