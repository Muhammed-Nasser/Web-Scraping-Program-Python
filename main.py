import requests
from bs4 import BeautifulSoup as bs

user = input ('Input GitHub User-Name: ')
url = 'https://github.com/'+user

r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_imge = soup.find('img',{'alt':'Avatar'})['src']
print(profile_imge)

