import numpy as np
import matplotlib.pyplot as plt
import datetime

# условный старт
start_time = datetime.datetime.now()

size = 1000
# simplenumslist = []
mama = np.zeros((size, size))

for i in range(size*size):
    if i > 1:
        branch = np.full(i, i)
        deviders = np.arange(1, i + 1)
        result = branch % deviders
        if np.count_nonzero(result == 0) <= 2:
           mama[i//size][i%size] = 255
        else:
            mama[i//size][i%size] = 0
        
# for i in range(size*size):
#     for inner in range(i + 1):
#         if i > 1 and inner > 1:
#             if i % inner == 0 and i != inner:
#                 mama[i//size][i%size] = 0
#                 break
#             elif i == inner:
#                 mama[i//size][i%size] = 255 

# условный конец выполнения кода
end_time = datetime.datetime.now()
total_time = end_time - start_time
print("Время выполнения:", total_time.total_seconds()," sec")

plt.imshow(mama, cmap = "summer")
plt.show()

