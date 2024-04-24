from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# python aascrape2.py
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = ["https://secim.ntv.com.tr/adana-secim-sonuclari", "https://secim.ntv.com.tr/adiyaman-secim-sonuclari"]

for x in URL:
    driver.get(x)
    time.sleep(2)
    sehir = driver.find_element(By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2")
    secmen = driver.find_element(By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[4]/div/div[2]/div")
    oy = driver.find_element(By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[5]/div/div[2]/div")
    gecerli_oy = driver.find_element(By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[6]/div/div[2]/div")
    seh_data = []
    bel_data = []
    mec_data = []
    seh_data.append({
    'veri': "şehir",
    'sehir': sehir.text,
    'secmen': secmen.text,
    'oy': oy.text,
    'gecerli_oy': gecerli_oy.text
})
    bel_data.append({
    'veri': "belediye",
})
    mec_data.append({
    'veri': "meclis",
})
    for i in range(1, 10):
        try:
            if driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]"):
                sira = f"{i}"
                parti = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]")
                oy = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[2]/span")
                alinan_bel = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]/span")

                seh_data.append({
                    'sira': sira.text,
                    'parti': parti.text,
                    'aday': aday.text,
                    'oy': oy.text,
                    'oran': oran.text,
                    'oy_2019': oy_2019.text,
                    'oran_2019': oran_2019.text
                })
        except NoSuchElementException:
            print(f"No element found for row {i}")
            break
    for i in range(1, 100):
        try:
            if driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]"):
                sira = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/th")
                parti = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[1]/span/a")
                aday = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[2]/a")
                oy = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[3]")
                oran = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[4]")
                oy_2019 = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[5]")
                oran_2019 = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[6]")

                bel_data.append({
                    'veri': "belediye",
                    'sira': sira.text,
                    'parti': parti.text,
                    'aday': aday.text,
                    'oy': oy.text,
                    'oran': oran.text,
                    'oy_2019': oy_2019.text,
                    'oran_2019': oran_2019.text
                })
        except NoSuchElementException:
            print(f"No element found for row {i}")
            break
    for i in range(1, 100):
        try:
            if driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]"):
                sira = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr{i}/th")
                parti = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr{i}/td[1]/span/a")
                oy = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr{i}/td[2]")
                oran = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr{i}/td[3]")
                oy_2019 = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr{i}/td[4]")
                oran_2019 = driver.find_element(By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr{i}/td[5]")

                mec_data.append({
                    'veri': "meclis",
                    'sira': sira.text,
                    'parti': parti.text,
                    'oy': oy.text,
                    'oran': oran.text,
                    'oy_2019': oy_2019.text,
                    'oran_2019': oran_2019.text
                })
        except NoSuchElementException:
            print(f"No element found for row {i}")
            break
    # Convert lists to DataFrames
    df_seh = pd.DataFrame(seh_data)
    df_bel = pd.DataFrame(bel_data)

    # Concatenate the DataFrames
    df = pd.concat([df_seh, df_bel], axis=1)

df = pd.DataFrame(data)
print(df)

time.sleep(2)

driver.quit()