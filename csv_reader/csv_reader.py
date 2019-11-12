'''
implement factory pattern
'''
import csv


class CSVReader(object):
    '''client side CSVReader caller'''

    def callCreateCSVReader(type, filepath, filename):
        reader = createCSVReader(type)
        return reader(filepath, filename)


def createCSVReader(type):
    '''server side CSVReader caller'''
    if type == "OneFieldsCSV":
        return getOneValuesCSVData
    elif type == "TwoFieldsCSV":
        return getTwoValuesCSVData
    elif type == "ThreeFieldsCSV":
        return getThreeValuesCSVData
    elif type == "FourFieldsCSV":
        return getFourValuesCSVData
    else:
        return ValueError(type)


def getFieldNames(csv_reader) -> dict:
    '''set field names'''
    return csv_reader.fieldnames


def readCSVData(filepath, filename) -> list:
    '''
    read csv data and save them to list
    every row is the dictionary object
    '''

    '''list to contain each row dictionary'''
    csv_data = []

    with open(filepath + filename, mode='r') as csv_file:
        '''read csv data via csv DictReader'''
        csv_reader = csv.DictReader(csv_file)
        '''get csv data field names'''
        fieldNames = getFieldNames(csv_reader)

        for row in csv_reader:
            csv_data.append(row)

    csv_file.close()

    return (fieldNames, csv_data)


def getOneValuesCSVData(filepath, filename):
    fieldNames, csvData = readCSVData(filepath, filename)

    value1 = fieldNames[0]

    return (value1, csvData)


def getTwoValuesCSVData(filepath, filename):
    fieldNames, csvData = readCSVData(filepath, filename)

    value1 = fieldNames[0]
    result = fieldNames[1]

    return (value1, result, csvData)


def getThreeValuesCSVData(filepath, filename):
    fieldNames, csvData = readCSVData(filepath, filename)

    value1 = fieldNames[0]
    value2 = fieldNames[1]
    result = fieldNames[2]

    return (value1, value2, result, csvData)

def getFourValuesCSVData(filepath, filename):
    fieldNames, csvData = readCSVData(filepath, filename)

    value1 = fieldNames[0]
    value2 = fieldNames[1]
    value3 = fieldNames[2]
    result = fieldNames[3]

    return (value1, value2, value3, result, csvData)


if __name__ == '__main__':
    csv_reader = CSVReader()
    value1, value2, result, csvData = csv_reader.callCreateCSVReader("ThreeFieldsCSV", "./csv_files/",
                                                                     "Unit Test Multiplication.csv")

    print(value1)
    print()
    print(value2)
    print()
    print(result)
    print()
    print(csvData)
    print()
