import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        result_var.set(password)
    except:
        result_var.set("Enter a valid number")

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(result_var.get())


window = tk.Tk()
window.title("Password Generator")
window.geometry("350x250")
window.resizable(False, False)


tk.Label(window, text="Clukh's Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(window, textvariable=result_var, width=30, justify="center").pack(pady=5)

tk.Button(window, text="Copy to Clipboard", command=copy_password).pack(pady=5)

window.mainloop()
