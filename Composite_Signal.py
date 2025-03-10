import numpy as np
import matplotlib.pyplot as plt

#version - 1
# Time range (0 to 1 second with 0.001 step size)
t = np.arange(0, 1, 0.001)

# Define three sine waves with different frequencies and amplitudes
A1, f1 = 1, 5    # Amplitude=1, Frequency=5Hz
A2, f2 = 0.5, 15 # Amplitude=0.5, Frequency=15Hz
A3, f3 = 0.3, 30 # Amplitude=0.3, Frequency=30Hz

# Composite Signal (Sum of Sine Waves)
composite_signal = A1 * np.sin(2 * np.pi * f1 * t)  +  A2 * np.sin(2 * np.pi * f2 * t)  +  A3 * np.sin(2 * np.pi * f3 * t)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t, composite_signal, label="Composite Signal", color="b")
plt.title("Composite Signal: Sum of Multiple Sine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
# plt.legend()
# plt.show()







#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#version - 2

amplitude1 = 1.0
frequency1 = 1.0    # in Hertz


amplitude2 = 0.5
frequency2 = 3.0    # in Hertz


sampling_rate = 100        # in samples per second
duration = 2               # in seconds

time = np.arange(0, duration, 1/sampling_rate)


#Generating the Sine Wave
sine_wave1 = [amplitude1 * np.sin(2 * np.pi * frequency1 * t ) for t in time]

sine_wave2 = [amplitude2 * np.sin(2 * np.pi * frequency2 * t) for t in time]

#generating Composite Signal
composite_signal = [sine_wave1[i] + sine_wave2[i] for i in range(len(time))]


#plotting the signal
plt.figure(figsize=(10, 5))
plt.plot(time, composite_signal, label="Composite Signal")
plt.title("Composite Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
