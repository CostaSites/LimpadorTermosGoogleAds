import csv
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def process_csv(input_file, output_file):
    encoding = detect_encoding(input_file)
    with open(input_file, mode='r', encoding=encoding) as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile)
        
        # Skip the first three lines
        for _ in range(3):
            next(reader)

        # Process the remaining rows, transform the text, and write only the first column to the output file
        for row in reader:
            capitalized_term = row[0].title()  # Transform each term to have each word's first letter in uppercase
            writer.writerow([capitalized_term])

input_file = 'termosEntrada.csv'
output_file = 'termosPreparados.csv'

process_csv(input_file, output_file)
