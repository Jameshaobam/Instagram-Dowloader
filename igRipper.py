import requests
import re
import os
from bs4 import BeautifulSoup
import urllib.request

os.chdir('C:/Users/ZuraH/AppData/Local/Programs/Python/Python37-32')
r = requests.get(VideoWebPageLink)
soup = BeautifulSoup(r.text,'html.parser')
result = soup.find('meta', attrs={'property':'og:video:secure_url'})
link=result.get("content", None)
urllib.request.urlretrieve(link,'test.mp4')
