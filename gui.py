import tkinter as tk
import random
from algorithms.fcfs import fcfs
from algorithms.sjf_non_pre import sjf_non_pre
from algorithms.sjf_pre import sjf_pre
from tkinter import messagebox
root = tk.Tk()
root.title("Interactive CPU Scheduler")
size = "1150x500"
root.geometry(size)

def algo(window, algorithm, queue):
    if algorithm == "fcfs":
        output = fcfs(queue)
    elif algorithm == "sjf_non_pre":
        output = sjf_non_pre(queue)
    elif algorithm == "sjf_pre":
        output = sjf_pre(queue)
    wait_time = output[0]
    response_time = output[1]
    turnaround_time = output[2]
    throughput = output[3]
    out = f"Input Queue: {queue}\n\n\nAverage Waiting Time: {round(wait_time,2)}\n\nAverage Response Time: {round(response_time,2)}\n\nAverage Turnaround Time: {round(turnaround_time,2)}\n\nThroughput: {round(throughput,2)}"
    label = tk.Label(window, text=out, justify="left").grid(row=20, column=1)

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
        ("fcfs"),
        ("sjf_non_pre"),
        ("sjf_pre"),
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
    second.geometry(size)
    def generate_random_queue(length):
            queue = []
            choices = list(range(0,10))
            row1 = 2
            random.shuffle(choices)
            for i in range(length):
                pid = choices.pop()
                burst_time = random.randint(0, 20)
                arr_time = random.randint(0, 20)
                m1 = tk.Label(second, text=pid, font=("Verdana", 15, "bold"))
                m2 = tk.Label(second, text=burst_time, font=("Verdana", 15, "bold"))
                m3 = tk.Label(second, text=arr_time, font=("Verdana", 15, "bold"))
                m1.grid(row=row1, column=0)
                m2.grid(row=row1, column=1)
                m3.grid(row=row1, column=2)
                row1+=1;
                queue.append((pid, burst_time, arr_time))
            return queue
    random_queue = generate_random_queue(length = 6)
    v = tk.Label(second, text="Your Queue is:", font=("New Times Roman", 25, "bold"))
    value1 = tk.Label(second, text="Process ID", font=("Verdana", 15, "bold")).grid(row=1, column=0, )
    value2 = tk.Label(second, text="Burst Time", font=("Verdana", 15, "bold")).grid(row=1, column=1)
    value3 = tk.Label(second, text="Arrival Time", font=("Verdana", 15, "bold")).grid(row=1, column=2)
    b1 = tk.Button(second, text="Go to Main", height=2, width=12, command=lambda: goto_main(second))
    b2 = tk.Button(second, text="Submit", height=2, width=12, command=lambda: goto_submission(second, random_queue))
    v.grid(row=0, column=0, pady=40, padx=250, columnspan=3)
    b1.grid(row=8, column=0, sticky=tk.NSEW, padx=200, pady=70)
    b2.grid(row=8, column=2, sticky=tk.NSEW, padx=200, pady=70)

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
    lab1 = tk.Label(second, text="Process ID:", font=("New Times Roman", 20, "bold"))
    lab2 = tk.Label(second, text="Burst Time:", font=("New Times Roman", 20, "bold"))
    lab3 = tk.Label(second, text="Arrival Time:", font=("New Times Roman", 20, "bold"))
    lab4 = tk.Label(second, text="Process ID", font=("New Times Roman", 10, "bold"))
    lab5 = tk.Label(second, text="Burst Time", font=("New Times Roman", 10, "bold"))
    lab6 = tk.Label(second, text="Arrival Time", font=("New Times Roman", 10, "bold"))
    e1.grid(row=1, column=0, padx=120, pady=10, ipady=4, ipadx=2)
    e2.grid(row=1, column=1, padx=100, pady=10, ipady=4, ipadx=2)
    e3.grid(row=1, column=2, padx=120, pady=10, ipady=4, ipadx=2)
    lab1.grid(row=0, column=0, padx=30, pady=30)
    lab2.grid(row=0, column=1, padx=20, pady=30)
    lab3.grid(row=0, column=2, padx=30, pady=30)
    lab4.grid(row=3, column=0, padx=30, pady=20)
    lab5.grid(row=3, column=1, padx=20, pady=20)
    lab6.grid(row=3, column=2, padx=30, pady=20)
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
        row1 = give_row()
        value1 = tk.Label(second, text = pid, font=("Verdana", 15, "bold")).grid(row=row1, column=0,)
        value2 = tk.Label(second, text=burst_time, font=("Verdana", 15, "bold")).grid(row=row1, column=1)
        value3 = tk.Label(second, text=arr_time, font=("Verdana", 15, "bold")).grid(row=row1, column=2)
        queue.append(user_process)
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    b1 = tk.Button(second, text="Go to Main", height=2, command=lambda:goto_main(second))
    b2 = tk.Button(second, text="Add Process",height=2,  command=add_process)
    b3 = tk.Button(second, text="Submit",height=2, command=lambda:goto_submission(second, queue))

    b1.grid(row=2, column=0, padx=50, pady=50, sticky=tk.NSEW)
    b2.grid(row=2, column=1, padx=50, pady=50, sticky=tk.NSEW)
    b3.grid(row=2, column=2, padx=50, pady=50, sticky=tk.NSEW)
w = tk.Label(root, text = "Make Your Choice", font=('Times New Roman',25,'bold'))
b1 = tk.Button(root, text="Random Queue", height=3, command=goto_random_queue)
b2 = tk.Button(root, text="Create Own", height=3, command=goto_user_queue)
b3 = tk.Button(root, text="Quit", height=3, command=root.quit)
w.grid(row=0, column=1, padx=425, pady=100, columnspan=3)
b1.grid(row=1, column=1, sticky=tk.NSEW, padx=40, pady=30)
b2.grid(row=1, column=2, sticky=tk.NSEW, padx=40, pady=30)
b3.grid(row=1, column=3, sticky=tk.NSEW, padx=40, pady=30)

root.mainloop()
