import matplotlib.pyplot as plt
import numpy as np
from skimage import draw
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from collections import defaultdict


def has_vline(arr):
    return 1. in arr.image.mean(0)
def has_hline(arr):
    return 1. in arr.image.mean(1)

def up_touch(prop):
    line = np.zeros(len(prop.image[0]) + 2)
    count = 0
    st = 0
    for i in range(1, len(line)):
        if i < len(prop.image[0])-2 and prop.image[0][i-1]:
            line[i] = 1
        if line[i] == st:
            pass
        else:
            st = line[i]
            count += 1
    return count

def down_touch(prop):
    y = prop.image.shape[0]-1
    line = np.zeros(len(prop.image[y]) + 2)
    count = 0
    st = 0
    for i in range(1, len(line)):
        if i < len(prop.image[y])-2 and prop.image[y][i-1]:
            line[i] = 1
        if line[i] == st:
            pass
        else:
            st = line[i]
            count += 1
    return count

def recognize(prop):
    if up_touch(prop) == 4:
        return "K"
    if down_touch(prop) == 4:
        return "R"
    if not has_hline(prop):
        return "D"
    if prop.image[0][0]:
        return "J"
    else:
        return "L"

image = plt.imread(r"images/task3.png")
image = image.mean(2)
binary = image > 0.250
labeled = label(binary)
props = regionprops(labeled)
count = 0
result = {}
for prop in props:
    symbol = recognize(prop)
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1
    count += 1
print(result)
print(count)
print(len(props))

# R 1   d   up_touch 2  down_touch 4  has_hline True
# L 6      up_touch 2  down_touch 2  has_hline True
# J 0      up_touch 2  down_touch 2  has_hline True
# K 3   d   up_touch 4  down_touch 4  has_hline False
# D 10  d  up_touch 2  down_touch 2  has_hline False


