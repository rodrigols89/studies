import matplotlib.pyplot as plt
import numpy as np


# Angles from 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)

# Coordinates x and y of the unit circle
x = np.cos(theta)
y = np.sin(theta)

# Create the plot
plt.figure(figsize=(6, 6))
plt.plot(x, y)

# Add title and axis labels
plt.title("Unit Circle")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Set axis limits
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)

# Draw x and y axes
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

# Mark points (0,0) and (1,0)
plt.plot(0, 0, "ro")  # origin
plt.plot(1, 0, "ro")  # point (1,0)

# Display the plot
plt.grid(True)
plt.show()
