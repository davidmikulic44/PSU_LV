from matplotlib import pyplot as plt
from skimage.transform import resize
import matplotlib.image as mpimg
import numpy as np


img = plt.imread("C:\\Users\\student\\Desktop\\psulv2\\3zad\\tiger.png")
img = img[:,:,0].copy()

img_array=[]

img_array=img+0.6
img_array[img_array>1]=1

    
img1 = np.rot90(img,3) #zakrenuta slika

img2 = np.fliplr(img) #zrcaljena slika


img1_1 = [[img_array[j][i] for j in range(len(img_array))] for i in range(len(img_array[0]))]
img1_1 = np.fliplr(img1_1)

img3 = img_array[::5,::5] #smanjena kvaliteta

plt.figure(1)
plt.title("Brightness")
plt.imshow(img_array,cmap='gray') #brightness
plt.figure(2)
plt.title("Rotirana slika")
plt.imshow(img1,cmap='gray')
plt.show()
