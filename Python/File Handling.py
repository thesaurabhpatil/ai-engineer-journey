import csv

# Write text to a file
with open('example.txt', 'w') as f:
    f.write('Hello, this is a sample text.\n')

# Append text to the file
with open('example.txt', 'a') as f:
    f.write('This line is appended.\n')

# Read text from the file
with open('example.txt', 'r') as f:
    content = f.read()
    print('File Content:')
    print(content)

# Create a sample CSV file if it does not exist
with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', '30', 'New York'])
    writer.writerow(['Bob', '25', 'London'])

# Read CSV file
with open('example.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    print('CSV Content:')
    for row in reader:
        print(row)