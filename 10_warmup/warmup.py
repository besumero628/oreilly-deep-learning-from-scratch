import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# numpy
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))
print(x.shape)
print(x.dtype)

# matplotlib
xx = np.arange(0, 6, 0.1)
yy1 = np.sin(xx)
yy2 = np.cos(xx)

plt.plot(xx, yy1, label="sin")
plt.plot(xx, yy2, linestyle = "--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()

# image
img = imread('../90_dataset/lena.png')
plt.imshow(img)

plt.show()