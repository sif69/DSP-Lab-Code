import numpy as np
import matplotlib.pyplot as plt

x =list(map(int,input().split()))
l = len(x) + len(x) - 1
y = [0] * l
hh = np.flip(x)

for i in range(len(x)):
  for j in range(len(hh)):
    y[i+j]+=(x[i] * hh[j])
print(y)
print(np.correlate(x,x,'Full'))
