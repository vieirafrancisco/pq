import requests
from bs4 import BeautifulSoup as Soup
from pq.job import Job

def get_site_text(url):
    html = requests.get(url)
    soup = Soup(html.text, "lxml")
    
    whitelist = [
       'p',
       'h1',
       'h2'
    ]
    text_elements = [t for t in soup.find_all(text=True) if t.parent.name in whitelist]
    return "\n".join(text_elements)

def save_site_article(path, url):
    text = get_site_text(url)
    title = url.replace("/", "-").replace(":", "")
    with open(f"{path}/{title}.txt", "w") as f:
        f.write(text)

class JobRequestSiteArticle(Job):
    def __init__(self, path, url):
        self.path = path 
        self.url = url
        
        super().__init__(save_site_article, path=path, url=url)


if __name__ == "__main__":
    print(save_site_article(".", "https://pt.wikipedia.org/wiki/Brasil"))
