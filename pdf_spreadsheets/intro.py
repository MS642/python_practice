# Libraries: Openpyxl, Pandas, Google Sheets Python API
import csv

# Open the file - need to have correct encoding depending on the data in the file
data = open('example.csv', encoding='utf-8')

# Csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

# Write to a csv
file_to_output = open('to_save_file1.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerow([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()
f = open('to_save_file1.csv', mode='a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1', '2', '3'])
f.close()

