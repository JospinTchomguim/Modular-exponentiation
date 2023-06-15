import tkinter as tk

def power_modulo(n, e, p):
    result = 1
    n = n % p
    
    while e > 0:
        if e % 2 == 1:
            result = (result * n) % p
        
        e = e // 2
        n = (n * n) % p
    
    return result

def calculate():
    n = int(entry_n.get())
    e = int(entry_e.get())
    p = int(entry_p.get())
    result = power_modulo(n, e, p)
    label_result.config(text=str(result))

root = tk.Tk()
root.title("Exponentiation modulaire")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_n = tk.Label(frame_input, text="n")
label_n.pack(side="left", padx=5)

entry_n = tk.Entry(frame_input, width=10)
entry_n.pack(side="left", padx=5)

label_e = tk.Label(frame_input, text="e")
label_e.pack(side="left", padx=5)

entry_e = tk.Entry(frame_input, width=10)
entry_e.pack(side="left", padx=5)

label_p = tk.Label(frame_input, text="p")
label_p.pack(side="left", padx=5)

entry_p = tk.Entry(frame_input, width=10)
entry_p.pack(side="left", padx=5)

button_calculate = tk.Button(root, text="Calculer", command=calculate)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
