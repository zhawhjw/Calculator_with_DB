# Reference


## Population Mean
Calculate the population mean.

Statistics.mean(data)

data: a list of numbers.

return: the mean of the input list.




## Median
Calculate the population mean.

Statistics.median(data)

data: a list of numbers.

return: the median of the input list.

```
>>> getMedian([0, 3, 5, 5])
4.0
```

```
>>> median([2, 3, 5])
3
```

## Mode



## Population Standard Deviation

Calculate the population standard deviation.

Statistics.stddev(data)

data: a list of numbers.

return: the standard deviation of the input list.

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.stddev(numbers)
print(result)
# 1.707825127659933
```

## Variance of population proportion


## Z-Score
Calculate the z-score.

Input: a value and a list of numbers.

Return: Z-score.
```python
value = 1.5
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.zscore(value, numbers)
print(result)
#  -1.7566201313073597
```


## Standardized score

Calculate the standardized-score.

Input: a value and a list of numbers.

Return: Standardized-score.
```python
value = 1.5
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.zscore(value, numbers)
print(result)
#  -1.7566201313073597
```

## Population Correlation Coefficient
The correlation coefficient of two variables in a data set equals to their covariance divided by the product of their individual standard deviations. It is a normalized measurement of how the two are linearly related.


Input: a value and a list of numbers.

Return: the population correlation coefficient.
```python
numbers1 = [2.3, 3.6, 4.7, 5.5, 6.47, 7.5]
numbers2 = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.pcc(numbers1, numbers2)
print(result)
#  1.1970737153967075
```

## Confidence Interval

## Population Variance

Input: a list of numbers.

Return: the standard deviation of the input list.

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.stddev(numbers)
print(result)
# 1.707825127659933
```

## P Value



## Proportion

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.proportion(numbers)
print(result)
#  [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
```


## Sample Mean

## Sample Standard Deviation

## Variance of sample proportion
