# Reference


## Population Mean
Calculate the population mean.

Population mean = μ = ( Σ Xi ) / N

Statistics.mean(data)

data: a list of numbers.

return: the mean of the input list.

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.mean(numbers)
print(result)
# 4.5
```


## Median
Calculate the population mean.

Statistics.median(data)

data: a list of numbers.

return: the median of the input list.

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.median(numbers)
print(result)
# 4.5
```

```python
numbers = [2, 3, 4, 5, 6, 7, 8]
statistics = Statistics()
result = statistics.median(numbers)
print(result)
# 5
```
## Mode



## Population Standard Deviation

Calculate the population standard deviation.

Population standard deviation = σ = sqrt [ Σ ( Xi - μ )2 / N ]

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

Standardized score = Z = (X - μ) / σ

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

Population correlation coefficient = ρ = [ 1 / N ] * Σ { [ (Xi - μX) / σx ] * [ (Yi - μY) / σy ] }

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

Population variance = σ2 = Σ ( Xi - μ )2 / N

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

Sample mean = x = ( Σ xi ) / n


## Sample Standard Deviation

Sample standard deviation = s = sqrt [ Σ ( xi - x )2 / ( n - 1 ) ]


## Variance of sample proportion




Reference:
Refer the formulae here:
[Stat Trek tutorials](https://stattrek.com/statistics/formulas.aspx)