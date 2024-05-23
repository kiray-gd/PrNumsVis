import numpy as np
import matplotlib.pyplot as plt

size = 4
# simplenumslist = []
mama = np.zeros((size, size))

for i in range(size*size):
    if i > 1:
        branch = np.full(i, i)
        deviders = np.arange(1, i + 1)
        print(branch)
        print(deviders)
        result = branch % deviders
        print("res:", result)
        if np.count_nonzero(result == 0) <= 2:
           mama[i//size][i%size] = 0
        else:
            mama[i//size][i%size] = 255
        print(np.count_nonzero(result == 0))
        
        # mama[i//size][i%size] = result
        
    


# for i in range(size*size):
#     for inner in range(i + 1):
#         if i > 1 and inner > 1:
#             if i % inner == 0 and i != inner:
#                 mama[i//size][i%size] = 0
#                 break
#             elif i == inner:
#                 mama[i//size][i%size] = 255
                # simplenumslist.append(i)  

plt.imshow(mama, cmap = "summer")
plt.show()
