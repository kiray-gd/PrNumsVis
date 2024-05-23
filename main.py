import numpy as np
import matplotlib.pyplot as plt
import datetime
import math

# условный старт
start_time = datetime.datetime.now()

size = 1000

# Создание массива mama
mama = np.zeros((size, size), dtype=np.uint8)  # Указать тип данных для эффективности

# v3
def prime6(upto=1000000):
    primes=np.arange(3,upto+1,2)
    isprime=np.ones((upto-1)//2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))//2]:
        if isprime[(factor-2)//2]: isprime[(factor*3-2)//2::factor]=0
    return np.insert(primes[isprime],0,2)

result = prime6(size*size)
for i in result:
    mama[i//size][i%size] = 255

# v2
# for i in range(size*size):
#     if i > 1:
#         branch = np.full(i, i)
#         deviders = np.arange(1, i + 1)
#         result = branch % deviders
#         if np.count_nonzero(result == 0) <= 2:
#            mama[i//size][i%size] = 255
#         else:
#             mama[i//size][i%size] = 0
        
# v1
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

plt.imshow(mama, cmap = "hot")
plt.show()

