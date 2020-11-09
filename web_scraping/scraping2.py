import requests
import bs4

request = requests.get('https://www.wikipedia.com/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(request.text, 'lxml')
table_of_content = soup.select('.toctext')
index = 0
for item in table_of_content:
    print(index, item.getText())
    index += 1

# scrap images
request = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(request.text, 'lxml')
images = soup.select('.thumbimage')

for img in images:
    print(img)
    print(img['src'])
    request = requests.get(f"http:{img['src']}")
    print(request.content)

f = open('img.jpg', 'wb')
f.write(request.content)
f.close()
