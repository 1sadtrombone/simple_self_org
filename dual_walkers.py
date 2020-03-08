import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

it_max = 100

x = [np.random.uniform()]
y = [np.random.uniform()]

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'r-')
pt, = plt.plot([], [], 'C0.')

def init():
    size = 10
    ax.set_xlim(-size,size)
    ax.set_ylim(-size,size)
    return ln,

def update(frame):

    direction = 2*(np.random.randint(0,2,size=2)-1/2)
    step_x = y[-1]
    step_y = x[-1]
    x.append(x[-1] + step_x*direction[0])
    y.append(y[-1] + step_y*direction[1])

    ln.set_data(x, y)
    pt.set_data(x[-1], y[-1])
    return ln,

ani = FuncAnimation(fig, update, frames=np.empty(it_max), init_func=init)

ani.save("step_walker.mp4")

plt.show()
