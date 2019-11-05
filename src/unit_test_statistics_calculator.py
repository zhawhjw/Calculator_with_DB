from statistics_calculator import StatisticsCalculator
from csv_reader import CSVReader
import unittest
from pprint import pprint

class unitTestForStatisticsCalculator(unittest.TestCase):

    statistics_calculator = None

    def setUp(self) -> None:
        self.statistics_calculator = StatisticsCalculator()
	
    def testInstanceOfCalculator(self) -> None:
        self.assertIsInstance(self.statistics_calculator, StatisticsCalculator)

    def testMean(self) -> None:
 
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                	      "../csv_files/",
                                                                              "Unit Test Mean.csv"
        )

        #pprint(test_data)
        #print()

        value_list = [int(row[value1_index]) for row in test_data]
        
        result_list = [float(row[result_index]) for row in test_data]
        result = result_list[0]
        
       
            
        self.assertEqual(self.statistics_calculator.mean(value_list), result)
        self.assertEqual(self.statistics_calculator.result, result)


    def testMedian(self) -> None:
 
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                	      "../csv_files/",
                                                                              "Unit Test Median.csv"
        )

        #pprint(test_data)
        #print()

        value_list = [float(row[value1_index]) for row in test_data]
        
        result_list = [float(row[result_index]) for row in test_data]
        result = result_list[0]
        
       
            
        self.assertEqual(self.statistics_calculator.median(value_list), result)
        self.assertEqual(self.statistics_calculator.result, result)

if __name__ == '__main__':
    unittest.main()

