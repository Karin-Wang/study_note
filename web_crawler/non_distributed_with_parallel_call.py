import concurrent.futures
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"====Error fetching {url}: {str(e)}=======")
        return None

def extract(html_content, base_url):
    links = []
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a', href=True):
            url = urljoin(base_url, link['href'])
            links.append(url)
    except Exception as e:
        print(f"======Error parsing links: {str(e)}======")
    return links

def crawl(start_url, max_depth, max_workers=5):
    visited = set()
    to_visit = [(start_url, 0)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        while to_visit:
            curr, depth = to_visit.pop(0)

            if depth > max_depth:
                continue

            if curr not in visited:
                print(f"Meow Meow crawling {curr} at depth {depth}")

                html_content = fetch(curr)
                if html_content:
                    visited.add(curr)
                    print(html_content)
                    links = extract(html_content, curr)
                    to_visit.extend([(link, depth + 1) for link in links])

if __name__ == "__main__":
    start_url = "https://howhttps.works/why-do-we-need-https/"  
    max_depth = 2  
    max_workers = 5  

    crawl(start_url, max_depth, max_workers)
