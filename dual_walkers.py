import numpy as np
import matplotlib.pyplot as plt

it_max = 100


xs = np.random.uniform(size=2)
ys = np.random.uniform(size=2)

path1 = np.zeros((2, it_max))
path2 = np.zeros((2, it_max))

for i in range(it_max):
    path1[:,i] = (xs[0], ys[0])
    path2[:,i] = (xs[1], ys[1])

    directions = 2*(np.random.randint(0,2,size=(2,2))-1/2)
    step_xs = ys[::-1]
    step_ys = xs[::-1]
    xs += step_xs*directions[0]
    ys += step_ys*directions[1]

plt.plot(path1[0], path1[1])
plt.plot(path2[0], path2[1])

plt.show()
