import tkinter as tk
import random
from sample import sample_function
from tkinter import messagebox
root = tk.Tk()
root.title("Interactive CPU Scheduler")
size = "1000x300"
root. configure(bg="grey")
root.geometry(size)

def algo(window, algorithm, queue):
    output = sample_function(queue)
    out = f"Input Queue: {queue}\n\n\nOutput: {output}"
    label = tk.Label(window, text=out).grid(row=20, column=1)

def goto_submission(second, queue):
    def pr():
        lab.config(text=op.get())
    third = tk.Toplevel()
    second.withdraw()
    third.configure(bg="grey")
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
    option.grid(row=0, column=1,padx=150, pady=40)
    b = tk.Button(third, text="Show Algorithm", height=2, width=20, command=pr)
    b.grid(row=5, column=1, padx=100, pady=30, sticky=tk.NSEW)
    lab.grid(row=8, column=1)
    b1 = tk.Button(third, text="Go to Main", height=2, width=20, command=lambda:goto_main(third))
    b1.grid(row=5, column=0, padx=100, pady=30, sticky=tk.NSEW)
    b2 = tk.Button(third, text="Show Output", height=2, width=20, command=lambda:algo(third, op.get(), queue))
    b2.grid(row=5, column=2, padx=100, pady=30, sticky=tk.NSEW)

def goto_random_queue():
    second = tk.Toplevel()
    root.withdraw()
    second.configure(bg="grey")
    second.geometry(size)
    def generate_random_queue(length):
            queue = []
            choices = list(range(0,10))
            random.shuffle(choices)
            for i in range(length):
                pid = choices.pop()
                burst_time = random.randint(0, 20)
                arr_time = random.randint(0, 20)
                queue.append((pid, burst_time, arr_time))
            return queue
    random_queue = generate_random_queue(length = 6)
    v = tk.Label(second, text="Your Queue is:", bg="grey", font=("New Times Roman", 40, "bold"))
    m = tk.Label(second, text=f"{random_queue}", bg="grey", font=("Verdana", 15, "bold"))
    b1 = tk.Button(second, text="Go to Main", height=3, command=lambda: goto_main(second))
    b2 = tk.Button(second, text="Submit", height=3, command=lambda: goto_submission(second, random_queue))
    v.grid(row=0, column=4, pady=20, padx=320, columnspan=5, rowspan=2)
    m.grid(row=2, column=1, pady=10, padx=55, columnspan=10, rowspan=2)
    b1.grid(row=4, column=6, sticky=tk.NSEW, padx=125, pady=20, columnspan=2)
    b2.grid(row=4, column=5, sticky=tk.NSEW, padx=125, pady=20, columnspan=2)

def goto_main(second):
    root.deiconify()
    second.withdraw()


def goto_user_queue():
    second = tk.Toplevel()
    second.configure(bg="grey")
    second.geometry(size)
    root.withdraw()
    e1 = tk.Entry(second)
    e2 = tk.Entry(second)
    e3 = tk.Entry(second)
    lab1 = tk.Label(second, text="Process ID:", bg="grey", font=("New Times Roman", 25, "bold"))
    lab2 = tk.Label(second, text="Burst Time:", bg="grey", font=("New Times Roman", 25, "bold"))
    lab3 = tk.Label(second, text="Arrival Time:", bg="grey", font=("New Times Roman", 25, "bold"))
    e1.grid(row=1, column=0, padx=110, ipady=5, ipadx=2)
    e2.grid(row=1, column=1, padx=100, ipady=5, ipadx=2)
    e3.grid(row=1, column=2, padx=110, ipady=5, ipadx=2)
    lab1.grid(row=0, column=0, padx=20, pady=30)
    lab2.grid(row=0, column=1, padx=20, pady=30)
    lab3.grid(row=0, column=2, padx=20, pady=30)
    global row
    row = 30
    queue = []
    def give_row():
        global row
        row += 1
        return row
    def add_process():
        try:
            pid = int(e1.get())
            burst_time = int(e2.get())
            arr_time = int(e3.get())
        except:
            messagebox.showerror("Invalid Input!", "One or more than one inputs aren't integers. Retry.")
            return
        user_process = (pid, burst_time, arr_time)
        for pr in queue:
            if user_process[0] == pr[0]:
                messagebox.showerror("Process IDs should be unique!", "You entered a Process ID which isn't unique.")
                e1.delete(0, tk.END)
                return
        if len(queue) > 6:
            messagebox.showwarning("Max Inputs Reached!", "User can input maximum of 7 processes.")
            return
        values = tk.Label(second, text = str(user_process)).grid(row=give_row(), column=1)
        queue.append(user_process)
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    b1 = tk.Button(second, text="Go to Main", height=2, command=lambda:goto_main(second))
    b2 = tk.Button(second, text="Add Process",height=2,  command=add_process)
    b3 = tk.Button(second, text="Submit",height=2, command=lambda:goto_submission(second, queue))

    b1.grid(row=2, column=2, padx=50, pady=50, sticky=tk.NSEW)
    b2.grid(row=2, column=0, padx=50, pady=50, sticky=tk.NSEW)
    b3.grid(row=2, column=1, padx=50, pady=50, sticky=tk.NSEW)
w = tk.Label(root, text = "Make Your Choice", bg="grey", font=('Times New Roman',30,'bold'))
b1 = tk.Button(root, text="Random Queue", height=3, command=goto_random_queue)
b2 = tk.Button(root, text="Create Own", height=3, command=goto_user_queue)
b3 = tk.Button(root, text="Quit",height=3, command=root.quit)
w.grid(row=0, column=1, padx=340, pady=40, columnspan=3)
b1.grid(row=1, column=1, sticky=tk.NSEW, padx=40, pady=30)
b2.grid(row=1, column=2, sticky=tk.NSEW, padx=40, pady=30)
b3.grid(row=1, column=3, sticky=tk.NSEW, padx=40, pady=30)

root.mainloop()
