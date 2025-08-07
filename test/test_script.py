from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

# === Paths ===
driver_path = r"D:\selenium driver\Chrome Driver\chromedriver-win64\chromedriver.exe"
chrome_binary_path = r"C:\Users\srini\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\chrome.exe"  # or your actual chrome.exe path

# === Chrome options ===
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# === Driver setup ===
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    file_path = os.path.abspath("contact.html")
    driver.get("file://" + file_path)
    time.sleep(2)

    links = driver.find_elements(By.CSS_SELECTOR, ".contact-links a")

    phone_link = links[0].get_attribute("href")
    assert phone_link.startswith("tel:+918870798720"), f"Phone link is invalid: {phone_link}"
    print("Phone link is valid.")

    insta_link = links[1].get_attribute("href")
    assert "instagram.com/srinivasan.sriraman23" in insta_link, f"Instagram link is invalid: {insta_link}"
    print("Instagram link is valid.")

    whatsapp_link = links[2].get_attribute("href")
    assert whatsapp_link.startswith("https://wa.me/918870798720"), f"WhatsApp link is invalid: {whatsapp_link}"
    print("WhatsApp link is valid.")

except Exception as e:
    print("Test failed:", e)

finally:
    driver.quit()
