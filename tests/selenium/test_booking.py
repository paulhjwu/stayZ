# Must consult the table in https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html 
# to identify compatible versions of geckodriver and Firefox
# In my wsl, I use the top line of the table, which is geckodriver v0.33.0 and Firefox > 102 ESR
# export DISPLAY=ip_address:0.0
# export LIBGL_ALWAYS_INDIRECT=1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

def test_booking():
    service_obj = Service("/d/tars/geckodriver")
    driver = webdriver.Firefox(service=service_obj)
    driver.maximize_window()
    driver.get("localhost:5000")

    driver.find_element(By.XPATH,"//a[@href='/viewPackageDetail/Shangri-La Singapore']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "(//a[normalize-space()='Back to Packages'])[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("peter@cde.com")
    driver.find_element(By.CSS_SELECTOR, "#pwd").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "button[value='login']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '''.btn.btn-primary[href="/view?hotel_name='Shangri-La Singapore'"]''').click()

    print("Application Title: ", driver.title)
    print("Application URL: ", driver.current_url)
    # driver.quit()