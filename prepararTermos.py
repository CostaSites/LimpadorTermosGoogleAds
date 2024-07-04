import csv

def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Skip the first three lines
        for _ in range(3):
            next(reader)

        # Process the remaining rows and write only the first column to the output file
        for row in reader:
            writer.writerow([row[0]])

input_file = 'termosEntrada.csv'
output_file = 'termosPreparados.csv'

process_csv(input_file, output_file)
