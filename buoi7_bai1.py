import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk

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
    if img is None:
        messagebox.showerror("Error", "Please open an image first.")
        return

    filter_type = simpledialog.askstring("Filter Type", "Enter filter type (sharpen, blur, grayscale):")
    if filter_type == "sharpen":
        kernel_sharpen = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])
        output = cv2.filter2D(img, -1, kernel_sharpen)
    elif filter_type == "blur":
        output = cv2.GaussianBlur(img, (15, 15), 0)
    elif filter_type == "grayscale":
        output = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2RGB)
    else:
        messagebox.showerror("Error", "Invalid filter type.")
        return

    display_image(output, f'{filter_type.capitalize()} Filtered')

# Hàm lưu hình ảnh đã được xử lý
def save_image(image):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        try:
            image.save(file_path)
            messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

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

# Tạo nút để lưu hình ảnh đã được xử lý
save_button = tk.Button(root, text="Save Image", command=lambda: save_image(Image.fromarray(img)))
save_button.pack(pady=20)

# Label để hiển thị hình ảnh
label = tk.Label(root)
label.pack()

# Hình ảnh được mở
img = None

# Chạy vòng lặp chính của Tkinter
root.mainloop()
