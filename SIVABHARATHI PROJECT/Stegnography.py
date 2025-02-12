import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to encrypt the message in the image
def encrypt_image():
    img_path = img_path_entry.get()
    msg = msg_entry.get()
    password = password_entry.get()

    if not img_path or not msg or not password:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    img = cv2.imread(img_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image path!")
        return

    # Store the message length in the first pixel
    msg_length = len(msg)
    img[0, 0, 0] = msg_length  # Store length in the first pixel (R channel)

    # Encrypt the message
    d = {chr(i): i for i in range(255)}
    m, n, z = 0, 1, 0  # Start from the second pixel to avoid overwriting the length

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_path = "encryptedImage.png"
    cv2.imwrite(encrypted_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save without compression
    messagebox.showinfo("Success", f"Image encrypted and saved as {encrypted_path}")
    os.system(f"start {encrypted_path}")  # Open the image on Windows

# Function to decrypt the message from the image
def decrypt_image():
    encrypted_path = encrypted_path_entry.get()
    password = decrypt_password_entry.get()

    if not encrypted_path or not password:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    img = cv2.imread(encrypted_path, cv2.IMREAD_UNCHANGED)  # Load image without modification
    if img is None:
        messagebox.showerror("Error", "Invalid image path!")
        return

    # Retrieve the message length from the first pixel
    msg_length = img[0, 0, 0]

    # Decrypt the message
    c = {i: chr(i) for i in range(255)}
    m, n, z = 0, 1, 0  # Start from the second pixel
    message = ""

    if password == password_entry.get():
        for _ in range(msg_length):  # Use the stored message length
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        messagebox.showinfo("Decrypted Message", f"Decrypted message: {message}")
    else:
        messagebox.showerror("Error", "Incorrect password!")

# Function to open file dialog for image selection
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    img_path_entry.delete(0, tk.END)
    img_path_entry.insert(0, file_path)

# Function to open file dialog for encrypted image selection
def browse_encrypted_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    encrypted_path_entry.delete(0, tk.END)
    encrypted_path_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("Image Steganography")

# Create and place widgets
tk.Label(root, text="Image Path:").grid(row=0, column=0, padx=10, pady=5)
img_path_entry = tk.Entry(root, width=40)
img_path_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_image).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Secret Message:").grid(row=1, column=0, padx=10, pady=5)
msg_entry = tk.Entry(root, width=40)
msg_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Encrypt", command=encrypt_image).grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Encrypted Image Path:").grid(row=4, column=0, padx=10, pady=5)
encrypted_path_entry = tk.Entry(root, width=40)
encrypted_path_entry.grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_encrypted_image).grid(row=4, column=2, padx=10, pady=5)

tk.Label(root, text="Decryption Password:").grid(row=5, column=0, padx=10, pady=5)
decrypt_password_entry = tk.Entry(root, width=40, show="*")
decrypt_password_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Button(root, text="Decrypt", command=decrypt_image).grid(row=6, column=1, padx=10, pady=10)


# Run the main loop
root.mainloop()
