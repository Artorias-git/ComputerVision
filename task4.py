import cv2
import numpy as np
from skimage import filters, measure
import matplotlib.pyplot as plt
def find_circly(mr):
    arr = []
    max = mr[0].area
    for i in range(1, len(mr)):
        if mr[i].area > max:
            max = mr[i].area
            arr = [i, mr[i].axis_major_length, mr[i].axis_minor_length]
    return arr
def cicler(image_path):
    image = cv2.imread(image_path, 0) # чб картинка
    binary_image = (image < filters.threshold_otsu(image)).astype(np.uint8)
    _, labeled_regions = cv2.connectedComponents(binary_image) # _ выбросить общее число меток
    mr = measure.regionprops(labeled_regions)
    return mr
image_path = "images/task4.jpg"
mr = cicler(image_path)
arr = find_circly(mr)
lenth = (arr[1] + arr[2])/ 2
print(lenth)
lenth *= 1.05714
print(lenth)
