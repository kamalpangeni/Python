import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('Importing data............')
df = pd.read_csv('train.csv')       # importing data
print('Data successfully imported')

df = df[0:20000]
print('size of input data:' + str(len(df)))

x0 = np.ones(len(df))
df.insert(1, 'x0', x0)              # insert a column of ones in first row

# First, we convert the digit into a 10 dimensional
# array with 1 in location corresponding to the integer
# and zero else. e.g 2=(0,0,1,...,0)

yraw = np.asarray(df)[:, 0].astype(int)  # convert float to int so can be used in indexing
ym = np.zeros((len(df), 10))
for i in range(len(df)):
    ym[i][yraw[i]] = 1

# given an array, it returns the index of first element where the element > 0.5
def position(array):
    for i in range(len(array)):
        if int(array[i]) > 0.5:
            return i
            break
    else:
        return 0

# returns number of true positives
def truepos(array1, array2):
    tp = 0
    for i in range(len(array1)):
        if array1[i] == array2[i]:
            tp = tp+1
    return tp

l0 = pd.DataFrame.as_matrix(df[df.columns[1:len(df.columns)]])
ypredict = np.zeros(len(df))

num_examples = len(df)              # number of data points
num_in = l0.shape[1]                # number of columns of input matrix
num_mid = 18                        # number of inter nodes
num_out = 10                        # number of outer nodes
num_iter = 6000                     # number of iteration for training data

# weight functions
theta0 = 2*np.random.random((num_in, num_mid))-1
theta1 = 2*np.random.random((num_mid, num_out))-1

# training the neural network
for j in range(num_iter):
    l1 = 1/2*(np.tanh(np.dot(l0, theta0))+1)
    l2 = 1/2*(np.tanh(np.dot(l1, theta1))+1)

    l2_error = ym-l2

    if (j % 1000) == 0:
        for i in range(len(l2)):
            ypredict[i] = position(l2[i])
        print('% of true pos:'+str(truepos(ypredict, yraw) / len(df)))

    l2_delta = np.multiply(l2_error, 1/(2*np.cosh(l2)*np.cosh(l2)))

    l1_error = l2_delta.dot(theta1.T)

    l1_delta = np.multiply(l1_error, 1/(2*np.cosh(l1)*np.cosh(l1)))

    theta1 += l1.T.dot(l2_delta)
    theta0 += l0.T.dot(l1_delta)

for i in range(len(l2)):
        ypredict[i] = position(l2[i])

print(truepos(ypredict, yraw)/len(df))