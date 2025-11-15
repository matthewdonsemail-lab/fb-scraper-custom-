import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")  # Run without visible browser if possible
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.facebook.com/")

# Manually log in here via the Codespaces browser preview if needed
# (You'll handle this in Step 1 below)
input("Log in manually in the preview window, then press Enter in terminal...")

time.sleep(5)
cookies = driver.get_cookies()
pickle.dump(cookies, open("fb_cookies.pkl", "wb"))
print("Cookies saved!")
driver.quit()
