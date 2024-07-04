# main.py

from cleaner import read_terms, filter_terms, write_terms
from config import INPUT_CSV, OUTPUT_CSV, UNWANTED_TERMS

def main():
    terms = read_terms(INPUT_CSV)
    filtered_terms = filter_terms(terms, UNWANTED_TERMS)
    write_terms(OUTPUT_CSV, filtered_terms)
    print(f"Filtered terms saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
