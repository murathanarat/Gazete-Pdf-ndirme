import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Chrome driver'ın olduğu dizini driver_path'a yazın
driver_path = "C:/chromedriver-win64/chromedriver.exe"
#İndirilecek olduğu dizini download_path'e yazın
download_path = "C:/Users/murat/Desktop/PDF"

#İndirilmek istenen yillar

        
while(True):
    try:
        bas_yil = int(input("hangi yildan indirmeye başlamak istersin : "))
        son_yil = int(input("hangi yila kadar indirmek istersin       : "))
        break
    except ValueError:
        print("Geçersiz Yil") 
    

if not os.path.exists(download_path):
    os.makedirs(download_path)
    print(download_path , " klasör oluşturuldu")

# Chrome'u başlat
options = Options()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Ana sayfaya git
base_url = "https://nek.istanbul.edu.tr/ekos/GAZETE/"
driver.get(base_url)

# Sayfanın yüklenmesini bekle (max 30 saniye)
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.popular-category.h-40")))

# Tüm gazete bağlantılarını al
gazete_links = driver.find_elements(By.CSS_SELECTOR, "a.popular-category.h-40")
gazete_link = [gazete.get_attribute("href") for gazete in gazete_links]

# Her bir linke sırayla git
for i, g_link in enumerate(gazete_link):
    
    # Eğer klasör yoksa oluştur
    directory_path = os.path.join(download_path, g_link.split("=")[-1])
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(directory_path , " klasör oluşturuldu")

    print(f"[{i+1}] {g_link} sayfasına gidiliyor...")
    driver.get(g_link)

    # Butonları bekle ve tıkla
    buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.collapsible")))

    for i in range(len(buttons)):

        if int(buttons[i].text) <= int(son_yil) and int(buttons[i].text) >= int(bas_yil):
            date_name_path = os.path.join(directory_path, buttons[i].text)
            if not os.path.exists(date_name_path):
                os.makedirs(date_name_path)
                print(date_name_path , " klasör oluşturuldu")


            print(f"[{i+1}] Butona tıklanıyor: {buttons[i].text}")
            buttons[i].click()

            # İçeriğin yüklenmesi için biraz bekle
            wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Tıklayınız")))

            # PDF bağlantılarını pdf_links e kayıt etme
            pdf_links = driver.find_elements(By.LINK_TEXT, "Tıklayınız")
            pdf_link = [link.get_attribute("href") for link in pdf_links]

            # PDF'leri indir
            for p_link in pdf_link:

                file_name = p_link.split("/")[-1]
                file_path = os.path.join(date_name_path, file_name)

                # Eğer dosya zaten varsa, indirme işlemini atla
                if os.path.exists(file_path):
                    print(f"{file_name} zaten mevcut, indirilmiyor.")
                    continue

                # İndirme işlemi
                print(f"{file_name} indiriliyor...")
                response = requests.get(p_link, verify=False)

                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"Dosya başarıyla {file_name} olarak indirildi.")
                else:
                    print(f"Dosya indirilirken bir hata oluştu: {file_name}")



# Tarayıcıyı kapat
driver.quit()
