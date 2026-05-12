import tkinter as tk
from tkinter import messagebox

def convert_to_bgn():
    try:
        euro = float(entry.get())
        bgn = euro * 1.95583
        result_label.config(text=f"{bgn:.2f} BGN", fg = "darkgreen")
    except ValueError:
        messagebox.showerror("ГРЕШКА", "МОЛЯ ВЪВЕДЕТЕ ПРАВИЛНО ЧИСЛО!")
root=tk.Tk()
root.title("Конвертор EUR -> BGN")
root.geometry("300x250")

label_top = tk.Label(root, text="ВЪВЕДЕТЕ СУМА В ЕВРО:", font=("Arial", 12))
label_top.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

btn = tk.Button(root, text="ПРЕВЪРНИ В ЛЕВА", command=convert_to_bgn,
                bg="#007bff", fg="white", font=("Arial", 10, "bold"),
                padx=10, pady=5)
btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack()

root.mainloop()

