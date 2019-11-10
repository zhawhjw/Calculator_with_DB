from calculator.calculator import Calculator
import math




# def getMean(data):
#    
#    summation = sum(data)
#    mean = summation / len(data)
#
#    return mean
#
# def getMedian(data):
#    
#    sorted_data = sorted(data)
#    print(sorted_data)
#
#    if (len(data) % 2 ==0):
#        median = (sorted_data[len(data)//2 - 1] + sorted_data[len(data)//2])/2
#    else:
#        median = sorted_data[len(data)//2]
#
#    return median
def frequencyCount(data):
    # Counts the number of each type of example in a dataset.
    counts = {}  # a dictionary of label -> count.
    for d in data:
        # Assume the label is the one value of current column
        label = d
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def reverseSortDictByValue(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
    frequent_tuple = sorted_dictionary[0]

    value = frequent_tuple[0]
    frequency = frequent_tuple[1]
    if frequency > 1:
        return value
    elif frequency == 1:

    return sorted_dictionary


class Statistics(Calculator):
    result = None

    def __init__(self):
        super().__init__()
        result = 0

    def covariance(self, data1: list, data2: list):
        add = self.add
        divide = self.divide
        subtract = self.subtract
        multiply = self.multiply
        mean = self.mean
        stddev = self.stddev

        data1_size = len(data1)
        data2_size = len(data2)

        if data1_size != data2_size:
            self.result = None
            return self.result
        else:

            nominator = 1
            denominator = subtract(1, data1_size)

            co = divide(denominator, nominator)
            data1_mean = mean(data1)
            data2_mean = mean(data2)

            variable = 0
            for i in range(data1_size):
                diff1 = subtract(data1_mean, data1[i])
                diff2 = subtract(data2_mean, data2[i])
                product = multiply(diff1, diff2)
                variable = add(variable, product)

            data_covariance = multiply(co, variable)

            self.result = data_covariance
            return self.result

    def sem(self, data: list):
        stddev = self.stddev
        sqrt = self.sqrt
        divide = self.divide

        data_size = len(data)
        data_stddev = stddev(data)

        data_size_sqrt = sqrt(data_size)

        data_sem = divide(data_size_sqrt, data_stddev)
        self.result = data_sem
        return self.result

    def mean(self, data: list):
        #Task 1

        """define function built in class 'Calculator' """
        divide = self.divide
        '''define required variables '''
        data_size = len(data)

        summation = sum(data)
        data_mean = divide(data_size, summation)

        self.result = data_mean
        return self.result

    def median(self, data: list):
        #Task 2

        divide = self.divide
        subtract = self.subtract
        add = self.add

        data_size = len(data)
        sorted_data = sorted(data)

        if data_size % 2 == 0:
            '''left_median = len(data)/2 - 1'''
            '''right_median = len(data)/2   '''
            minuend = divide(2, data_size)
            minuend = int(minuend)

            index_low = subtract(1, minuend)
            index_high = add(index_low, 1)

            left_median = sorted_data[index_low]
            right_median = sorted_data[index_high]

            sum_left_right_median = add(left_median, right_median)

            data_median = divide(2, sum_left_right_median)

        else:
            '''right_median = len(data)/2'''
            index = divide(2, data_size)
            index = int(index)

            data_median = sorted_data[index]

        self.result = data_median

        return self.result

    def mode(self, data: list):
        #Task 3 (NOT FINISH)
        add = self.add

        count_set = {}

        mode = max(set(data), key=data.count)

    def stddev(self, data: list):
        #Task 4
        """returns the standard deviation of data"""
        variance = self.variance
        sqrt = self.sqrt

        data_variance = variance(data)
        data_stddev= sqrt(data_variance)

        self.result = data_stddev
        return self.result

    def zscore(self, value, data: list):
        #Task 6
        divide = self.divide
        subtract = self.subtract
        mean = self.mean
        stddev = self.stddev

        data_mean = mean(data)
        data_stddev = stddev(data)
        data_mdev = subtract(data_mean,value)

        data_zscore = divide(data_stddev, data_mdev)

        self.result = data_zscore
        return self.result

    def standardizedscore(self, value, data:list ):
        #Task 7
        zscore = self.zscore
        self.result = zscore(value,data)
        return self.result

    def pcc(self, data1:list, data2:list):
        #Task 8
        divide = self.divide
        multiply = self.multiply

        covariance = self.covariance
        stddev = self.stddev

        data_covariance = covariance(data1,data2)
        data1_stddev = stddev(data1)
        data2_stddev = stddev(data2)

        product_data_stddev = multiply(data1_stddev, data2_stddev)

        data_ppc = divide(product_data_stddev, data_covariance)
        self.result = data_ppc
        return self.result


    def variance(self, data: list):
        #Task 10
        add = self.add
        subtract = self.subtract
        divide = self.divide
        sqr = self.sqr
        mean = self.mean

        data_size = len(data)

        diff_sqr_summation = 0
        mn = mean(data)
        for e in data:
            diff = subtract(mn, e)
            diff_sqr = sqr(diff)
            diff_sqr_summation = add(diff_sqr_summation, diff_sqr)

        data_variance = divide(data_size, diff_sqr_summation)

        self.result = data_variance
        return self.result




    def proportion(self, data: list):
        #Task 12
        subtract = self.subtract
        divide = self.divide

        sorted_data = sorted(data)

        p = []

        data_min = sorted_data[0]
        data_max = sorted_data[-1]

        total_diff = subtract(data_min, data_max)

        for d in data:
            proportion_diff = subtract(min, d)
            data_proportion = divide(total_diff, proportion_diff)
            p.append(data_proportion)

        self.result = p
        return self.result



    #def cdi(self,data:list, cdl = 0.95 ):

