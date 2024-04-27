from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = ["https://secim.ntv.com.tr/adana-secim-sonuclari"]

df_final = pd.DataFrame()
for x in URL:
    driver.get(x)
    wait = WebDriverWait(driver, 20)
    meclis_button_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[4]/div[2]/ul/li[2]/button"))
    )
    meclis_button_1.click()
    parti = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/a")))
    print(parti.text)
time.sleep(5)

driver.quit()