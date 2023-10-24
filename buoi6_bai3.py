import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc hình ảnh
img = cv2.imread('test.png')

# Hiển thị hình ảnh gốc
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Chuyển đổi hình ảnh thành ảnh grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Chuẩn hóa ảnh grayscale
normalized_gray_img = cv2.normalize(gray_img, None, 0, 255, cv2.NORM_MINMAX)

# Hiển thị hình ảnh gốc
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Hiển thị ảnh đã được chuẩn hóa
plt.subplot(1, 2, 2)
plt.title("Normalized")
plt.imshow(normalized_gray_img, cmap='gray')
plt.axis('off')

plt.show()
