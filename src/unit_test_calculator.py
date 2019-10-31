from calculator import Calculator
from csv_reader import CSVReader
import unittest
from pprint import pprint



class unitTestForCalculator(unittest.TestCase):

    calculator = None

    def setUp(self) -> None:
        self.calculator = Calculator()
	
    def testInstanceOfCalculator(self) -> None:
        self.assertIsInstance(self.calculator, Calculator)

    def testAddition(self) -> None:
 
        value1_index,value2_index,result_index,test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                       "../csv_files/",
                                                                                       "Unit Test Addition.csv"
        )

        #pprint(test_data)
        #print()
        for row in test_data:
            
            value1 = int(row[value1_index])
            value2 = int(row[value2_index])
            result = int(row[result_index])
            
            self.assertEqual(self.calculator.add(value1, value2), result)
            self.assertEqual(self.calculator.result, result)

    def testSubtratcion(self) -> None:

        value1_index,value2_index,result_index,test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                       "../csv_files/",
                                                                                       "Unit Test Subtraction.csv"
        )

        #pprint(test_data)
        #print()
        for row in test_data:
            
            value1 = int(row[value1_index])
            value2 = int(row[value2_index])
            result = int(row[result_index])
            
            self.assertEqual(self.calculator.subtract(value1, value2), result)
            self.assertEqual(self.calculator.result, result)


    def testMultiplication(self) -> None:

        value1_index,value2_index,result_index,test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                       "../csv_files/",
                                                                                       "Unit Test Multiplication.csv"
        )
        #pprint(test_data)
        #print()
        for row in test_data:
            
            value1 = int(row[value1_index])
            value2 = int(row[value2_index])
            result = int(row[result_index])
            
            self.assertEqual(self.calculator.multiply(value1, value2), result)
            self.assertEqual(self.calculator.result, result)


    def testDivision(self) -> None:

        value1_index,value2_index,result_index,test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                       "../csv_files/",
                                                                                       "Unit Test Division.csv"
        )
        #pprint(test_data)
        #print()
        for row in test_data:
            
            value1 = int(row[value1_index])
            value2 = int(row[value2_index])
            result = float(row[result_index])
            
            self.assertEqual(self.calculator.divide(value1, value2), result)
            self.assertEqual(self.calculator.result, result)


    def testSquare(self) -> None:

        value1_index,result_index,test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                            "../csv_files/",
                                                                            "Unit Test Square.csv"
        )
        #pprint(test_data)
        #print()
        for row in test_data:
            
            value1 = int(row[value1_index])
            result = int(row[result_index])
            
            self.assertEqual(self.calculator.sqr(value1), result)
            self.assertEqual(self.calculator.result, result)


    def testSquareRoot(self) -> None:

        value1_index,result_index,test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                            "../csv_files/",
                                                                            "Unit Test Square Root.csv"
        )
        #pprint(test_data)
        #print()
        for row in test_data:
            
            value1 = int(row[value1_index])
            result = float(row[result_index])
            
            self.assertEqual(self.calculator.sqrt(value1), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()

