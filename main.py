import parser

if __name__ == "__main__":
    book_info_list = parser.scrape_books_info()
    parser.write_to_excel(book_info_list)