import tkinter as tk
import random
from sample import sample_function
from tkinter import messagebox
from tkinter import *
root = tk.Tk()
root.title("Os LAB")
root.title("Interactive CPU Scheduler")
size = "700x300"
root.configure(bg="green")
size1= "300x250"
root.geometry(size1)

def algo(window, algorithm, queue):
    output = sample_function(queue)
    out = f"Input Queue: {queue}\n\n\nOutput: {output}"
    label = tk.Label(window, text=out).grid(row=20, column=1)

def goto_submission(second, queue):
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
    b = tk.Button(third, text="Show Algorithm", command=pr).grid(row=5, column=1)
    lab.grid(row=8, column=1)
    b1 = tk.Button(third, text="Go to Main", command=lambda:goto_main(third)).grid(row=5, column=0)
    b2 = tk.Button(third, text="Show Output", command=lambda:algo(third, op.get(), queue)).grid(row=5, column=2)

def goto_random_queue():        
    second = tk.Toplevel()
    root.withdraw()
    size2 = "425x200"
    second.configure(bg="green")
    second.geometry(size2)
    def generate_random_queue(length):
            queue = []
            choices = list(range(0,10))
            random.shuffle(choices)
            for i in range(length):
                pid = choices.pop()
                bust_time = random.randint(0,20)
                arr_time = random.randint(0,20)
                queue.append((pid,bust_time,arr_time))
            return queue
    random_queue = generate_random_queue(length = 6)
    v = tk.Label(second, text="Your Queue is:", bg="green", fg="purple",font=("New Times Roman", 18, "bold")).grid(row=0, column=2, pady=20, padx=25,columnspan=3 )
    m = tk.Label(second, text=f"{random_queue}", bg="orange", fg="midnight blue",font=("MS Sans Serif", 2, "bold")).grid(row=1,column=1, columnspan=5, pady=10,  padx=25)
    b1 = tk.Button(second, bg="yellow", text="Go to Main", command=lambda:goto_main(second)).grid(row=2, column=2,sticky=NSEW,padx=25, pady=20)
    b2 = tk.Button(second, bg="yellow",  text="Submit", command=lambda:goto_submission(second, random_queue)).grid(row=2, column=4,sticky=NSEW, padx=20, pady=20)


def goto_main(second):
    root.deiconify()
    second.withdraw()


def goto_user_queue():
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
            bust_time = int(e2.get())
            arr_time = int(e3.get())
        except:
            messagebox.showerror("Invalid Input!", "One or more than one inputs aren't integers. Retry.")
            return
        user_process = (pid, bust_time, arr_time)
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
    b1 = tk.Button(second, text="Go to Main", command=lambda:goto_main(second))
    b2 = tk.Button(second, text="Add Process", command=add_process)
    b3 = tk.Button(second, text="Submit", command=lambda:goto_submission(second, queue))

    b1.grid(row=10, column=0)
    b2.grid(row=10, column=1)
    b3.grid(row=10, column=2)
w = tk.Label(root, text = "Make Your Choice", bg="green" , fg = "purple", font=('Times New Roman',18,'bold'))
b1 = tk.Button(root, bg="yellow", text="Random Queue", command=goto_random_queue)
b2 = tk.Button(root, bg="yellow", text=" Create Own ", command=goto_user_queue)
b3 = tk.Button(root, bg="yellow", text="   Quit    ", command=root.quit)
w.grid(row=0, column=1, padx=40, pady=10)
b1.grid(row=1, column=1, sticky=NSEW, padx=50, pady=10)
b2.grid(row=2, column=1, sticky=NSEW, padx=50, pady=10)
b3.grid(row=3, column=1, sticky=NSEW, padx=50 , pady=10)


root.mainloop()
