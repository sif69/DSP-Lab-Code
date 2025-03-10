x = [2,1,4,3]
h = [1,2,3,4]
l = len(x) + len(h) - 1
y = [0] * l
hh = np.flip(h)

for i in range(len(x)):
  for j in range(len(hh)):
    y[i+j]+=(x[i] * hh[j])
print(y)
print(np.correlate(x,h,'Full'))


