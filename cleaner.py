# cleaner.py

import csv
from config import UNWANTED_TERMS

def read_terms(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        terms = [row[0] for row in reader]
    return terms

def filter_terms(terms, unwanted_terms):
    return [term for term in terms if all(unwanted not in term for unwanted in unwanted_terms)]

def write_terms(file_path, terms):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for term in terms:
            writer.writerow([term])
