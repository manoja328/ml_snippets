import scipy
from scipy.io import loadmat
from pathlib import Path
%matplotlib inline
from PIL import Image
import os
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon

def showAnns(ax, anns):
    """
        ax: matplotlib axes
        anns: list of Nx2 arrays of polygons coordinates  (x,y)
    """
    
    polygons = []
    color = []
    for poly in anns:
        c = (np.random.random((1, 3))*0.6+0.4).tolist()[0]
        polygons.append(Polygon(poly))
        color.append(c)

    p = PatchCollection(polygons, facecolor=color, linewidths=0, alpha=0.4)
    ax.add_collection(p)
    p = PatchCollection(polygons, facecolor='none', edgecolors=color, linewidths=2)
    ax.add_collection(p)
    
    
 # using the variable ax for single a Axes
fig, ax = plt.subplots(1,2,figsize=(16,8))
pil = Image.open(IMGDIR/ fname)
ax[0].axis('off')
ax[0].imshow(pil)
ax[1].imshow(pil)
ax[1].set_autoscale_on(False)
ax[1].axis('off')
showAnns(ax[1],polys) #polys is a numpy array of shape N x 2 ( if N = 4 makes a bounding box ) 
