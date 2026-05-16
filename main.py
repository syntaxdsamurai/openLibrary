from extractor import fetch_books
from processor import clean_books,save_as_csv,save_as_parquet

topic = input('Enter the topic name: ')
page =  int(input('Enter the amount of search pages: '))
filename = input('Enter Filename you want to store it in: ')


raw = fetch_books(topic,page)
clean = clean_books(raw)

save_as_csv(clean,filename)
save_as_parquet(clean,filename)

