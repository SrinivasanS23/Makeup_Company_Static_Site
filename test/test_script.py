from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

# ==== ChromeDriver Setup ====
driver_path = r"D:\selenium driver\Chrome Driver\chromedriver-win64\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')        # Headless mode (no GUI)
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # ==== Load local HTML file ====
    file_path = os.path.abspath("contact.html")
    driver.get("file://" + file_path)
    time.sleep(2)

    # ==== Find all links in .contact-links ====
    links = driver.find_elements(By.CSS_SELECTOR, ".contact-links a")

    # ==== Validate Phone Link ====
    phone_link = links[0].get_attribute("href")
    assert phone_link.startswith("tel:+918870798720"), f"Phone link is invalid: {phone_link}"
    print("Phone link is valid.")

    # ==== Validate Instagram Link ====
    insta_link = links[1].get_attribute("href")
    assert "instagram.com/srinivasan.sriraman23" in insta_link, f"Instagram link is invalid: {insta_link}"
    print("Instagram link is valid.")

    # ==== Validate WhatsApp Link ====
    whatsapp_link = links[2].get_attribute("href")
    assert whatsapp_link.startswith("https://wa.me/918870798720"), f"WhatsApp link is invalid: {whatsapp_link}"
    print("WhatsApp link is valid.")

except Exception as e:
    print("Test failed:", e)

finally:
    driver.quit()
