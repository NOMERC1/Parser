import requests
from bs4 import BeautifulSoup
import openpyxl

def scrape_books_info():
    book_info_list = []
    page = 1

    while True:
        url = 'https://www.chitai-gorod.ru/search?phrase=Python&page={}'.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all("div", class_="product-title__head")
        authors = soup.find_all("div", class_="product-title__author")
        prices = soup.find_all("div", class_="product-price__value product-price__value--discount")

        if not titles:
            break

        for i in range(len(titles)):
            book_title = titles[i].text.strip()
            book_author = authors[i].text.strip() if len(authors) > i and authors[i].text.strip() else "Не указан"
            book_price = prices[i].text.strip() if i < len(prices) else "Не указана"
            book_info_list.append([book_title, book_author, book_price])
        page += 1
    return book_info_list


def write_to_excel(book_info_list):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(['Название книги', 'Автор', 'Цена'])

    for book_info in book_info_list:
        sheet.append(book_info)

    workbook.save('books_info.xlsx')
    print('Данные успешно записаны в файл books_info.xlsx')