import time

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch()

page = browser.new_page()

page.goto("https://www.meteoprog.com/review/Glivitse/")

time.sleep(1)

page.locator("#pt-accept-all").click()

time.sleep(1)

page.locator(".weather-day-by-day-slider").screenshot(path=f"forecast_temp.jpg")

#page.goto("https://www.google.com/search?q=weather+gliwice")

#time.sleep(1)

#page.locator("#W0wltc").click()

#time.sleep(1)

#page.locator("#wob_wc").screenshot(path=f"forecast_temp2.jpg")

#page.locator("#wob_rain").click()
#page.locator("#wob_wc").screenshot(path=f"forecast_rain.jpg")

#page.locator("#wob_wind").click()
#page.locator("#wob_wc").screenshot(path=f"forecast_wind.jpg")

page.goto("https://radioaktywnosc-pomiary.umcs.lublin.pl/wykresy_front/wykresy_podstawowe/wykresy.php")
page.locator("#canvasMoc").screenshot(path=f"radiation.jpg")

page.goto("https://embed.windy.com/embed2.html?lat=52.536&lon=20.479&zoom=6&level=surface&overlay=snowcover&menu=&message=false&marker=false&calendar=&pressure=false&type=map&location=coordinates&detail=&detailLat=55.003&detailLon=24.170&metricWind=default&metricTemp=default&radarRange=-1")
page.screenshot(path=f"snow.jpg")

browser.close()
playwright.stop()
