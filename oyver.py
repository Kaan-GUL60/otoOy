import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains


hata_say = 0

# 10 defa tekrarla
for i in range(50):
    print("-----------Döngü Tur Attı----------")
    print("*******************************Tur sayısı: " , i )
    # Microsoft Edge sürücüsünü başlatma
    options = Options()
    driver = webdriver.Edge(service=Service('msedgedriver.exe'), options=options)

    # Yeni gizli sekme açma
    driver.execute_script("window.open('','_blank');")
    time.sleep(1)
    print("beklen,yor")
    driver.switch_to.window(driver.window_handles[1])  # Yeni sekme üzerine geçiş
    time.sleep(1)
    print("beklen,yor")
    # Expo.gen-e.eu sitesini açma ve 10 saniye bekletme
    driver.get("https://expo.gen-e.eu/expo")
    time.sleep(8)
    print("açılıd site")
    try:
        # 1. tuşa basma ve 4 saniye bekletme
        tuş_1 = driver.find_element(By.XPATH, '//*[@id="panorama"]/div[2]/div[1]')
        tuş_1.click()
        time.sleep(3)
        print("ja ya basıldı")

        # 2. tuşa basma ve 4 saniye bekletme
        tuş_2 = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-catergories/div/div/div/div[1]/a/img')
        tuş_2.click()
        time.sleep(3)
        print("beklen,yor")

        # 3. tuşa basma ve 4 saniye bekletme
        tuş_3 = driver.find_element(By.XPATH, '//*[@id="collapseBasic"]/ul/li[39]/a')
        tuş_3.click()
        time.sleep(3)
        print("türkiye ye basdı mı,yor")
    
        # 4. tuşa basma ve 4 saniye bekletme
        tuş_4 = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-category/div/div/div/div[1]/app-pagination/nav/ul/li[2]/button')
        tuş_4.click()
        time.sleep(4)
        print("beklen,yor")

        # 5. tuşa basma ve 6 saniye bekletme
        tuş_5 = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-category/div/div/div/div[1]/div/app-items[7]/div/div[2]/a')
        tuş_5.click()
        print("beklen, 6sn yor")
        time.sleep(6)

        # 6. tuşa basma ve 4 saniye bekletme
        tuş_6 = driver.find_element(By.XPATH, '/html/body/ngb-modal-window[2]/div/div/app-item/div/div/div/a[5]/img')
        tuş_6.click()
        time.sleep(5)
    except Exception as e:
        # Belirtilen XPath ifadesine sahip öğe bulunamadığından kaynaklı hata oluştu
        print("Öğe bulunamadı!")
        print("!!!!!!!!!!!!!!BU TUR HATALI!!!!!!!!!!!!!")
        hata_say = hata_say + 1
        print("!!!!!!!!!!!!!!!HATA SAYISI---------> ",hata_say)
        
    
    print("UYGULAMA SON BULMUŞTUR")
    oy_say = i - hata_say
    print("BAŞARILI OY SAYISI------> " , oy_say)
    # Gizli sekmeyi kapatma
    driver.close()
    driver.switch_to.window(driver.window_handles[0])  # Ana sekmaya geçiş

    # Tarayıcıyı kapatma
    driver.quit()
    if i == 49:
        print("UYGULAMA SON BULMUŞTUR")
        oy_say = i - hata_say
        print("BAŞARILI OY SAYISI------> " , oy_say)
