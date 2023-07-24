import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
from tqdm import tqdm
import os

def get_xs_links(url):
    http = httplib2.Http(disable_ssl_certificate_validation=True)
    s, r = http.request(url)
    xs_links = []
    soup = BeautifulSoup(r, 'html.parser')
    for link in soup.find_all('img'):
        tmp = link.get('src')
        if 'get' in tmp:
            xs_links.append(tmp)
    return xs_links

def get_links_from_yandex(search_url, total_pages):
    links = []
    for i in tqdm(range(total_pages)):
        page_url = search_url.format(i)
        xs_links = get_xs_links(page_url)
        orig_links = [link[:-2] + 'orig' for link in xs_links]
        links += orig_links
    return links


models1 = {
    'iPhone'
    'samsug galaxy'
    'realme'
}


path = 'files/{}/'
for model, conf in models1.items():
    os.makedirs(path.format(model), exist_ok=True)
    links = get_links_from_yandex(*conf)
    with open(path.format(model) + model + '.txt', 'w') as out:
        for link in links:
            out.write(link + '\n')



path = 'files/{}/'
for model, conf in models2.items():
    os.makedirs(path.format(model), exist_ok=True)
    links = get_links_from_yandex(*conf)
    with open(path.format(model) + model + '.txt', 'w') as out:
        for link in links:
            out.write(link + '\n')






