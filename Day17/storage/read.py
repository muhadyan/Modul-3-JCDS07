from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 'L': B/W, 'RGBA': rgba, 'CMYK': cmyk
gbr = np.array(Image.open('0.jpg').convert('L'))
print(gbr.shape)

# # show pic Cara 1
# plt.imshow(gbr, cmap='gray')
# plt.show()

# show pic Cara 2
img = Image.fromarray(gbr, 'L')
img.show()

# # ngesave gambarnya (bisa ubah format juga)
# img.save('1.png')