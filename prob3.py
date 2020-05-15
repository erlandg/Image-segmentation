import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Image segmentation
im = np.array(Image.open('Fig0630(01)(strawberries_fullcolor).tif')).astype('float')/255
P = im.shape[0]; Q = im.shape[1]
SS = im[25:325,25:325]
a = np.mean(SS, axis=(0,1))
C = np.dstack([np.cov(im[:,:,0]), np.cov(im[:,:,1]), np.cov(im[:,:,2])])

plt.subplot(121)
plt.imshow(im, cmap='binary_r', vmin=0, vmax=1)
plt.subplot(122)
plt.imshow(im[25:325,25:325], cmap='binary_r', vmin=0, vmax=1)
# plt.show()
plt.clf()

DR = np.sqrt(np.absolute((im[:,:,0] - a[0]).T / C[:,:,0] * (im[:,:,0] - a[0])))
DG = np.sqrt(np.absolute((im[:,:,1] - a[1]).T / C[:,:,1] * (im[:,:,1] - a[1])))
DB = np.sqrt(np.absolute((im[:,:,2] - a[2]).T / C[:,:,2] * (im[:,:,2] - a[2])))
D = np.dstack([DR, DG, DB])
plt.imshow(D)
plt.colorbar()
# plt.show()
plt.clf()

newim = im.copy()
D0 = 2
for v in range(Q):
    for u in range(P):
        if np.linalg.norm(D[u,v,:]) >= D0: newim[u,v] = 0
plt.title(r'$D_0 = %g$' % D0)
plt.imshow(newim)
plt.show()
