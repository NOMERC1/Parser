from parser import scrape_books_info, write_to_excel

book_info_list = scrape_books_info()
write_to_excel(book_info_list)