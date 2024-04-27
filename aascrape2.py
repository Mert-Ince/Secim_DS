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
    sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2")))
    secmen = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[4]/div/div[2]/div")))
    oy = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[5]/div/div[2]/div")))
    gecerli_oy = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[6]/div/div[2]/div")))
    meclis_button_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[3]/ul/li[2]/button"))
    )
    meclis_button_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[4]/div[2]/ul/li[2]/button"))
    )
    seh_data = []
    ö_bel_data = []
    bel_data = []
    ö_mec_data = []
    mec_data = []
    ilce_data = []
    seh_data.append({
    'veri': "şehir",
    'sehir': sehir.text,
    'secmen': secmen.text,
    'oy': oy.text,
    'gecerli_oy': gecerli_oy.text
})
    for i in range(1, 10):
        try:
            if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]"))):
                sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2")))
                sira = f"{i+1}"
                parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]")))
                oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[2]/span")))
                alinan_bel = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]/span")))

                ö_bel_data.append({
                    'veri': "belediye başkanlığı alınan ilçeler",
                    'sehir': sehir.text,
                    'sira': sira,
                    'parti': parti.text,
                    'oy': oy.text,
                    'alinan_bel': alinan_bel.text
                })
        except NoSuchElementException:
            print(f"No element found for row {i}")
            break
        except TimeoutException:
            print(f"Element not loaded for row {i}")
            break
    for i in range(1, 100):
        try:
            if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]"))):
                sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2")))
                sira = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/th")))
                try:
                    parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[1]/span/a")))
                except NoSuchElementException:
                    parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[1]/span/span")))
                aday = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[2]/a")))
                oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[3]")))
                oran = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[4]")))
                oy_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[5]")))
                oran_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[6]")))

                bel_data.append({
                    'veri': "belediye başkanlığı",
                    'sehir': sehir.text,
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
        except TimeoutException:
            print(f"Element not loaded for row {i}")
            break
    meclis_button_1.click()
    meclis_button_2.click()
    for i in range(1, 10):
        try:
            if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]"))):
                sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2")))
                sira = f"{i+1}"
                parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[2]/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]")))
                oy = wait.until(EC.presence_of_element_located((By.XPATH, f"//html/body/app-root/main/div/app-city/div[3]/div[3]/div[2]/div/div/div[2]/div/table/tbody/tr[{i}]/td[2]/span")))
                alinan_bel = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[2]/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]/span")))

                ö_bel_data.append({
                    'veri': "meclisi alınan ilçeler",
                    'sehir': sehir.text,
                    'sira': sira,
                    'parti': parti.text,
                    'oy': oy.text,
                    'alinan_bel': alinan_bel.text
                })
        except NoSuchElementException:
            print(f"No element found for row {i}")
            break
        except TimeoutException:
            print(f"Element not loaded for row {i}")
            break
    for i in range(1, 100):    
        try:
            if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]"))):
                sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2")))
                sira = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/th")))
                parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[1]/span/a")))
                oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[2]")))
                oran = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[3]")))
                oy_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[4]")))
                oran_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[5]")))
                
                mec_data.append({
                    'veri': "il meclisi",
                    'sehir': sehir.text,
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
        except TimeoutException:
            print(f"Element not loaded for row {i}")
            break
    for i in range(1, 100):    
        try:
            if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[1]/th/a"))):
                ilce = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/th/a")))
                parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[1]/span")))
                aday = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[2]")))
                oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[3]")))
                oran = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[4]")))
                
                ilce_data.append({
                    'veri': "ilce",
                    'sehir': sehir.text,
                    'ilce': ilce.text,
                    'parti': parti.text,
                    'aday': aday.text,
                    'oy': oy.text,
                    'oran': oran.text,
                })
        except NoSuchElementException:
            print(f"No element found for row {i}")
            break
        except TimeoutException:
            print(f"Element not loaded for row {i}")
            break
    df_seh = pd.DataFrame(seh_data)
    df_ö_bel = pd.DataFrame(ö_bel_data)
    df_bel = pd.DataFrame(bel_data)
    df_ö_mec = pd.DataFrame(ö_mec_data)
    df_mec = pd.DataFrame(mec_data)
    df_ilce = pd.DataFrame(ilce_data)

    #df_all = pd.concat([df_seh, df_bel, df_mec], keys=['seh', 'bel', 'mec'])
    df_seh.to_csv('output.csv')
    df_ö_bel.to_csv('output1.csv')
    df_bel.to_csv('output2.csv')
    df_ö_mec.to_csv('output3.csv')
    df_mec.to_csv('output4.csv')
    df_ilce.to_csv('output5.csv')
time.sleep(2)

driver.quit()