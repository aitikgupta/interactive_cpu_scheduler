import tkinter as tk
root = tk.Tk()
root.title("Os LAB")
size = "400x200"
root.geometry(size)


def show_sub(second):
    def pr():
        lab.config(text=op.get())
    third = tk.Toplevel()
    second.withdraw()
    third.geometry(size)
    lab = tk.Label(third)
    modes = [
        ("Default Algo", "Default Algo"),
        ("1st Algo", "1st Algo"),
        ("2nd Algo", "2nd Algo"),
        ("3rd Algo", "3rd Algo"),
        ("4th Algo", "4th Algo"),
    ]
    op = tk.StringVar()
    op.set("Default Algo")
    option = tk.OptionMenu(third, op, *modes)
    option.grid(row=0, column=1)
    b = tk.Button(third, text="Show Selection", command=pr).grid(row=5, column=1)
    lab.grid(row=8, column=1)
    b1 = tk.Button(third, text="Go Back", command=lambda:show_1(third)).grid(row=5, column=0)
    b2 = tk.Button(third, text="Output dede").grid(row=5, column=2)



def show_2():
    second = tk.Toplevel()
    root.withdraw()
    second.geometry(size)
    v = tk.Label(second, text="Your Queue is: blabla").grid(row=0, column=1)
    b1 = tk.Button(second, text="Show First", command=lambda:show_1(second)).grid(row=1, column=0)
    b2 = tk.Button(second, text="Submit", command=lambda:show_sub(second)).grid(row=1, column=2)


def show_1(second):
    root.deiconify()
    second.withdraw()

def show_3():
    second = tk.Toplevel()
    second.geometry(size)
    root.withdraw()
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()
    e1 = tk.Entry(second)
    e2 = tk.Entry(second)
    e3 = tk.Entry(second)
    e1.grid(row=0, column=0, padx=5, pady=2)
    e2.grid(row=0, column=1, padx=5, pady=2)
    e3.grid(row=0, column=2, padx=5, pady=2)
    e1.insert(0, "Enter Process ID")
    e2.insert(0, "Enter Burst Time")
    e3.insert(0, "Enter Arrival Time")
    b1 = tk.Button(second, text="Show First", command=lambda:show_1(second))
    b2 = tk.Button(second, text="Submit", command=lambda:show_sub(second))
    b1.grid(row=10, column=0)
    b2.grid(row=10, column=2)

b1 = tk.Button(root, bg="red", text="Random Queue", command=show_2).pack()
b2 = tk.Button(root, bg="blue", text="Create Own", command=show_3).pack()
b3 = tk.Button(root, bg="green", text="Bitch I wanna quit", command=root.quit).pack()
root.mainloop()