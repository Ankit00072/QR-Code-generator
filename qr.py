import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        self.text_label = ttk.Label(root, text="Enter Text:")
        self.text_label.grid(row=0, column=0, padx=10, pady=10)

        self.text_entry = ttk.Entry(root, width=30)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.qr_code_image_label = ttk.Label(root, text="QR Code will appear here.")
        self.qr_code_image_label.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_qr_code(self):
        text_to_encode = self.text_entry.get()

        if text_to_encode:
            # Create a QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text_to_encode)
            qr.make(fit=True)

            # Create an image from the QR code instance
            qr_code_image = qr.make_image(fill_color="black", back_color="white")

            # Display the image in the GUI
            self.display_qr_code_image(qr_code_image)
        else:
            self.qr_code_image_label.configure(text="Please enter text to generate a QR code.")

    def display_qr_code_image(self, image):
        # Convert PIL Image to PhotoImage
        img_tk = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.qr_code_image_label.configure(image=img_tk)
        self.qr_code_image_label.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
