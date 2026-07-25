import threading
import requests
from bs4 import BeautifulSoup

# https://docs.langchain.com/oss/python/langchain/overview
# https://docs.langchain.com/oss/python/langchain/install
# https://docs.langchain.com/oss/python/langchain/quickstart

urls = [
 '   https://docs.langchain.com/oss/python/langchain/overview',
'https://docs.langchain.com/oss/python/langchain/install',
'https://docs.langchain.com/oss/python/langchain/quickstart'
]

def fetchContent(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from URL: {url}')

threads=[]

for url in urls:
    thread = threading.Thread(target=fetchContent, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print('All Web page fetched')