from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import time
import pandas as pd

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

URL = ["https://secim.ntv.com.tr/adana-secim-sonuclari"]

df_final = pd.DataFrame()
for x in URL:
    driver.get(x)
    wait = WebDriverWait(driver, 2)
    combobox = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[3]/div[2]/ng-select/div/div/div[3]")))
    for i in range (1, 82):
        combobox.click()
        select_sehir = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[{i}]/span")))
        select_sehir.click()
        time.sleep(3)
        sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2"))).text
        secmen = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[4]/div/div[2]/div"))).text
        oy = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[5]/div/div[2]/div"))).text
        gecerli_oy = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[1]/div[6]/div/div[2]/div"))).text
        belediye_button_1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[3]/ul/li[1]/button"))
        )
        belediye_button_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[4]/div[2]/ul/li[1]/button"))
        )
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
        'sehir': sehir,
        'secmen': secmen,
        'oy': oy,
        'gecerli_oy': gecerli_oy
        })
        belediye_button_1.click()
        for i in range(1, 10):
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]"))):
                    sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2"))).text
                    sira = i
                    parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]"))).text
                    oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[2]/span"))).text
                    alinan_bel = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]/span"))).text

                    ö_bel_data.append({
                        'sira': sira,
                        'veri': "belediye başkanlığı alınan ilçeler",
                        'sehir': sehir,
                        'parti': parti,
                        'oy': oy,
                        'alinan_bel': alinan_bel
                    })
            except NoSuchElementException:
                print(f"No element found for row {i}")
                break
            except TimeoutException:
                print(f"Element not loaded for row {i}")
                break
            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Retrying...")
                continue
        belediye_button_2.click()    
        for i in range(1, 100):
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]"))):
                    sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2"))).text
                    sira = i
                    try:
                        parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[1]/span/a"))).text
                    except NoSuchElementException:
                        parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[1]/span/span"))).text
                    aday = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[2]/a"))).text
                    oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[3]"))).text
                    oran = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[4]"))).text
                    oy_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[5]"))).text
                    oran_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]/td[6]"))).text

                    bel_data.append({
                        'sira': sira,
                        'veri': "belediye başkanlığı",
                        'sehir': sehir,
                        'parti': parti,
                        'aday': aday,
                        'oy': oy,
                        'oran': oran,
                        'oy_2019': oy_2019,
                        'oran_2019': oran_2019
                    })
            except NoSuchElementException:
                print(f"No element found for row {i}")
                break
            except TimeoutException:
                print(f"Element not loaded for row {i}")
                break
            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Retrying...")
                continue
        meclis_button_1.click()
        for i in range(1, 10):
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[1]/div/div/div[2]/div/table/tbody/tr[{i}]"))):
                    sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2"))).text
                    sira = i
                    parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[2]/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]"))).text
                    oy = wait.until(EC.presence_of_element_located((By.XPATH, f"//html/body/app-root/main/div/app-city/div[3]/div[3]/div[2]/div/div/div[2]/div/table/tbody/tr[{i}]/td[2]/span"))).text
                    alinan_bel = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[3]/div[3]/div[2]/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]/span"))).text

                    ö_mec_data.append({
                        'sira': sira,
                        'veri': "meclisi alınan ilçeler",
                        'sehir': sehir,
                        'parti': parti,
                        'oy': oy,
                        'alinan_bel': alinan_bel
                    })
            except NoSuchElementException:
                print(f"No element found for row {i}")
                break
            except TimeoutException:
                print(f"Element not loaded for row {i}")
                break
            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Retrying...")
                continue
        meclis_button_2.click()
        for i in range(1, 100):    
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[1]/div/table/tbody/tr[{i}]"))):
                    sehir = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/main/div/app-city/div[2]/div[1]/h2"))).text
                    sira = i
                    parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[1]/span/a"))).text
                    oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[2]"))).text
                    oran = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[3]"))).text
                    oy_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[4]"))).text
                    oran_2019 = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[4]/div[2]/div/div[2]/div/table/tbody/tr[{i}]/td[5]"))).text
                    
                    mec_data.append({
                        'sira': sira,
                        'veri': "il meclisi",
                        'sehir': sehir,
                        'parti': parti,
                        'oy': oy,
                        'oran': oran,
                        'oy_2019': oy_2019,
                        'oran_2019': oran_2019
                    })
            except NoSuchElementException:
                print(f"No element found for row {i}")
                break
            except TimeoutException:
                print(f"Element not loaded for row {i}")
                break
            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Retrying...")
                continue
        for i in range(1, 100):    
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[1]/th/a"))):
                    sira = i
                    ilce = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/th/a"))).text
                    parti = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[1]/span"))).text
                    aday = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[2]"))).text
                    oy = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[3]"))).text
                    oran = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/main/div/app-city/div[5]/div[2]/div/table/tbody/tr[{i}]/td[4]"))).text
                    
                    ilce_data.append({
                        'sira': sira,
                        'veri': "ilce",
                        'sehir': sehir,
                        'ilce': ilce,
                        'parti': parti,
                        'aday': aday,
                        'oy': oy,
                        'oran': oran,
                    })
            except NoSuchElementException:
                print(f"No element found for row {i}")
                break
            except TimeoutException:
                print(f"Element not loaded for row {i}")
                break
            except StaleElementReferenceException:
                print("StaleElementReferenceException encountered. Retrying...")
                continue
        df_seh = pd.DataFrame(seh_data)
        df_ö_bel = pd.DataFrame(ö_bel_data)
        df_bel = pd.DataFrame(bel_data)
        df_ö_mec = pd.DataFrame(ö_mec_data)
        df_mec = pd.DataFrame(mec_data)
        df_ilce = pd.DataFrame(ilce_data)

        df_all = pd.concat([df_seh, df_ö_bel, df_bel, df_ö_mec, df_mec, df_ilce], keys=['seh', 'ö_bel','bel', 'ö_mec', 'mec', 'ilce'])
        df_final = pd.concat([df_final, df_all])
df_final.to_csv('secim_data.csv', index=False)

time.sleep(2)

driver.quit()