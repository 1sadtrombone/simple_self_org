import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers

it_max = 100

x = [0]
y = [0]

print(x,y)

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'r-')
pt, = plt.plot([], [], 'C0.')

def init():
    ax.set_xlim(-50,50)
    ax.set_ylim(-50,50)
    return ln,

def update(frame):

    roll = np.random.random(size=2)
    p_right = np.abs(y[-1]) / np.sqrt(y[-1]**2 + x[-1]**2)
    p_up = np.abs(x[-1]) / np.sqrt(y[-1]**2 + x[-1]**2)
    direction_x = 2*((p_right > roll[0])-1/2)
    direction_y = 2*((p_up > roll[1])-1/2)
    x.append(x[-1] + direction_x)
    y.append(y[-1] + direction_y)

    ln.set_data(x, y)
    pt.set_data(x[-1], y[-1])
    return ln,

ani = FuncAnimation(fig, update, frames=np.empty(it_max), init_func=init)

#ani.save('diag2.mp4')

plt.show()
