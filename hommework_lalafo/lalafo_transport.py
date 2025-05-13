import json
import requests
from bs4 import BeautifulSoup

def parsing(url, pages=1):
    try:
        result = []
        for page in range(1, pages + 1):
            page_url = f"{url}?page={page}" if page > 1 else url
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, "html.parser")

            articles = soup.find_all("article", class_="lf-ad-tile")

            for article in articles:
                title = article.find("p", class_="LFParagraph size-14  lf-ad-tile__title")
                title = title.text.strip() if title else None

                price = article.find("p", class_="LFSubHeading")
                price = price.text.strip() if price else None

                image = article.find("img")
                image = image.get('src') if image else None

                result.append({
                    "title": title,
                    "price": price,
                    "image": image
                })

        with open("lalafo_transport.json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

        print(f"Successfully added {len(result)} products from Lalafo Transport in lalafo_transport.json")

    except Exception as e:
        print(f"Error: {e}")

parsing("https://lalafo.kg/kyrgyzstan/transport", pages=1)