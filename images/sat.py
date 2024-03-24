import time

from datetime import datetime
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch()

page = browser.new_page()

now = datetime.now()
d = now.strftime("%Y-%m-%d-%H-%M")

page.goto("https://www.wunderground.com/maps/satellite/current-visible/europ")

time.sleep(1)

page.locator(".map").screenshot(path=f"sat_{d}.jpg")

page.goto("https://www.wunderground.com/maps/satellite/infrared/europ")

time.sleep(1)

page.locator(".map").screenshot(path=f"sat2_{d}.jpg")

browser.close()
playwright.stop()
