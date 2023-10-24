import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Khởi tạo biến toàn cục để lưu hình ảnh
img = None

# Hàm xử lý sự kiện khi nút "Open Image" được nhấn
def open_image():
    global img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    display_image(img)

# Hàm xử lý sự kiện khi nút "Apply Filters" được nhấn
def apply_filters():
    global img
    if img is not None:
        # Define different filters
        kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
        kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                                    [-1, 2, 2, 2, -1],
                                    [-1, 2, 8, 2, -1],
                                    [-1, 2, 2, 2, -1],
                                    [-1, -1, -1, -1, -1]]) / 8.0
        
        # Apply filters
        output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
        output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
        output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)
        
        # Display filtered images
        display_image(output_1, 'Sharpening')
        display_image(output_2, 'Excessive Sharpening')
        display_image(output_3, 'Edge Enhancement')

# Hàm xử lý sự kiện khi nút "Save Image" được nhấn
def save_image():
    global img
    if img is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img_to_save = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imwrite(file_path, img_to_save)

# Hàm xử lý sự kiện khi nút "Resize Image" được nhấn
def resize_image():
    global img
    if img is not None:
        new_width = int(entry_width.get())
        new_height = int(entry_height.get())
        resized_img = cv2.resize(img, (new_width, new_height))
        display_image(resized_img, 'Resized Image')

# Hàm hiển thị hình ảnh trong cửa sổ
def display_image(image, window_title='Image'):
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image=image)
    label.config(image=photo)
    label.image = photo
    root.title(window_title)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Image Filters")

# Tạo nút để mở hình ảnh
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=20)

# Tạo nút để áp dụng bộ lọc
apply_button = tk.Button(root, text="Apply Filters", command=apply_filters)
apply_button.pack(pady=20)

# Tạo nút để lưu hình ảnh
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=20)

# Nhập chiều rộng mới
tk.Label(root, text="New Width:").pack()
entry_width = tk.Entry(root)
entry_width.pack()

# Nhập chiều cao mới
tk.Label(root, text="New Height:").pack()
entry_height = tk.Entry(root)
entry_height.pack()

# Tạo nút để thay đổi kích thước hình ảnh
resize_button = tk.Button(root, text="Resize Image", command=resize_image)
resize_button.pack(pady=20)

# Label để hiển thị hình ảnh
label = tk.Label(root)
label.pack()

# Chạy vòng lặp chính của Tkinter
root.mainloop()
