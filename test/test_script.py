from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Setup headless Chrome browser
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Load local HTML file
    file_path = os.path.abspath("contact.html")  # Adjust path if needed
    driver.get("file://" + file_path)
    time.sleep(2)

    # Find all contact links
    links = driver.find_elements(By.CSS_SELECTOR, ".contact-links a")

    # Validate Phone Link
    phone_link = links[0].get_attribute("href")
    assert phone_link.startswith("tel:+918870798720"), f"❌ Phone link invalid: {phone_link}"
    print("✅ Phone link is valid.")

    # Validate Instagram Link
    insta_link = links[1].get_attribute("href")
    assert "instagram.com/srinivasan.sriraman23" in insta_link, f"❌ Instagram link invalid: {insta_link}"
    print("✅ Instagram link is valid.")

    # Validate WhatsApp Link
    whatsapp_link = links[2].get_attribute("href")
    assert whatsapp_link.startswith("https://wa.me/918870798720"), f"❌ WhatsApp link invalid: {whatsapp_link}"
    print("✅ WhatsApp link is valid.")

except Exception as e:
    print("❌ Test failed:", e)

finally:
    driver.quit()
