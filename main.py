import tkinter as tk
from tkinter import messagebox
import config
from converter import convert_currency
from exceptions import InvalidCurrencyError, NegativeAmountError

def on_convert_click():
    try:
        amt = float(amount_entry.get())
        res = convert_currency(amt, currency_from_entry.get(), currency_to_entry.get())
        result_label.config(text=f"{res:,.0f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ!")
    except (InvalidCurrencyError, NegativeAmountError) as e:
        messagebox.showerror("Lỗi nghiệp vụ", str(e))

root = tk.Tk()
root.title(config.APP_TITLE)
root.geometry("530x400+0+0")
root.configure(bg="#484040")

label_title = tk.Label(root, text=config.APP_TITLE, font=("Arial", 16), bg="#484040", fg="white")
label_title.place(x=100, y=20)

amount_label = tk.Label(root, text="Amount: ", font=("Arial", 12), bg="#484040", fg="white")
amount_label.place(x=50, y=80)

amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.place(x=250, y=80)

currency_from_label = tk.Label(root, text="From (Currency Code): ", font=("Arial", 12), bg="#484040", fg="white")
currency_from_label.place(x=50, y=120)

currency_from_entry = tk.Entry(root, font=("Arial", 12))
currency_from_entry.place(x=250, y=120)

currency_to_label = tk.Label(root, text="To (Currency Code): ", font=("Arial", 12), bg="#484040", fg="white")
currency_to_label.place(x=50, y=160)

currency_to_entry = tk.Entry(root, font=("Arial", 12))
currency_to_entry.place(x=250, y=160)

convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=on_convert_click)
convert_button.place(x=200, y=200)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#484040", fg="white")
result_label.place(x=50, y=240)


root.mainloop()