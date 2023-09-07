from keras.models import load_model
import numpy as np
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg

filename = 'Test/00000.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img)
img = resize(img, (28, 28))


plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

model = load_model('model')
# TODO: napravi predikciju 

digit = np.argmax(model.predict(img), axis = -1)

# TODO: ispis rezultat
print("---------------------------------------------------")
print("Slika sadrzi znamenku: ", digit)
