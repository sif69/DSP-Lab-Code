import numpy as np
import matplotlib.pyplot as plt


l = 20
t = np.arange(-10, 19)
a = 0.9

# Unit-step Signal
y_step = np.where(t >= 0, 1, 0)

# Unit-ramp Signal
y_ramp = np.where(t >= 0, t, 0)

# Impulse Signal
y_impluse = np.where(t == 0, 1, 0)

# Exponential Signal
y_exp = np.where(t >= 0, a ** t, 0)

# Plot Unit-Step Signal
plt.figure(figsize=(10, 6))
plt.subplot(2,2,1)
plt.stem( y_step, basefmt='')
plt.title('Unit-Step Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Unit-Ramp Signal
plt.subplot(2,2,2)
plt.stem(y_ramp, basefmt='')
plt.title('Unit-Ramp Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Impulse Signal

plt.subplot(2,2,3)
plt.stem(y_impluse, basefmt='')
plt.title('Impulse Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Exponential Signal
plt.subplot(2,2,4)
plt.stem(y_exp, basefmt='')
plt.title('Exponential Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
