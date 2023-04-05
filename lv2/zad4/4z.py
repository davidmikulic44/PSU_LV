import numpy as np
import matplotlib.pyplot as plt
check = np.zeros((5, 5))

redovi = len(check)
stupci = len(check[0])

for i in range(redovi):
    for j in range(stupci):
        if(i%2==0):
            if(j%2!=0):
                check[i][j]=1
        if(i%2!=0):
            if(j%2==0):
                check[i][j]=1

plt.matshow(check, cmap='gray')
plt.show()
