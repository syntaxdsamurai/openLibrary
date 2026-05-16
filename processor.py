import csv

import pyarrow as pa
import pyarrow.parquet as pq
def clean_books(data):
    return [
        {
            'title': d.get('title'),
            'author_name': d.get('author_name'),
            'first_publish_year': d.get('first_publish_year'),
            'language': d.get('language'),
            'edition_count': d.get('edition_count')
        }
        for d in data
    ]

def save_as_csv(clean,filepath):
    with open(f'{filepath}.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=['title','author_name','first_publish_year','language','edition_count'])
        writer.writeheader()
        writer.writerows(clean)

def save_as_parquet(clean,filepath):
    table = pa.Table.from_pydict({
        'title': [d['title'] for d in clean],
        'author_name': [d['author_name'] for d in clean],
        'first_publish_year': [d['first_publish_year'] for d in clean],
        'language': [d['language'] for d in clean],
        'edition_count': [d['edition_count'] for d in clean]
    })

    pq.write_table(table,f'{filepath}.parquet')