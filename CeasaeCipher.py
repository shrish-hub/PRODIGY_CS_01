import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Algorithm
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Keep non-alphabetical characters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Function to handle encryption or decryption
def process_text():
    message = entry_text.get()
    shift = shift_value.get()
    
    if not message:
        messagebox.showerror("Error", "Please enter a message!")
        return
    
    if selected_option.get() == 1:  # Encrypt option
        result = encrypt(message, shift)
    elif selected_option.get() == 2:  # Decrypt option
        result = decrypt(message, shift)
    else:
        messagebox.showerror("Error", "Please select an option!")
        return
    
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, result)

# Creating the GUI window
root = tk.Tk()
root.title("Caesar Cipher")

# GUI Labels and Inputs
label_text = tk.Label(root, text="Enter your message:")
label_text.pack(pady=10)

entry_text = tk.Entry(root, width=50)
entry_text.pack(pady=10)

label_shift = tk.Label(root, text="Enter shift value:")
label_shift.pack(pady=10)

shift_value = tk.IntVar(value=3)  # Default shift value is 3
entry_shift = tk.Entry(root, textvariable=shift_value, width=10)
entry_shift.pack(pady=10)

selected_option = tk.IntVar()

radio_encrypt = tk.Radiobutton(root, text="Encrypt", variable=selected_option, value=1)
radio_encrypt.pack(pady=5)

radio_decrypt = tk.Radiobutton(root, text="Decrypt", variable=selected_option, value=2)
radio_decrypt.pack(pady=5)

button_process = tk.Button(root, text="Process", command=process_text)
button_process.pack(pady=10)

label_output = tk.Label(root, text="Output:")
label_output.pack(pady=10)

output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=10)

# Start the GUI loop
root.mainloop()
