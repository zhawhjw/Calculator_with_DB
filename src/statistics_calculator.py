import calculator

def getMean(data):
    
    summation = sum(data)
    mean = summation / len(data)

    return mean

def getMedian(data):
    
    sorted_data = sorted(data)
    print(sorted_data)

    if (len(data) % 2 ==0):
        median = (sorted_data[len(data)//2 - 1] + sorted_data[len(data)//2])/2
    else:
        median = sorted_data[len(data)//2]

    return median

class StatisticsCalculator(calculator.Calculator):
    result = None
    
    def __init__(self):
        result = 0
    
    def mean(self,data):
        self.result = getMean(data)
        return self.result

    def median(self,data):
        self.result = getMedian(data)
        return self.result
