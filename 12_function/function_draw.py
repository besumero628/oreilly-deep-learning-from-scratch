from cProfile import label
import imp

import matplotlib.pyplot as plt
import function as fn

x = fn.np.arange(-5.0, 5.0, 0.1)
y_step = fn.step_function(x)
y_sigmoid = fn.sigmoid(x)
y_relu = fn.relu(x)
plt.plot(x,y_step, label="step")
plt.plot(x,y_sigmoid, label="sigmoid")
plt.plot(x,y_relu, label="ReLU")
plt.ylim(-0.1, 1.1)
plt.legend()
plt.show()
