#Linear regression without moduless
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2,-1,0,1,2], dtype=float)
y = np.array([65,95,80,115,105], dtype=float)

n = len(x)
mean_x = np.mean(x)
mean_y = np.mean(y)

num = np.sum((x-mean_x)*(y-mean_y))
den = np.sum((x-mean_x)**2)
m = num/den
c = mean_y - m*mean_x

y_pred = m*x + c

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("Slope m =", m)
print("Intercept c =", c)
print("Predicted values =", y_pred)

