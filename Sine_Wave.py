import numpy as np
import matplotlib.pyplot as plt

f = 1
A = 1
#sampling rate
sr = 1000
t = np.arange(0 , 5, 1/sr)
y = A * np.sin( 2 * np.pi * f * t)

# plt.figure(figsize = (14,8))
plt.plot(t,y)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title("Sine Wave")
plt.grid(True)
plt.show()










