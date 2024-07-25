import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# Crawling
def crawl_web(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

# Indexing
index = defaultdict(list)

def index_content(url, content):
    words = content.split()
    for word in words:
        index[word].append(url)

# Searching
def search(query):
    return index.get(query, [])

# Main function
def main():
    url = 'https://en.wikipedia.org/wiki/Abdul_Qadir_Gilani'
    page_content = crawl_web(url)
    index_content(url, page_content)
    
    query = 'Name'
    results = search(query)
    print(f"Search results for '{query}': {results}")

if __name__ == "__main__":
    main()
