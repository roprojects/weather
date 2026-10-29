import asyncio
from datetime import datetime
from playwright.async_api import async_playwright

async def take_screenshots(pages_list):
    async with async_playwright() as p:
        # Uruchomienie przeglądarki w tle
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Ustawienie domyślnej rozdzielczości ekranu
        await page.set_viewport_size({"width": 1280, "height": 1000})

        for site in pages_list:
            url = site["url"]
            locator = site["locator"]
            path = site["path"]

            try:
                print(f"Otwieranie strony: {url}...")
                await page.goto(url, wait_until="networkidle", timeout=60000)

                # Dodatkowe krótkie czekanie na animacje / wyrenderowanie skryptów
                await page.wait_for_timeout(5000)

                if locator is None:
                    # Pobieranie zrzutu całej strony
                    await page.screenshot(path=path, full_page=True)
                    print(f" Zapisano całą stronę jako: {path}")
                else:
                    # Pobieranie zrzutu tylko dla wybranego selektora
                    element = page.locator(locator)

                    # Sprawdzenie czy element istnieje na stronie przed wykonaniem zrzutu
                    if await element.count() > 0:
                        if path == "meteo.jpg":
                            element2 = page.locator("button.fc-button")

                            if await element2.count() > 0:
                                await element2.click()

                            element2 = page.locator("span.tutorial__btn--skip")

                            if await element2.count() > 0:
                                await element2.click()

                            element2 = page.locator("button.cmplz-deny")

                            if await element2.count() > 0:
                                await element2.click()

                        await element.screenshot(path=path)
                        print(f" Zapisano wycięty element '{locator}' jako: {path}")
                    else:
                        print(f" Błąd: Nie znaleziono selektora '{locator}' na stronie {url}")

            except Exception as e:
                print(f" Wystąpił błąd podczas przetwarzania {url}: {e}")

        await browser.close()

now = datetime.now()
d = now.strftime("%Y-%m-%d-%H-%M")

# Definicja listy stron do przetworzenia
pages = [
    {"url": "https://www.yr.no/en/forecast/daily-table/2-3099230/Poland/Silesian%20Voivodeship/Gliwice/Gliwice", "locator": "#forecast-page__table", "path": "forecast_temp.jpg"},
    {"url": "https://www.yr.no/en/forecast/graph/2-3099230/Poland/Silesian%20Voivodeship/Gliwice/Gliwice", "locator": "#forecast-page__graph", "path": "forecast_temp2.jpg"},
    {"url": "https://embed.windy.com/embed2.html?lat=52.536&lon=20.479&zoom=6&level=surface&overlay=snowcover&menu=&message=false&marker=false&calendar=&pressure=false&type=map&location=coordinates&detail=&detailLat=55.003&detailLon=24.170&metricWind=default&metricTemp=default&radarRange=-1", "locator": None, "path": "snow.jpg"},
    {"url": "https://www.met.ie/latest-reports/satellites/europe-visible", "locator": ".satellites-container", "path": f"sat_{d}.jpg"},
    {"url": "https://www.met.ie/latest-reports/satellites/europe-infrared-radar", "locator": ".satellites-container", "path": f"sat2_{d}.jpg"},
    {"url": "https://www.meteo.pl/meteogramy?lat=50.3086154&lng=18.7863749", "locator": ".meteograms-box", "path": "meteo.jpg"}
]

# Uruchomienie skryptu
asyncio.run(take_screenshots(pages))
