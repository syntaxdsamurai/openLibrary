# 📚 Open Library Pipeline

A Python data pipeline that fetches book data from the Open Library API, cleans it, and saves the output as both CSV and Parquet.

Built as part of my Data Engineering learning journey — no pandas, no shortcuts, pure Python.

---

## What it does

- Hits the [Open Library Search API](https://openlibrary.org/developers/api)
- Paginates through n pages of results automatically
- Cleans the raw response — keeps only useful fields, handles missing data gracefully
- Saves the final output as **CSV** and **Parquet**
- Prints a run summary

---

## Why Parquet?

CSV is fine for sharing. Parquet is what production DE pipelines actually use.

- Columnar storage → faster analytical queries
- Compressed by default → smaller file size
- Schema-aware → no guessing data types

---

## Project Structure

```
openLibrary/
├── extractor.py      # API calls + pagination
├── processor.py      # cleaning + saving CSV/Parquet
├── main.py           # entry point, user input, summary
├── requirements.txt
└── .gitignore
```

---

## How to run

```bash
# Clone the repo
git clone https://github.com/syntaxdsamurai/openLibrary.git
cd openLibrary

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

You'll be prompted to enter:
- Topic to search (e.g. `cricket`, `machine learning`, `cloud`)
- Number of pages to fetch
- Output filename

---

## Output fields

| Field | Description |
|---|---|
| `title` | Book title |
| `author_name` | Author(s) |
| `first_publish_year` | Year first published |
| `language` | Available languages |
| `edition_count` | Number of editions (popularity proxy) |

---

## Tech stack

- Python 3.14
- `requests` — API calls
- `pyarrow` — Parquet read/write
- `csv` — CSV read/write (stdlib)

---

## Part of a larger roadmap

This is Project 3 in my DE learning stack:

| # | Project | Stack |
|---|---|---|
| 1 | [F1 Race Pipeline](https://github.com/syntaxdsamurai/f1-pipeline) | Python, FastF1 |
| 2 | [IPL Auction Simulator](https://github.com/syntaxdsamurai/ipl-auction) | Python, OOP |
| 3 | Open Library Pipeline | Python, APIs, Parquet |
| 4 | Hinglish Sentiment Pipeline | Python, Pandas *(coming soon)* |
| 5 | Capstone: F1 → BigQuery → Airflow | GCP, Airflow, dbt *(coming soon)* |

---

## Connect

[LinkedIn](https://www.linkedin.com/in/) • [GitHub](https://github.com/syntaxdsamurai)
