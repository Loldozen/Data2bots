#! python3
import csv
import json
import os
import sys
from datetime import datetime

def compare_dates(check_date):
    """Function to compare the products date with the given expiry date
        it returns true or false"""
        
    #expire = input('Input the expiry date with format YYYY-MM-DD: ')
    expire = '2020-01-01'
    expiry_date = datetime.strptime(expire, '%Y-%m-%d')
    product_date = datetime.strptime(check_date, '%Y-%m-%d')
    status = expiry_date > product_date and 'True' or 'False'
    return status

def add_column(fileName):
    with open(fileName, 'r' ) as inputData,open('result.csv', 'w') as outputData:
        reader = csv.reader(inputData)
        writer = csv.writer(outputData)

        result = []
        header = next(reader)
        header.append('obsolete')
        result.append(header)
        for row in reader:
            obsolete = compare_dates(row[0])
            row.append(obsolete)
            result.append(row)
            
        return writer.writerows(result), header, reader
def convert_to_json():
    data = {}
    with open('result.csv', 'r') as csvFile, open('jsonResult.json', 'w') as jsonFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            key = row['sku']
            data[key] = row
        print(json.dumps(data, indent=4))
        return jsonFile.write(json.dumps(data, indent=4))

def check_file_type(fileName):   
    extension = os.path.splitext(fileName)[-1].lower()
    if extension == '.csv':
        add_column(fileName)
        convert_to_json()
        return fileName
    else :
        print('Invalid file type, Open a csv only')
        

#fileName= input('Enter csv file name: ')
#check_file_type()
if __name__ == '__main__':
    try:
        name = sys.argv[1]
    except IndexError:
        name= input('Enter csv file name: ')
    check_file_type(name)
