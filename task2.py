import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/task2.png")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def hsv_zero(c, hsv_image):
    max_value = 0
    for i in range(len(hsv_image)):
        for j in range(len(hsv_image[i])):
            if hsv_image[i][j][c] > max_value:
                max_value = hsv_image[i][j][c]

    for i in range(len(hsv_image)):
        for j in range(len(hsv_image[i])):
            if hsv_image[i][j][c] != max_value:
                hsv_image[i][j] = [0, 0, 0]
    return hsv_image

hsv_image = hsv_zero(1, hsv_image)
hsv_image = hsv_zero(2, hsv_image)

plt.imshow(hsv_image)
plt.show()
