import tkinter as tk
import random
from sample import sample_function
root = tk.Tk()
root.title("Os LAB")
size = "800x800"
root.geometry(size)

def algo(window, algorithm, queue):
    output = sample_function(queue)
    out = f"Input Queue: {queue}\n\n\nOutput: {output}"
    label = tk.Label(window, text=out).grid(row=20, column=1)

def show_sub(second, queue):
    def pr():
        lab.config(text=op.get())
    third = tk.Toplevel()
    second.withdraw()
    third.geometry(size)
    lab = tk.Label(third)
    modes = [
        ("Default Algo"),
        ("1st Algo"),
        ("2nd Algo"),
        ("3rd Algo"),
        ("4th Algo"),
    ]
    op = tk.StringVar()
    op.set("Default Algo")
    option = tk.OptionMenu(third, op, *modes)
    option.grid(row=0, column=1)
    b = tk.Button(third, text="Show Selection", command=pr).grid(row=5, column=1)
    lab.grid(row=8, column=1)
    b1 = tk.Button(third, text="Go to Main", command=lambda:show_1(third)).grid(row=5, column=0)
    b2 = tk.Button(third, text="Output dede", command=lambda:algo(third, op.get(), queue)).grid(row=5, column=2)


def show_2():        
    second = tk.Toplevel()
    root.withdraw()
    second.geometry(size)
    def generate_random_queue(length):
        queue = []
        for i in range(length):
            pid = random.randint(0,10)
            bust = random.randint(0,20)
            arrival = random.randint(0,20)
            queue.append((pid,bust,arrival))
        return queue
    random_queue = generate_random_queue(length = 6)
    v = tk.Label(second, text=f"Your Queue is: {random_queue}").grid(row=0, column=1)
    b1 = tk.Button(second, text="Go to Main", command=lambda:show_1(second)).grid(row=1, column=0)
    b2 = tk.Button(second, text="Submit", command=lambda:show_sub(second, random_queue)).grid(row=1, column=2)


def show_1(second):
    root.deiconify()
    second.withdraw()


def show_3():
    second = tk.Toplevel()
    second.geometry(size)
    root.withdraw()
    e1 = tk.Entry(second)
    e2 = tk.Entry(second)
    e3 = tk.Entry(second)
    lab1 = tk.Label(second, text="Process ID:").grid(row=0, column=0)
    lab2 = tk.Label(second, text="Bust Time:").grid(row=0, column=1)
    lab3 = tk.Label(second, text="Arrival Time:").grid(row=0, column=2)
    e1.grid(row=1, column=0, padx=5, pady=2)
    e2.grid(row=1, column=1, padx=5, pady=2)
    e3.grid(row=1, column=2, padx=5, pady=2)
    queue = []
    def add_process():
        queue.append((int(e1.get()), int(e2.get()), int(e3.get())))
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    b1 = tk.Button(second, text="Go to Main", command=lambda:show_1(second))
    b2 = tk.Button(second, text="Add Process", command=add_process)
    b3 = tk.Button(second, text="Submit", command=lambda:show_sub(second, queue))

    b1.grid(row=10, column=0)
    b2.grid(row=10, column=1)
    b3.grid(row=10, column=2)

b1 = tk.Button(root, bg="red", text="Random Queue", command=show_2).pack()
b2 = tk.Button(root, bg="blue", text="Create Own", command=show_3).pack()
b3 = tk.Button(root, bg="green", text="Quit", command=root.quit).pack()
root.mainloop()