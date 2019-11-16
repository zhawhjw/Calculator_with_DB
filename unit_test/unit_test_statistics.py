from statistics.statistics import Statistics
from csv_reader.csv_reader import CSVReader
import unittest
from pprint import pprint


class unitTestForStatisticsCalculator(unittest.TestCase):
    statistics_calculator = None

    def setUp(self) -> None:
        self.statistics_calculator = Statistics()

    def testInstanceOfCalculator(self) -> None:
        self.assertIsInstance(self.statistics_calculator, Statistics)

    def testMean(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Mean.csv"
                                                                              )

        # pprint(test_data)
        # print()

        value_list = [int(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]
        result = result_list[0]

        self.assertEqual(self.statistics_calculator.mean(value_list), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testMode(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Mode.csv"
                                                                              )

        # pprint(test_data)
        # print()

        value_list = [int(row[value1_index]) for row in test_data]

        result_list = [row[result_index] for row in test_data]
        result = list(set(result_list))

        self.assertEqual(self.statistics_calculator.mode(value_list), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testConfidenceInterval(self) -> None:
        value1_index, left_index, right_index, test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                         "../csv_files/",
                                                                                         "Unit Test CI.csv"
                                                                                         )

        # pprint(test_data)
        # print()

        value1_list = [int(row[value1_index]) for row in test_data]
        left_list = [float(row[left_index]) for row in test_data]
        right_list = [float(row[right_index]) for row in test_data]

        result = [left_list[0], right_list[0]]

        self.assertEqual(self.statistics_calculator.ci(value1_list, cl=0.95), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testSampleMean(self) -> None:
        value1_index, result_index, sample_index, test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                            "../csv_files/",
                                                                                            "Unit Test Sample Mean.csv"
                                                                                            )
        # pprint(test_data)
        # print()

        value_list = [int(row[value1_index]) for row in test_data]
        sample_list = [int(row[sample_index]) for row in test_data]

        sample_value_list = []

        for i in range(len(sample_list)):
            if sample_list[i] == 1:
                sample_value_list.append(value_list[i])

        result_list = [float(row[result_index]) for row in test_data]
        result = result_list[0]

        self.assertEqual(self.statistics_calculator.mean(sample_value_list), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testMedian(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Median.csv"
                                                                              )

        value_list = [float(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]
        result = result_list[0]

        self.assertEqual(self.statistics_calculator.median(value_list), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testProportion(self) -> None:
        value1_index, result_index, value2_index, test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                            "../csv_files/",
                                                                                            "Unit Test Proportion.csv"
                                                                                            )
        value1_list = [float(row[value1_index]) for row in test_data]
        value2_list = [float(row[value2_index]) for row in test_data]
        result_list = [float(row[result_index]) for row in test_data]

        value2 = value2_list[0]
        result = result_list[0]

        self.assertEqual(self.statistics_calculator.proportion(value1_list, value2), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testPopulationStddev(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Population Std.csv"
                                                                              )
        value1_list = [float(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]

        result = result_list[0]

        # print(np.std(value1_list))
        # print()

        self.assertEqual(self.statistics_calculator.stddev(value1_list), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testSampleStddev(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Sample Std.csv"
                                                                              )
        value1_list = [float(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]

        result = result_list[0]

        # print(np.std(value1_list))
        # print()

        self.assertEqual(self.statistics_calculator.stddev(value1_list, mode="sample"), result)
        self.assertEqual(self.statistics_calculator.result, result)

    def testPopulationCorrlationCoefficeint(self) -> None:
        value1_index, value2_index, result_index, test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                            "../csv_files/",
                                                                                            "Unit Test PPC.csv"
                                                                                            )
        value1_list = [float(row[value1_index]) for row in test_data]
        value2_list = [float(row[value2_index]) for row in test_data]
        result_list = [float(row[result_index]) for row in test_data]

        result = result_list[0]
        result = round(result, 10)

        expected = self.statistics_calculator.pcc(value1_list, value2_list, mode="sample")
        expected = round(expected, 10)

        returned_result = self.statistics_calculator.result
        returned_result = round(returned_result, 10)

        self.assertEqual(expected, result)
        self.assertEqual(returned_result, result)

    def testPopulationVariance(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Population Variance.csv"
                                                                              )
        value1_list = [float(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]

        result = result_list[0]
        # result = round(result, 10)

        expected = self.statistics_calculator.variance(value1_list)
        # expected = round(expected, 10)

        returned_result = self.statistics_calculator.result
        # returned_result = round(returned_result, 10)

        self.assertEqual(expected, result)
        self.assertEqual(returned_result, result)

    def testZscore(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Z Score.csv"
                                                                              )
        value1_list = [float(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]

        # result = round(result, 10)

        expected = self.statistics_calculator.zscore(value1_list)
        # expected = round(expected, 10)

        returned_result = self.statistics_calculator.result
        # returned_result = round(returned_result, 10)

        self.assertEqual(expected, result_list)
        self.assertEqual(returned_result, result_list)

    def testStandardizedScore(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test Standardized Score.csv"
                                                                              )
        value1_list = [float(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]

        # result = round(result, 10)

        expected = self.statistics_calculator.standardizedscore(value1_list)
        # expected = round(expected, 10)

        returned_result = self.statistics_calculator.result
        # returned_result = round(returned_result, 10)

        self.assertEqual(expected, result_list)
        self.assertEqual(returned_result, result_list)

    def testVariancePopulationProportion(self) -> None:
        value1_index, value2_index, result_index, test_data = CSVReader.callCreateCSVReader("ThreeFieldsCSV",
                                                                                            "../csv_files/",
                                                                                            "Unit Test Variance of Population Proportion.csv"
                                                                                            )
        value1_list = [float(row[value1_index]) for row in test_data]
        value2_list = [float(row[value2_index]) for row in test_data]
        result_list = [float(row[result_index]) for row in test_data]

        success_count = value2_list[0]
        print(success_count)
        result = result_list[0]
        # result = round(result, 10)

        expected = self.statistics_calculator.vp(value1_list, success_count)
        # expected = round(expected, 10)

        returned_result = self.statistics_calculator.result
        # returned_result = round(returned_result, 10)

        self.assertEqual(expected, result)
        self.assertEqual(returned_result, result)

    def testVarianceSampleProportion(self) -> None:
        value1_index, value2_index, sample_index, result_index, test_data = CSVReader.callCreateCSVReader(
            "FourFieldsCSV",
            "../csv_files/",
            "Unit Test Variance of Sample Proportion.csv"
            )
        value1_list = [float(row[value1_index]) for row in test_data]
        value2_list = [float(row[value2_index]) for row in test_data]
        sample_list = [float(row[sample_index]) for row in test_data]
        result_list = [float(row[result_index]) for row in test_data]

        success_count = value2_list[0]
        # print(success_count)
        result = result_list[0]

        sample_value1_list = []
        for i in range(len(sample_list)):
            if sample_list[i] == 1:
                sample_value1_list.append(value1_list[i])

        expected = self.statistics_calculator.vp(sample_value1_list, success_count)
        # expected = round(expected, 10)

        returned_result = self.statistics_calculator.result
        # returned_result = round(returned_result, 10)

        self.assertEqual(expected, result)
        self.assertEqual(returned_result, result)

    def testPValue(self) -> None:
        value1_index, result_index, test_data = CSVReader.callCreateCSVReader("TwoFieldsCSV",
                                                                              "../csv_files/",
                                                                              "Unit Test P Value.csv"
                                                                              )
        value1_list = [float(row[value1_index]) for row in test_data]

        result_list = [float(row[result_index]) for row in test_data]

        print("THIS TAKES A LONG TIME TO RUN!")
        expected = self.statistics_calculator.pvalue(value1_list)
        # expected = round(expected, 10)

        returned_result = self.statistics_calculator.result
        # returned_result = round(returned_result, 10)

        self.assertEqual(expected, result_list)
        self.assertEqual(returned_result, result_list)


if __name__ == '__main__':
    unittest.main()
