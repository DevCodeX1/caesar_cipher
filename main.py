import tkinter as tk
from tkinter import ttk

def encode_caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decode_caesar_cipher(text, shift):
    return encode_caesar_cipher(text, -shift)

def encode_text():
    shift = int(shift_entry.get())
    text = encode_box.get("1.0", tk.END).strip()
    encoded = encode_caesar_cipher(text, shift)
    decode_box.delete("1.0", tk.END)
    decode_box.insert(tk.END, encoded)

def decode_text():
    shift = int(shift_entry.get())
    text = decode_box.get("1.0", tk.END).strip()
    decoded = decode_caesar_cipher(text, shift)
    encode_box.delete("1.0", tk.END)
    encode_box.insert(tk.END, decoded)

# Create main window
root = tk.Tk()
root.title("Caesar Cipher Encoder/Decoder")

# Apply some styling
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Create and place widgets
ttk.Label(root, text="Shift:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
shift_entry = ttk.Entry(root, width=5)
shift_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

ttk.Label(root, text="Text to Encode:").grid(row=1, column=0, padx=10, pady=10, sticky="nw")
encode_box = tk.Text(root, height=10, width=50, font=("Helvetica", 12), wrap=tk.WORD)
encode_box.grid(row=1, column=1, padx=10, pady=10, sticky="w")

ttk.Label(root, text="Text to Decode:").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
decode_box = tk.Text(root, height=10, width=50, font=("Helvetica", 12), wrap=tk.WORD)
decode_box.grid(row=2, column=1, padx=10, pady=10, sticky="w")

encode_button = ttk.Button(root, text="Encode", command=encode_text)
encode_button.grid(row=3, column=0, padx=10, pady=10, sticky="e")

decode_button = ttk.Button(root, text="Decode", command=decode_text)
decode_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Apply padding to all widgets
for widget in root.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Set a minimum size for the window
root.minsize(600, 400)

# Run the application
root.mainloop()