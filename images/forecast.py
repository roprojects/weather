import time

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch()

page = browser.new_page()

try:
 page.goto("https://www.meteoprog.com/review/Glivitse/")
except:
 print("Unable to load 'https://www.meteoprog.com/review/Glivitse/'!!")
else:
 time.sleep(1)

 try:
  page.locator('button:text("Accept All")').click()
 except:
  print("Unable to find 'Accept all' button!!")
 else:
  time.sleep(1)

  try:
   page.locator("#weather-temp-graph-week").screenshot(path=f"forecast_temp.jpg")
  except:
   print("Unable to find weather plot!!")

try:
 page.goto("https://radioaktywnosc-pomiary.umcs.lublin.pl/wykresy_front/wykresy_podstawowe/wykresy.php")
except:
 print("Unable to load 'https://radioaktywnosc-pomiary.umcs.lublin.pl/wykresy_front/wykresy_podstawowe/wykresy.php'!!")
else:
 time.sleep(1)

 try:
  page.locator("#canvasMoc").screenshot(path=f"radiation.jpg")
 except:
  print("Unable to find radiation plot!!")

try:
 page.goto("https://embed.windy.com/embed2.html?lat=52.536&lon=20.479&zoom=6&level=surface&overlay=snowcover&menu=&message=false&marker=false&calendar=&pressure=false&type=map&location=coordinates&detail=&detailLat=55.003&detailLon=24.170&metricWind=default&metricTemp=default&radarRange=-1")
except:
 print("Unable to load 'https://embed.windy.com/embed2.html'!!")
else:
 time.sleep(1)

 try:
  page.screenshot(path=f"snow.jpg")
 except:
  print("Unable to find snow plot!!")

browser.close()
playwright.stop()
