import requests
import bs4

# GOAL: Get titles of books wil 2 star rating

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
number_of_books = int(soup.select('form strong')[0].getText())
page = 1
books_with_rating_two = []
while number_of_books:
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    res = requests.get(base_url.format(page))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    for b in books:
        rating = b.select('.star-rating.Two')
        if len(rating):
            books_with_rating_two.append(b.select('h3 a')[0]['title'])
    page += 1
    number_of_books -= len(books)

for book in books_with_rating_two:
    print(book)
print(len(books_with_rating_two))
