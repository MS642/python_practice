# pip install requests
# pip install lxml
# pip install bs4
import requests
import bs4
import lxml


result = requests.get("http://www.example.com")
print(result.content)
print(result.text)
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup)
print(type(result))
print(soup.select('title')[0].getText())
site_paragraphs = soup.select('p')

