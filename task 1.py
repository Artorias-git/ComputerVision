import cv2
import numpy as np
from skimage import filters, measure

image = cv2.imread("images/task1.png", 0)

binary_image = (image == 51).astype(np.uint8)
inverted_arr = 1 - binary_image
_, labeled_regions = cv2.connectedComponents(inverted_arr)
mr = measure.regionprops(labeled_regions)

def areas(mr):
    arr = []
    for i in range(len(mr)):
        arr.append( mr[i].area - mr[i].perimeter)
    return arr
arr = areas(mr)
print(max(arr))
