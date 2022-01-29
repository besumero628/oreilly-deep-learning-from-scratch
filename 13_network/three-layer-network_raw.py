import sys
sys.path.append('../12_function')

import numpy as np
import function as fn

# element
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],
              [0.2, 0.4, 0.6]])
W2 = np.array([[0.1, 0.4],
               [0.2, 0.5],
               [0.3, 0.6]])
W3 = np.array([[0.1, 0.3],
               [0.2, 0.4]])
B1 = np.array([0.1, 0.2, 0.3])
B2 = np.array([0.1, 0.2])
B3 = np.array([0.1, 0.2])

# 1st layer
A1 = np.dot(X, W1) + B1
Z1 = fn.sigmoid(A1)

# 2nd layer
A2 = np.dot(Z1, W2) + B2
Z2 = fn.sigmoid(A2)

# final layer
A3 = np.dot(Z2, W3) + B3
Y = fn.identity_function(A3)

print("-----1st layer----")
print(X.shape)
print(W1.shape)
print(B1.shape)

print("-----1st result----")
print(A1)
print(Z1)

print("-----2nd layer----")
print(Z1.shape)
print(W2.shape)
print(B2.shape)

print("-----2nd result----")
print(A2)
print(Z2)

print("-----final layer----")
print(Z2.shape)
print(W3.shape)
print(B3.shape)

print("-----final result----")
print(A3)
print(Y)