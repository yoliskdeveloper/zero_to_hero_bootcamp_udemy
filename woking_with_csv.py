# supporting library to work with csv:
# pandas, Openpyxl, Google sheets Python API
import csv

# open file csv
data = open('example.csv', encoding='utf-8')
# csv reader
csv_data = csv.reader(data)
# reformat ke python object
data_lines = list(csv_data)

# LOOPING
for d in data_lines[:5]:
    print(d)
# print(data_lines[10])

# GRAB ONLY EMAIL
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
# print(all_emails)

# GRAB ONLY FIRST NAME AND LAST NAME
fullname = []
for n in data_lines[1:20]:
    join = n[1] + ' ' + n[2]
    fullname.append(join)
# print(fullname)

# OUTPUT CSV FILE AND CREATE CSV
file_to_output = open('to_save_file.csv', mode='w', newline='')     # open file
csv_writer = csv.writer(file_to_output, delimiter=',')  # create file into csv
csv_writer.writerow(['a', 'b', 'c'])                    # create 1 row saja dengan value
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])    # create banyak row dengan value
file_to_output.close()                                      # close file

# OPEN AND APPEND DATA TO EXISTING FILE
f = open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['7','8','9'])
f.close()
