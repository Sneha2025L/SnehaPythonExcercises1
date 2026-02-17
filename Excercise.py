import argparse, json, os, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openai
import traceback

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")


def scrape_amazon(query):
    options = webdriver.ChromeOptions()
    # Headless removed for visible browser
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.amazon.com/s?k={query}")
    wait = WebDriverWait(driver, 10)
    products = []

    try:
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-search-result")))
        items = driver.find_elements(By.CSS_SELECTOR, "div.s-search-result[data-component-type='s-search-result']")[:5]

        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, "h2 span").text
                url = item.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                try:
                    price = item.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                except:
                    price = None
                try:
                    rating = item.find_element(By.CSS_SELECTOR, ".a-icon-alt").text
                except:
                    rating = None

                products.append({"title": title, "price": price, "rating": rating, "url": url})
            except:
                continue
    except:
        pass
    finally:
        driver.quit()

    return products


def fallback_fake_store():
    r = requests.get("https://fakestoreapi.com/products")
    items = r.json()[:5]
    return [{
        "title": i["title"],
        "price": i["price"],
        "rating": i.get("rating", {}).get("rate"),
        "url": f"https://fakestoreapi.com/products/{i['id']}"
    } for i in items]


def enhance_with_ai(products):
    for p in products:
        prompt = f"Categorize this product as budget, gaming, or professional: {p['title']}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=10
            )
            p["ai_category"] = response.choices[0].message.content.strip()
        except Exception as e:
            print(f"\nAI call failed for product: {p['title']}")
            traceback.print_exc()
            # Fallback: simple rule-based category
            title_lower = p["title"].lower()
            if "gaming" in title_lower:
                p["ai_category"] = "gaming"
            elif "laptop" in title_lower or "backpack" in title_lower:
                p["ai_category"] = "professional"
            else:
                p["ai_category"] = "budget"

    return products


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", default="laptops")
    args = parser.parse_args()

    data = scrape_amazon(args.query)

    if not data:
        print("Amazon blocked or no results. Using fallback API...\n")
        data = fallback_fake_store()

    enhanced = enhance_with_ai(data)
    print(json.dumps(enhanced, indent=2))
