import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)


print(data)

plt.scatter(data[:,0],data[:,3],c='b',s=data[:,5]*20)

print(min(data[:,0]))
print(max(data[:,0]))
print(sum(data[:,0])/len(data[:,0]))
arr=[]

for i,item in enumerate(data[:,1]):
    if item >=6:
        arr.append(data[i,0])
        
print("min: ", min(arr))
print("max: ", max(arr))
print("avg: ", sum(arr)/len(arr))
    
plt.show()