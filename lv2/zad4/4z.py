import numpy as np
import matplotlib.pyplot as plt

def checkers(redovi, stupci):
    check = np.zeros((redovi, stupci))

    for i in range(redovi):
        for j in range(stupci):
            if(i%2==0):
                if(j%2!=0):
                    check[i][j]=1
            if(i%2!=0):
                if(j%2==0):
                    check[i][j]=1
    
    return check


check = checkers(5,5)

plt.matshow(check, cmap='gray')
plt.show()
