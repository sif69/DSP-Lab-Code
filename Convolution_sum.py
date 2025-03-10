
# x = [2,1,4,3]
# h = [1,2,3,4] sample input

x =list(map(int,input().split())) #user input
h = list(map(int,input().split())) #user input
l = len(x) + len(h) - 1

y = [0] * l
for i in range(len(x)):
    for j in range(len(h)):
      y[i+j]+=(x[i] * h[j])
plt.stem(y)
print("Manual Convolution Sum :",y)
print("Numpy Convolution Sum :",np.convolve(x,h,'Full'))
