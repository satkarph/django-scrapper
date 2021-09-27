from typing import List
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
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re
from time import sleep
import requests
import urllib.parse

import time
import pandas as pd
import os
from fuzzywuzzy import fuzz

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-mMessiagueroaximized")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--headless")
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)


def next_facebook(page_source):
    file = open("myfb.html","w+")
    file.write(page_source)
    source = BeautifulSoup(page_source, 'lxml')
    followers = re.findall(r'(\d+[A-z]) followers', str(source))[0]
    address = source.findAll('div', {'class': 'rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr o8rfisnq p8fzw8mz pcp91wgn iuny7tx3 ipjc6fyt'})[1].text
    website = source.find('span', {'class': 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v b1v8xokw q66pz984 hzawbc8m'}).text
    print("addresss-----------------------")
    print(address)
    print("address----------")
    strong = source.findAll("strong")
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
    print(url)
    response = requests.get(url).json()
    if response:

        latitude = response[0]["lat"]
        longitude = response[0]["lon"]
    else:
        latitude=None
        longitude=None
    posts = len(list(strong))

    return followers,posts,address,latitude,longitude

def get_link_for_facebook(company,zip,state ):
    try:
        query1= company + " {0} {1} Facebook".format(state, zip)
        print(query1)
        driver = webdriver.Chrome( chrome_options=chrome_options)
        driver.get('https://www.google.com/')
        inp = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

        inp.send_keys(query1)
        inp.send_keys(Keys.RETURN)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        div = soup.find_all('div', class_='g')
        for d in div:
            txt = d.find('div', class_='IsZvec')
            if txt is None:
                break

            print(txt.text)
            text_to_find = "MI 48173"
            print(text_to_find)
            if text_to_find in txt.text or "Michigan" in txt.text:
                hh = d.find('h3', class_='LC20lb')
                data = hh.text.replace(' - Home | Facebook', '')
                print("dddddddddd")
                print(data)
                score = fuzz.partial_ratio(company, data)
                print(score)
            else:
                score =0
            if score > 94:
                print(data)
                link = d.find('a', href=True)['href']
                print(link)
                print("hhih")
                driver.quit()
                if "facebook" in link:
                    return link
        driver.quit()
        return None
    except:
        return None


def get_link_for_twitter(company,zip,state):
    try:
        query1=company + " {0} {1} Twitter".format(state, zip)
        print(query1)
        driver = webdriver.Chrome( chrome_options=chrome_options)
        driver.get('https://www.google.com/')
        inp = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        inp.send_keys(query1)
        inp.send_keys(Keys.RETURN)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        div = soup.find_all('div', class_='g')
        for d in div:
            txt = d.find('div', class_='IsZvec')
            print("sssssssssssssssssssss")
            text_to_find = "MI USA"
            print(text_to_find)
            if text_to_find in txt.text:
                hh = d.find('h3', class_='LC20lb')
                data = hh.text.replace(' - Home | Facebook', '')
                score = fuzz.partial_ratio(query1, data)
                print(score)
            else:
                score = 0
            if score >94:

                print(data)
                link = d.find('a', href=True)['href']
                print(link)
                return link

        driver.quit()
        return None
    except:
        return None


def get_link_for_instagram(company,zip,state):
    try:
        query1 = company + " {0} {1} Instagram".format(state,zip)
        driver = webdriver.Chrome( chrome_options=chrome_options)
        driver.get('https://www.google.com/')
        inp = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        inp.send_keys(query1)
        inp.send_keys(Keys.RETURN)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        div = soup.find_all('div', class_='g')
        for d in div:
            txt = d.find('div', class_='IsZvec')
            print(txt.text)
            text_to_find = "MI"
            print(text_to_find)
            print("----------------")
            if text_to_find in txt.text:
                hh = d.find('h3', class_='LC20lb')
                data = hh.text.replace(' - Instagram', '')
                data = re.sub("[\(\[].*?[\)\]]", "", data)
                print(data)
                print(query1)
                score = fuzz.partial_ratio(company, data)
                print(score)
                print('score')
            else:
                score=0
            if score > 92:
                print(data)
                link = d.find('a', href=True)['href']
                print(link)
                driver.quit()
                return link
        driver.quit()
        return None
    except:
        return  None

# def get_link_instagram(query):


def facebook_call(link):
    if link is not None:
        driver = webdriver.Chrome( chrome_options=chrome_options)
        driver.get('https://www.facebook.com/login.php')

        usr = 'satsphuyal@gmail.com'
        pwd = 'Nepal-1234'

        email_element = driver.find_element_by_id('email')
        email_element.send_keys(usr)  # Give keyboard input

        password_element = driver.find_element_by_id('pass')
        password_element.send_keys(pwd)  # Give password as input too

        login_button = driver.find_element_by_id('loginbutton')
        login_button.click()  # Send mouse click

        link = link.replace('m.facebook', 'facebook')
        driver.get(link)
        driver.get(link)
        driver.get(link)
        time.sleep(3)

        try:
            followers = re.findall(r'(\d+) people follow', str(driver.page_source))[0]
        except:
            lenOfPage = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            match = False
            while (match == False):
                lastCount = lenOfPage
                time.sleep(3)
                lenOfPage = driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount == lenOfPage:
                    match = True
            followers, posts, address, latitude, longitude = next_facebook(driver.page_source)
            return posts, followers, address, latitude, longitude


        try:
            loc = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div/div/span/a/span/span')


            map_loc = (loc.text)


            address = map_loc
            url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'

            response = requests.get(url).json()
            if response:
                latitude = response[0]["lat"]
                longitude = response[0]["lon"]
            else:
                latitude = None
                longitude = None
        except:
            latitude = None
            longitude = None
            address=None

        source = BeautifulSoup(driver.page_source, 'lxml')
        followers = re.findall(r'(\d+) people follow', str(driver.page_source))[0]
        print(followers)
        time.sleep(10)
        lenOfPage = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True
        source = BeautifulSoup(driver.page_source, 'lxml')
        strong = source.findAll("strong")
        posts = len(list(strong))
        print(posts)

        driver.quit()
        return posts,followers,address,latitude,longitude
    return  None,None,None,None,None



def twitter_call(link):
    if link is not None:
        try:
            driver = webdriver.Chrome( chrome_options=chrome_options)
            driver.get(link)
            time.sleep(5)
            # followers = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span').text
            source = BeautifulSoup(driver.page_source, 'lxml')
            post = driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/div').text
            post = post.replace(' Tweets', '')
            post = post.replace(',', '')
            post = int(post)
            print(post)
            # time=source.findAll("time")
            # posts= len(list(time))
            follower = re.findall(r'r-qvutc0\">(\d+)<\/span', str(source))
            follower=(follower[1])
            # print(followers)
            # print(posts)
            driver.quit()
            return post,follower
        except :
            pass
    return None,None


def instagram_call(link):
    if link is not None and "instagram" in link:
        try:
            driver = webdriver.Chrome( chrome_options=chrome_options)
            driver.get(link)
            time.sleep(5)
            a = (driver.page_source)
            file = open('ss.html', 'w', encoding='utf8')
            file.write(a)
            source = BeautifulSoup(driver.page_source, 'lxml')
            lidata = source.findAll("span", {"class": "g47SY"})
            post = lidata[0].text
            followers = lidata[1].text
            driver.quit()
            return post,followers
        except:
            pass
    return  None,None



def main_socailmedia(data):
    found_values=[]
    company = data['company']
    zip = data['zip']
    state= data['state']

    link_facebook = get_link_for_facebook(company,zip,state)
    fb_post,fb_followers,address,latitude,longitude = facebook_call(link_facebook)
    link_twitter = get_link_for_twitter(company,zip,state)
    t_post,t_follwers = twitter_call(link_twitter)
    link_instagram = get_link_for_instagram(company,zip,state)
    i_post,i_follower =instagram_call(link_instagram)

    data = [company,address,address,state,zip,None,latitude,longitude,link_facebook,fb_followers,fb_post,link_instagram,i_follower,i_post,link_twitter,t_follwers,t_post,None,None,None,None,None,None]
    found_values.append(data)
    return  found_values