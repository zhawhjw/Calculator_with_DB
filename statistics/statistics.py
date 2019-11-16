from calculator.calculator import Calculator
import math
import collections


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

def frequencyTable(data):
    """
    This piece is based on Python mode function
    :param data: data list
    :return: frequency table
    """
    # Generate a table of sorted (value, frequency) pairs.
    table = collections.Counter(iter(data)).most_common()
    if not table:
        return table
    # Extract the values with the highest frequency.
    maxfreq = table[0][1]
    for i in range(1, len(table)):
        if table[i][1] != maxfreq:
            table = table[:i]
            break
    return table


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

    def pdf(self, value: float, mean=0, stddev=1):
        e = math.e
        pi = math.pi

        subtract = self.subtract
        divide = self.divide
        multiply = self.multiply
        sqr = self.sqr
        sqrt = self.sqrt

        base = multiply(2, pi)
        base = sqrt(base)
        base = multiply(base, stddev)
        base = divide(base, 1)

        p = subtract(mean, value)
        p = divide(stddev, p)
        p = sqr(p)
        p = multiply(0.5, p)
        p = -p
        p = pow(e, p)

        data_pdf = multiply(base, p)
        self.result = data_pdf
        return self.result

    def mean(self, data: list):
        """
        Task 1 and 13

        get the mean value of the data

        :param data: data list
        :return: mean value
        """

        """define function built in class 'Calculator' """
        divide = self.divide
        '''define required variables '''
        data_size = len(data)

        summation = sum(data)
        data_mean = divide(data_size, summation)

        self.result = data_mean
        return self.result

    def median(self, data: list):
        """
        Task 2

        get the median value of sorted data list;
        calculation method is depend on Parity of length of the data list

        :param data: data list
        :return: median value
        """

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
        """
        Task 3
        get the most frequent numbers in data list;
        will return error when all numbers have same frequency
        Based on Python mode library
        :param data: data list
        :return: error or  mode value
        """
        n = len(data)

        data_cnt = collections.Counter(data)
        print(data_cnt)
        get_mode = dict(data_cnt)
        mode = [k for k, v in get_mode.items() if v == max(list(data_cnt.values()))]

        if len(mode) == n:
            get_mode = None
        else:
            get_mode = list(map(str, mode))

        self.result = get_mode
        return self.result

    def stddev(self, data: list, mode="population"):
        """
        Task 4 and 14

        Calculate stand deviation for population data or sample data

        :param data: data list
        :param mode: "population" or "sample"
        :return: stand deviation
        """

        """returns the standard deviation of data"""
        variance = self.variance
        sqrt = self.sqrt

        data_variance = variance(data, mode)
        data_stddev = sqrt(data_variance)

        self.result = data_stddev
        return self.result

    def vp(self, data: list, success_data_count: int):
        """
        Task 5 and 15

        ^p = X / n
        q = sqrt( ^p * (1 - ^p) / n)

        :param data: data list has size n
        :param success_data_count: given count of data which matches the characteristics we want X
        :return: variance of population/sample proportion q
        """
        subtract = self.subtract
        multiply = self.multiply
        divide = self.divide
        sqrt = self.sqrt

        proportion = self.proportion

        data_size = len(data)

        data_proportion = proportion(data, success_data_count)

        complementary_proportion = subtract(data_proportion, 1)
        nominator = multiply(data_proportion, complementary_proportion)
        denominator = data_size
        ratio = divide(denominator, nominator)
        vp = sqrt(ratio)

        self.result = vp
        return self.result

    def zscore(self, data: list):
        """
        Task 6
        get z-score of data list

        :param value:
        :param data:
        :return:
        """

        divide = self.divide
        subtract = self.subtract
        mean = self.mean
        stddev = self.stddev

        z = []
        data_mean = mean(data)
        data_stddev = stddev(data)

        for value in data:
            data_mdev = subtract(data_mean, value)

            data_zscore = divide(data_stddev, data_mdev)

            z.append(data_zscore)

        self.result = z
        return self.result

    def standardizedscore(self, data: list):
        """
        Task 7
        same meaning with z-score

        :param value:
        :param data:
        :return:
        """

        zscore = self.zscore
        self.result = zscore(data)
        return self.result

    def pcc(self, data1: list, data2: list, mode="population"):
        """
        Task 8
        get population correlation coefficient

        :param data1:
        :param data2:
        :return:
        """

        divide = self.divide
        multiply = self.multiply

        covariance = self.covariance
        stddev = self.stddev

        data_covariance = covariance(data1, data2)
        data1_stddev = stddev(data1, mode)
        data2_stddev = stddev(data2, mode)

        product_data_stddev = multiply(data1_stddev, data2_stddev)

        data_pcc = divide(product_data_stddev, data_covariance)
        self.result = data_pcc
        return self.result

    def ci(self, data: list, cl=0.95):
        """
        Task 9

        Confidence interval - given a data list of values compute the stand deviation,
        divided by the number of entries,
        multiplied by a constant factor of (cc).
        The constant factor can be looked up from a table, for 95% confidence
        on a reasonable size sample (>=500) 1.96 is used.
        """
        add = self.add
        subtract = self.subtract
        divide = self.divide
        multiply = self.multiply
        sqrt = self.sqrt

        mean = self.mean
        stddev = self.stddev

        data_mean = mean(data)
        data_size = len(data)
        data_stddev = stddev(data)

        if cl == 0.95:
            cc = 1.96
        elif cl == 0.90:
            cc = 1.64
        elif cl == 0.99:
            cc = 2.58
        else:
            cc = 1.96
            print('Only 0.90, 0.95 or 0.99 % are allowed for, using default 0.95')

        data_size_sqrt = sqrt(data_size)
        h = divide(data_size_sqrt, data_stddev)
        h = multiply(h, cc)

        left = subtract(h, data_mean)
        right = add(h, data_mean)

        self.result = [left, right]
        return self.result

    def variance(self, data: list, mode="population"):
        """
        Task 10
        get variance of population data or sample data

        :param data:
        :param mode:
        :return:
        """

        add = self.add
        subtract = self.subtract
        divide = self.divide
        multiply = self.multiply
        mean = self.mean

        data_size = len(data)
        # print(data_size)
        diff_sqr_summation = 0
        mn = mean(data)
        # print(mn)
        for e in data:
            diff = subtract(mn, e)
            diff_sqr = multiply(diff, diff)
            diff_sqr_summation = add(diff_sqr_summation, diff_sqr)
        # print(diff_sqr_summation)

        # data_variance = 0
        if mode == "sample":
            df = subtract(1, data_size)
            data_variance = divide(df, diff_sqr_summation)
        else:
            data_variance = divide(data_size, diff_sqr_summation)

        # print(data_variance)
        self.result = data_variance
        return self.result

    def pvalue(self, data: list, mode="one"):
        """
        Task 11
        get p-value from z-score
        :param mode: "one" or "two"
        :param value: value in data list that be computed to get p-value
        :param data: data list
        :return: p-value on one-tail or two-tail
        """
        subtract = self.subtract
        multiply = self.multiply

        cdf = self.cdf
        mean = self.mean
        stddev = self.stddev

        m = mean(data)
        std = stddev(data)

        data_cdf = cdf(data, mean=m, stddev=std)

        data_pvalue = [subtract(c, 1) for c in data_cdf]

        if mode == "two":
            data_pvalue = [multiply(2, p) for p in data_pvalue]

        self.result = data_pvalue
        return self.result

    def proportion(self, data: list, success_data_count: int):
        """
        Task 12

        ^p = X / n

        Where X is the given count of data which matches the characteristics we want
              n is the sample size where draws the X

              ^p is the proportion

        :param data: sample size n
        :param success_data_count: given count of data which matches the characteristics we want X
        :return: proportion ^p
        """

        divide = self.divide

        data_size = len(data)

        data_proportion = divide(data_size, success_data_count)
        self.result = data_proportion
        return self.result

    def cdf(self, data: list, mean=0, stddev=1):


        add = self.add
        subtract = self.subtract
        divide = self.divide
        multiply = self.multiply
        pdf = self.pdf

        rang = multiply(300, stddev)
        interval = 1000000

        min_x = subtract(rang, mean)
        min_x = divide(2, min_x)
        # max_x = mean + rang / 2

        c = []

        for x in data:

            if x == mean:
                c.append(0.5)
                continue

            dx = divide(interval, rang)

            # idx = int((x - min_x) / dx)
            idx = subtract(min_x, x)
            idx = divide(dx, idx)
            idx = int(idx)

            r = []
            for i in range(idx):
                # dx * i + min_x + dx / 2
                x1 = multiply(dx, i)
                x2 = divide(2, dx)
                x3 = add(x1, x2)
                x = add(x3, min_x)

                x_pdf = pdf(x, mean=mean, stddev=stddev)

                x_pdf_product = multiply(dx, x_pdf)

                r.append(x_pdf_product)

            result = round(sum(r), 2)

            c.append(result)

        return c


if __name__ == '__main__':
    s = Statistics()
    data = [782, 527, 140, 13, 670, 458, 549, 862, 154, 906, 162, 203, 309, 982]

    m = s.mean(data)
    sdt = s.stddev(data)
    # print(s.zscore(982, data))
    # print(s.pvalue(982, data))

    print(s.pvalue(data, mean=m, stddev=sdt, mode="one"))
