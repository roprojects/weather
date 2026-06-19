import time

from datetime import datetime
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch()

page = browser.new_page()

now = datetime.now()
d = now.strftime("%Y-%m-%d-%H-%M")

try:
 page.goto("https://www.met.ie/latest-reports/satellites/europe-visible")
except:
 print("Unable to visit 'https://www.met.ie/latest-reports/satellites/europe-visible'!!")
else:
 time.sleep(1)

 try:
  page.locator(".satellites-container").screenshot(path=f"sat_{d}.jpg")
 except:
  print("Unable to load sat visible image!!")

try:
 page.goto("https://www.met.ie/latest-reports/satellites/europe-infrared-radar")
except:
 print("Unable to visit 'https://www.met.ie/latest-reports/satellites/europe-infrared-radar'!!")
else:
 time.sleep(1)

 try:
  page.locator(".satellites-container").screenshot(path=f"sat2_{d}.jpg")
 except:
  print("Unable to load sat ir image!!")

browser.close()
playwright.stop()
