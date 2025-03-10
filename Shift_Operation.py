import numpy as np
import matplotlib.pyplot as plt

# Given discrete-time signal x[n] and time samples t[n]
x = np.array([1, 3, 1, 2, 3, 4, 1, 1])
t = np.array([-3, -2, -1, 0, 1, 2, 3, 4])

# Shift operations
identity_x = x  # Identity system: no shift

unit_delay_x = [] # y[n] = x[n-1]
for i in range(1, len(x)):
  unit_delay_x.append(x[i-1])


unit_advance_x = [] # y[n] = x[n+1]
for i in range(0,len(x)-1):
  unit_advance_x.append(x[i+1])

# Moving Average system: (x[n-1] + x[n] + x[n+1]) / 3
moving_average_x = []
for i in range(len(x)):
    prev_x = x[i-1] if i > 0 else 0
    next_x = x[i+1] if i < len(x)-1 else 0
    moving_average_x.append((prev_x + x[i] + next_x) / 3)

# Moving Median system: median([x[n-1], x[n], x[n+1]])
moving_median_x = []
for i in range(len(x)):
    prev_x = x[i-1] if i > 0 else 0
    next_x = x[i+1] if i < len(x)-1 else 0
    moving_median_x.append(np.median([prev_x, x[i], next_x]))

# Accumulator system: (cumulative sum)
accumulator_x = []
cumulative_sum = 0
for value in x:
    cumulative_sum += value
    accumulator_x.append(cumulative_sum)

# Plotting the systems and their responses
plt.figure(figsize=(10, 6))

# Plotting the Identity system
plt.subplot(3, 2, 1)
plt.stem(t, identity_x, basefmt=" ")
plt.title('Identity System')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotting the Unit Delay system
plt.subplot(3, 2, 3)
plt.stem(t[1:], unit_delay_x, basefmt=" ")
plt.title('Unit Delay System (x[n-1])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotting the Unit Advance system
plt.subplot(3, 2, 5)
plt.stem(t[:-1], unit_advance_x, basefmt=" ")
plt.title('Unit Advance System (x[n+1])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotting the Moving Average system
plt.subplot(3, 2, 2)
plt.stem(t, moving_average_x, basefmt=" ")
plt.title('Moving Average System ([x[n-1] + x[n] + x[n+1]] / 3)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotting the Moving Median system
plt.subplot(3, 2, 4)
plt.stem(t, moving_median_x, basefmt=" ")
plt.title('Moving Median System (median[x[n-1], x[n], x[n+1]])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotting the Accumulator system
plt.subplot(3, 2, 6)
plt.stem(t, accumulator_x, basefmt=" ")
plt.title('Accumulator System (Cumulative Sum)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)


plt.tight_layout()
plt.show()
