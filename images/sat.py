import time

from datetime import datetime
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch()

page = browser.new_page()

now = datetime.now()
d = now.strftime("%Y-%m-%d-%H-%M")

page.goto("https://www.met.ie/latest-reports/satellites/europe-visible")

time.sleep(1)

#page.get_by_role("button", name="Reject All").click()

#time.sleep(1)

page.locator(".satellites-container").screenshot(path=f"sat_{d}.jpg")

page.goto("https://www.met.ie/latest-reports/satellites/europe-infrared-radar")

time.sleep(1)

page.locator(".satellites-container").screenshot(path=f"sat2_{d}.jpg")

browser.close()
playwright.stop()
