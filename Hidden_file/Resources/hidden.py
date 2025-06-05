import requests
from bs4 import BeautifulSoup
import os
import time

BASE_URL = "http://192.168.56.101"
FLAG = "flag"

visited = set()
matching_readmes = []

session = requests.Session()

def fetch_and_parse(path):
    url = BASE_URL + path
    try:
        response = session.get(url)
        if response.status_code != 200:
            return None
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def explore(path):
    if path in visited:
        return
    visited.add(path)

    soup = fetch_and_parse(path)
    if soup is None:
        return

    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href in ["../"]:
            continue

        full_path = os.path.join(path, href)
        if href.endswith("/"):
            explore(full_path)
        elif href.lower() == "readme":
            readme_url = BASE_URL + full_path
            try:
                response = session.get(readme_url)
                time.sleep(0.0002)
                if response.status_code == 200:
                    content = response.text
                    if FLAG.lower() in content.lower():
                        matching_readmes.append((readme_url, content))
                        print(f"Found Flag in README: {readme_url, content}")
                        exit()
                    print(f"Found README: {readme_url}")
            except Exception as e:
                print(f"Failed to read {readme_url}: {e}")

if __name__ == "__main__":
    explore("/.hidden")
