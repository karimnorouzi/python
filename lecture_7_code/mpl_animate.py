import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as animation
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 128)
line, = ax.plot(x, -1/2*np.sin(x))
def animate(i):
    line.set_ydata((i-100)/200*np.sin(x))  # Update the y-data for animation
    return line,
ani = animation.FuncAnimation(fig, animate, frames=200, interval=100, blit=False)
plt.title('Animation Example: Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()
