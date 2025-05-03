import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def setup_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def scrape_images(keyword, num_images, headless=True):
    if not os.path.exists(f"data/raw/{keyword}"):
        os.makedirs(f"data/raw/{keyword}")

    driver = setup_driver(headless)
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={keyword}"
    driver.get(search_url)

    image_urls = set()
    while len(image_urls) < num_images:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        img_tags = soup.find_all('img')
        for img in img_tags:
            if len(image_urls) >= num_images:
                break
            img_url = img.get('src')
            if img_url and img_url.startswith('http'):
                image_urls.add(img_url)

        # Scroll down to load more images
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.quit()

    for i, url in enumerate(image_urls):
        try:
            img_data = requests.get(url).content
            with open(f"data/raw/{keyword}/{keyword}_{i+1}.jpg", 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print(f"Could not download {url}: {e}")

if __name__ == "__main__":
    keyword = input("Enter keyword for scraping: ")
    num_images = int(input("How many images to scrape? "))
    scrape_images(keyword, num_images)