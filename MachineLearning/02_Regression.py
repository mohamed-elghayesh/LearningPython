# simple regression line y= mx + b, (m, b) are required 
from statistics import mean
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
import random

style.use('fivethirtyeight')

# xs = np.array([1,2,3,4,5,6],dtype=np.float64)
# ys = np.array([5,4,6,5,6,7],dtype=np.float64)

# instead of hardcoded xs and ys use random data, hm: how much, vary variance and check accuracy
def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

# getting the slope m
def best_fit_slope_intercept(xs,ys):
    m = ( mean(xs) * mean(ys) - mean(xs * ys)) / ((mean(xs)**2) - (mean(xs**2)))
    b = mean(ys) - m * mean(xs)
    return m, b

def squared_error(ys_orig, ys_fit):
    return sum((ys_fit - ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_fit):
    y_mean_fit = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_fit)
    squared_error_y_mean = squared_error(ys_orig, y_mean_fit)
    return 1 - (squared_error_regr/squared_error_y_mean)

# plt.scatter(xs,ys) # plt.plot() -> draws a line
# plt.show()

# Main
xs, ys = create_dataset(40, 10, 2, correlation='False')
m, b = best_fit_slope_intercept(xs,ys)
print(m, b)

regression_line = [(m*x)+b for x in xs]

predict_x = 8
predict_y = (m * predict_x + b)

# R square (error) accuracy of fitting
r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, s=100, color='g')
plt.plot(xs, regression_line)
plt.show()
