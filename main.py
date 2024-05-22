import numpy as np
import matplotlib.pyplot as plt

size = 100
# simplenumslist = []
mama = np.zeros((size, size))

for i in range(size*size):
    # for inner in range(i, size*size):
    for inner in range(i + 1):
        if i > 1 and inner > 1:
            if i % inner == 0 and i != inner:
                mama[i//size][i%size] = 0
                break
            elif i == inner:
                mama[i//size][i%size] = 255
                # simplenumslist.append(i)  

plt.imshow(mama, cmap = "summer")
plt.show()
