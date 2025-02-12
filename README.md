# Steganography Project

## 📜 Brief Description
This is a **Python-based Steganography project** that allows users to hide secret messages inside images and retrieve them later. The project uses the OpenCV library for image processing and Tkinter for the graphical user interface (GUI). It provides a simple and intuitive way to encrypt and decrypt messages within images.

---

## 🛠️ Detailed Description

### What is Steganography?
Steganography is the practice of hiding secret information within a non-secret medium, such as an image, audio, or video file. In this project, the secret message is embedded into the pixel values of an image, making it invisible to the naked eye.

### Features
- **Encryption**: Hide a secret message inside an image.
- **Decryption**: Extract the hidden message from the image.
- **Password Protection**: Secure the hidden message with a password.
- **User-Friendly GUI**: Built with Tkinter for ease of use.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

### How It Works
1. **Encryption**:
   - The user selects an image and enters a secret message and password.
   - The message is embedded into the pixel values of the image.
   - The modified image is saved as `encryptedImage.png`.

2. **Decryption**:
   - The user selects the encrypted image and enters the password.
   - The hidden message is extracted from the pixel values of the image.
   - The decrypted message is displayed in a pop-up window.

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.x installed on your system.
- Required Python libraries: `opencv-python`, `tkinter`.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
