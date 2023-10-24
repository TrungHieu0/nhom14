import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from PIL import Image

# Hàm lưu hình ảnh đã được xử lý
def save_image(image):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        try:
            image.save(file_path)
            messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {e}")



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
    kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
    kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, 2, 8, 2, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, -1, -1, -1, -1]]) / 8.0

    output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
    output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
    output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

    display_image(output_1, 'Sharpening')
    display_image(output_2, 'Excessive Sharpening')
    display_image(output_3, 'Edge Enhancement')


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

# Label để hiển thị hình ảnh
label = tk.Label(root)
label.pack()

# Chạy vòng lặp chính của Tkinter
root.mainloop()
