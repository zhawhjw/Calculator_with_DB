# API Reference


## 1. Population Mean
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


## 2. Median
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
## 3. Mode
Get the most frequent numbers in data list; will return error when all numbers.

```python
numbers = [2, 3, 3, 3, 3, 4, 5, 5]
statistics = Statistics()
result = statistics.mode(numbers)
print(result)
# 3
```

## 4. Population Standard Deviation

Calculate the population standard deviation.

Population standard deviation = σ = sqrt [ Σ ( Xi - μ )2 / N ]

Statistics.stddev(data,  mode="population")

data: a list of numbers.

return: the standard deviation of the input list.

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.stddev(numbers,  mode="population")
print(result)
# 1.8708286933869707
```

## 5. Variance of population proportion

Calculate the sample standard deviation.

Variance of sample proportion = sp*sp = pq / (n - 1)

^p = X / n

q = sqrt( ^p * (1 - ^p) / n)

:param data: data list has size n

:param success_data_count: given count of data which matches the characteristics we want X

:return: variance of population/sample proportion q

Statistics.vp(data: list, success_data_count: int)

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.vp(numbers, 3)
print(result)
# 0.2041241452319315
```

## 6. Z-Score
Calculate the z-score.

Input: a value and a list of numbers.

Return: Z-score.
```python
import numpy as np
from numpy.linalg import cholesky

sampleNum = 10
mu = 10
sigma = 2
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNum)

value = s[0]
statistics = Statistics()
zscore = statistics.zscore(value, s) 
print(value, " have a z-score of ", zscore, "in the list of: " , s)
#  13.528104691935328  have a z-score of  1.0065119079295075 in the list of:  [13.52810469 10.80031442 11.95747597 14.4817864  13.73511598  8.04544424
 11.90017684  9.69728558  9.7935623  10.821197  ]
```


## 7. Standardized score

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

## 8. Population Correlation Coefficient
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

## 9. Confidence Interval
Statisticians use a confidence interval to describe the amount of uncertainty associated with a sample estimate of a population parameter.

Confidence interval: given a data list of values compute the stand deviation, divided by the number of entries,
        multiplied by a constant factor of (cc). The constant factor can be looked up from a table, for 95% confidence on a reasonable size sample (>=500) 1.96 is used.
        
```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.ci(numbers, cl = 0.95)
print(result)
# [3.003025272981092, 5.996974727018908]

```        

## 10. Population Variance

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

## 11. P Value

Get p-value from z-score

Statistics.pvalue(self, value, data: list, mode = "one")

:param mode: "one" or "two"

:param value: value in data list that be computed to get p-value

:param data: data list

:return: p-value on one-tail or two-tail

```python
import numpy as np
from numpy.linalg import cholesky

sampleNum = 10
mu = 10
sigma = 2
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNum)

value = s[0]
statistics = Statistics()
pvalue = statistics.pvalue(value, s, mode = "one") 
print(value, " have a p-value of ", pvalue, "in the list of: " , s)
# 13.528104691935328  have a p-value of  -4119.094006713272 in the list of:  [13.52810469 10.80031442 11.95747597 14.4817864  13.73511598  8.04544424
 11.90017684  9.69728558  9.7935623  10.821197  ]
```



## 12. Proportion

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.proportion(numbers)
print(result)
#  [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
```


## 13. Sample Mean

Calculate the sample mean.

Sample mean = ( Σ xi ) / n

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
 
## 14. Sample Standard Deviation

Calculate the sample standard deviation.

Sample standard deviation = s = sqrt [ Σ ( xi - x )2 / ( n - 1 ) ]

Statistics.stddev(data,  mode="sample")

data: a list of numbers.

return: the standard deviation of the input list.


```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.stddev(numbers,  mode="sample")
print(result)
# 1.707825127659933
```

## 15. Variance of sample proportion

Calculate the sample standard deviation.

Variance of sample proportion = sp*sp = pq / (n - 1)

^p = X / n

q = sqrt( ^p * (1 - ^p) / n)

:param data: data list has size n

:param success_data_count: given count of data which matches the characteristics we want X

:return: variance of population/sample proportion q

Statistics.vp(data: list, success_data_count: int)

```python
numbers = [2, 3, 4, 5, 6, 7]
statistics = Statistics()
result = statistics.vp(numbers, 3)
print(result)
# 0.2041241452319315
```


# Reference:
Refer the formulae here:
[Stat Trek tutorials](https://stattrek.com/statistics/formulas.aspx)