#!/usr/bin/env python

import csv

def read_csv():
    lines = []
    filename = "data.csv"
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            lines.append(line)
    return lines

def main():
    print("starting program...")
    csv_data = read_csv()
    print(csv_data)
    print("program finished.")
    
if __name__ == '__main__':
    main()
