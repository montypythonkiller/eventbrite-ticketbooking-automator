import names
from random import randint
import time
from selenium import webdriver
from selenium.common.exceptions import *

# import the webdriver, chrome driver is recommended
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})
driver = webdriver.Chrome(chrome_options=chrome_options)

#enter direct url to the event here
url = ""
#enter number of accounts to purchase from
num = 100

#enter how many tickets you want each purchase
tickets = 100





for i in range(num):
    driver.delete_all_cookies()    
        
    driver.get(url)
    #click Register button on main event page
    try:
        driver.find_element_by_xpath("//button[contains(@id,'eventbrite-widget-modal-trigger-')]").click()
    except UnexpectedAlertPresentException:
        time.sleep(2)
        try:
            driver.switch_to.alert.dismiss()
            print("Dismissed")
            driver.find_element_by_xpath("//button[contains(@id,'eventbrite-widget-modal-trigger-')]").click()
        except NoAlertPresentException:
            driver.find_element_by_xpath("//button[contains(@id,'eventbrite-widget-modal-trigger-')]").click()

            pass
       
    time.sleep(4)

    #click Register button on number of tickets page
    #driver.find_element_by_xpath("//div[contains(@class,'eds-modal')]").click()
    #driver.find_element_by_css_selector("div.eds-modal>button").click()
    iframe = driver.find_element_by_xpath("//iframe[contains(@id,'eventbrite-widget-modal')]")
    driver.switch_to.frame(iframe)
    #driver.find_elements_by_xpath("//button[contains(@class,'eds-btn')]")[1].click()
    driver.find_element_by_xpath("//button[contains(text(), 'Tickets')]").click()
    time.sleep(2)

    driver.find_element_by_xpath("//select[contains(@name,'ticket-quantity-selector')]").send_keys(tickets)

    driver.find_element_by_xpath("//button[contains(text(), 'Register')]").click()
    

    time.sleep(24)
    email = names.get_first_name()+names.get_last_name()+"@gmail.com"
    #enter email
    try:
        driver.find_element_by_xpath("//input[contains(@id,'buyer.N-email')]").send_keys(email)
    except ElementNotInteractableException:
        driver.find_element_by_xpath("//button[contains(@data-spec,'email-field-edit-button')]").click()
        driver.find_element_by_xpath("//input[contains(@id,'buyer.N-email')]").send_keys(email)
        
    #confirm email
    try:
        driver.find_element_by_xpath("//input[contains(@id,'buyer.confirmEmailAddress')]").send_keys(email)
    except:
        pass
    #enter first name
    driver.find_element_by_xpath("//input[contains(@id,'buyer.N-first_name')]").send_keys(names.get_first_name())
    #enter last name
    driver.find_element_by_xpath("//input[contains(@id,'buyer.N-last_name')]").send_keys(names.get_last_name())
    #enter phone number
    n = 10
    phonenum = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
    driver.find_element_by_xpath("//input[contains(@id,'buyer.N-cell_phone')]").send_keys(phonenum)

    
    time.sleep(1)
    #click final registration button
    driver.find_elements_by_css_selector("button.eds-btn")[0].click()
    time.sleep(12)
