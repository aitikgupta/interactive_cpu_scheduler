import tkinter as tk
import random
from sample import sample_function
from algorithms.fcfs import fcfs
from algorithms.sjf_non_pre import sjf_non_pre
from algorithms.sjf_pre import sjf_pre
from algorithms.round_robin import round_robin
from algorithms.priority_non_pre import priority_non_pre
from algorithms.priority_queue_pre import priority_queue_pre
from algorithms.multi_level_feedback import multi_level_feedback
from algorithms.default_algorithm import default_algorithm
from algorithms.multi_level import multi_level
from tkinter import messagebox
import webbrowser

root = tk.Tk()
root.title("Interactive CPU Scheduler")
size = "1150x500"
size_out = "600x200"
root.geometry(size)

def algo(window, algorithm, queue, extra):
    def show_output(algorithm, output, default_output):
        def ret():
            top_out.grid_forget()
            top_def.grid_forget()
            label.grid_forget()
            def_label.grid_forget()
            button.grid_forget()
            output_win.destroy()
            
        output_win = tk.Toplevel()
        output_win.geometry(size)
        button = tk.Button(output_win, text="Go Back", command=ret, height=2, width=14)

        wait_time = output[0]
        response_time = output[1]
        turnaround_time = output[2]
        throughput = output[3]
        def_wait_time = default_output[0]
        def_response_time = default_output[1]
        def_turnaround_time = default_output[2]
        def_throughput = default_output[3]
        out = f"Average Waiting Time: {round(wait_time,2)}\n\nAverage Response Time: {round(response_time,2)}\n\nAverage Turnaround Time: {round(turnaround_time,2)}\n\nThroughput: {round(throughput,2)}"
        default_out = f"Average Waiting Time: {round(def_wait_time,2)}\n\nAverage Response Time: {round(def_response_time,2)}\n\nAverage Turnaround Time: {round(def_turnaround_time,2)}\n\nThroughput: {round(def_throughput,2)}"
        label = tk.Label(output_win, text=out, justify="left", font=("Times New Roman", 12, "normal"))
        def_label = tk.Label(output_win, text=default_out, justify="left", font=("Times New Roman", 12, "normal"))
        top_out = tk.Label(output_win, text=f"Selected Algorithm\n({algorithm})", font=("Times New Roman", 15, "normal"))
        top_def = tk.Label(output_win, text="Default Algorithm", font=("Times New Roman", 15, "normal"))
        t1 = tk.Label(output_win, text="Process ID", font=("Times New Roman", 15, "normal"))
        t2 = tk.Label(output_win, text="Burst Time", font=("Times New Roman", 15, "normal"))
        t3 = tk.Label(output_win, text="Arrival Time", font=("Times New Roman", 15, "normal"))
        tk.Label(output_win, text="  ").grid(row=0, column=0, padx=60)
        t1.grid(row=0, column=1, padx=60, pady=20)
        t2.grid(row=0, column=2, pady=20)
        t3.grid(row=0, column=3, padx=60, pady=20)
        pri = [process[0] for process in queue]
        burst = [process[1] for process in queue]
        arriv = [process[2] for process in queue]
        for i in range(len(pri)):
            tk.Label(output_win, text=pri[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=1)
            tk.Label(output_win, text=burst[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=2)
            tk.Label(output_win, text=arriv[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=3)
        top_out.grid(row=10, column=1, padx=60, pady=10)
        top_def.grid(row=10, column=3, padx=60)
        label.grid(row=11, column=1, padx=60)
        def_label.grid(row=11, column=3, padx=60)
        button.grid(row=12, column=2, sticky=tk.NSEW)
    if algorithm == "First Come First Serve":
        output = fcfs(queue)
    elif algorithm == "Shortest Job First Non Preemption":
        output = sjf_non_pre(queue)
    elif algorithm == "Shortest Remaining Time First":
        output = sjf_pre(queue)
    elif algorithm == "Round Robin":
        value = extra.get()
        output = round_robin(queue, value)
    elif algorithm == "Non Preemption Priority Queue":
        priorities = []
        for idx in extra:
            try:
                value = int(idx.get())
            except:
                messagebox.showerror("Invalid priorities found!", "One or more priorities are not integer.")
                return
            if not value:
                messagebox.showerror("Invalid priorities found!", "One or more priorities are blank.")
                return
            priorities.append(value)
        # if sorted(priorities) != sorted(list(set(priorities))):
        #     messagebox.showerror("Invalid priorities found!", "One or more priorities are not unique.")
        #     return
        output = priority_non_pre(queue, priorities)
    elif algorithm == "Preemption Priority Queue":
        priorities = []
        for idx in extra:
            try:
                value = int(idx.get())
            except:
                messagebox.showerror("Invalid priorities found!", "One or more priorities are not integer.")
                return
            if not value:
                messagebox.showerror("Invalid priorities found!", "One or more priorities are blank.")
                return
            priorities.append(value)
        # if sorted(priorities) != sorted(list(set(priorities))):
        #     messagebox.showerror("Invalid priorities found!", "One or more priorities are not unique.")
        #     return
        output = priority_queue_pre(queue, priorities)
    elif algorithm == "Multi Level Queue":
        pids = [inp[0] for inp in queue]
        multi_level_algorithms = [algori.get() for algori in extra[0]]
        processes = []
        for prid in extra[1]:
            level_wise_processes = []
            try:
                idx = [int(i) for i in prid.get().strip().split(",")]
            except:
                messagebox.showerror("Invalid Process ID(s) found!", "One or more process IDs are blank.")
                return
            for j in idx:
                if j not in pids:
                    messagebox.showerror("Invalid Process ID(s) found!", "One or more process IDs do not exist in input process IDs.")
                    return
                for proc in queue:
                    if proc[0] == j:
                        level_wise_processes.append(proc)
            processes.append(level_wise_processes)
        output = multi_level(multi_level_algorithms, processes)
    elif algorithm == "Multi Level Feedback Queue":
        threshold = extra[1].get()
        if not threshold or int(threshold) > 5 or int(threshold) < 1:
            messagebox.showerror("Invalid thresold found!", "Threshold should be an integer in range (1-5), and can not be empty.")
            return
        threshold = int(threshold)
        multi_level_algorithms = [algori.get() for algori in extra[0]]
        quantums = [al[-1] for al in multi_level_algorithms if al[0] == "R"]
        quantums = list(map(int, quantums))
        if quantums != sorted(quantums):
            messagebox.showerror("Invalid time quantums found!", "Time Quantums should be in increasing order level-wise.")
            return
        output = multi_level_feedback(queue, multi_level_algorithms, threshold)
    elif algorithm == "Default Algorithm":
        output = default_algorithm(queue)
    else:
        messagebox.showerror("Select Algorithm First!", "Click on Select Algorithm button before submitting.")
        return
    default_output = default_algorithm(queue)
    show_output(algorithm, output, default_output)


def goto_submission(second, queue):
    global submit
    global extra
    submit = None
    extra = None
    third = tk.Toplevel()
    second.withdraw()
    third.geometry(size)
    ids = [pri[0] for pri in queue]
    ids_stat = tk.Label(third, text=f"Process IDs: {ids}", relief=tk.SUNKEN, bd=2)
    sl = tk.Scale(third, from_=1, to=7, orient=tk.HORIZONTAL)
    pr = [process[0] for process in queue]
    pr_pris = [0 for i in pr]
    pr_idx = [0 for i in pr]    
    pr_title = tk.Label(third, text="Process ID:")
    pris_title = tk.Label(third, text="Priorities:")
    time_quantum = tk.Label(third, text="Time Quantum")
    feedback_label = tk.Label(third, text="Threshold (integer in range 1-5):")
    feedback_threshold = tk.Entry(third)
    for i in range(len(pr)):
        pr_idx[i] = tk.Label(third, text=pr[i])
        pr_pris[i] = tk.Entry(third)

    multi_algos = [[
        ("Round Robin with Time Quantum: 2"),
        ("Round Robin with Time Quantum: 3"),
        ("Round Robin with Time Quantum: 4"),
        ("Round Robin with Time Quantum: 5"),
        ("Round Robin with Time Quantum: 6"),
        ("Round Robin with Time Quantum: 7"),
        ("Round Robin with Time Quantum: 8")
    ],[
        ("Round Robin with Time Quantum: 2"),
        ("Round Robin with Time Quantum: 3"),
        ("Round Robin with Time Quantum: 4"),
        ("Round Robin with Time Quantum: 5"),
        ("Round Robin with Time Quantum: 6"),
        ("Round Robin with Time Quantum: 7"),
        ("Round Robin with Time Quantum: 8")
    ], [
        ("First Come First Serve")
    ]]
        

    multi_level_algo_labels = []
    multi_level_algo_menus = []
    multi_level_algorithms = []
    multi_level_pr_labels = []
    multi_level_processes = []
    for level in range(3):
        multi_level_algo_labels.append(tk.Label(third, text=f"Level {level+1} Algorithm:"))  
        multi_level_pr_labels.append(tk.Label(third, text=f"Process IDs for {level+1} Level (separated by ','): "))
        multi_level_algorithms.append(tk.StringVar())
        multi_level_algorithms[level].set(multi_algos[level][0])
        multi_level_algo_menus.append(tk.OptionMenu(third, multi_level_algorithms[level], *multi_algos[level]))
        multi_level_processes.append(tk.Entry(third))

    def select_algo(algorithm):
        global submit
        global extra
        extra = None
        lab.config(text=op.get())
        def clear():
            sl.grid_forget()
            feedback_threshold.grid_forget()
            feedback_label.grid_forget()
            time_quantum.grid_forget()
            pr_title.grid_forget()
            pris_title.grid_forget()
            for i in range(len(pr)):
                pr_idx[i].grid_forget()
                pr_pris[i].grid_forget()
            for level in range(3):
                    multi_level_algo_labels[level].grid_forget()
                    multi_level_algo_menus[level].grid_forget()
                    multi_level_pr_labels[level].grid_forget()
                    multi_level_processes[level].grid_forget()
        clear()
        if algorithm == "Round Robin":
            sl.grid(row=20, column=1)
            extra = sl
            time_quantum.grid(row=21, column=1)
        elif algorithm == "Non Preemption Priority Queue" or algorithm == "Preemption Priority Queue":
            pr_title.grid(row=19, column=0)
            pris_title.grid(row=19, column=2)
            for i in range(len(pr)):
                pr_pris[i].delete(0, tk.END)
                pr_idx[i].grid(row=20+i, column=0)
                pr_pris[i].grid(row=20+i, column=2)
            extra = pr_pris
        elif algorithm == "Multi Level Queue":
            for level in range(3):
                    multi_level_algo_labels[level].grid(row=20+level, column=0)
                    multi_level_algo_menus[level].grid(row=20+level, column=2)
                    multi_level_algo_menus[level].config(height=1, width=40)
                    multi_level_pr_labels[level].grid(row=23+level, column=0)
                    multi_level_processes[level].grid(row=23+level, column=2)
            extra = [multi_level_algorithms, multi_level_processes]
        elif algorithm == "Multi Level Feedback Queue":
            for level in range(3):
                    multi_level_algo_labels[level].grid(row=20+level, column=0)
                    multi_level_algo_menus[level].grid(row=20+level, column=2)
                    multi_level_algo_menus[level].config(height=1, width=40)
            feedback_label.grid(row=23, column=0)
            feedback_threshold.grid(row=23, column=2)
            extra = [multi_level_algorithms, feedback_threshold]
        submit = algorithm
    lab = tk.Label(third)
    modes = [
        ("Default Algorithm"),
        ("First Come First Serve"),
        ("Shortest Job First Non Preemption"),
        ("Shortest Remaining Time First"),
        ("Round Robin"),
        ("Non Preemption Priority Queue"),
        ("Preemption Priority Queue"),
        ("Multi Level Queue"),
        ("Multi Level Feedback Queue")
    ]
    op = tk.StringVar()
    op.set("Default Algorithm")
    option = tk.OptionMenu(third, op, *modes)
    b = tk.Button(third, text="Select Algorithm", height=2, width=30, command=lambda: select_algo(op.get()))
    b1 = tk.Button(third, text="Go to Main", height=2, width=30, command=lambda:goto_main(third))
    b2 = tk.Button(third, text="Submit for Processing", height=2, width=30, command=lambda:algo(third, submit, queue, extra))
    option.config(height=1, width=30)
    option.grid(row=1, column=1, padx=60, pady=40)
    b.grid(row=2, column=1, padx=60, pady=30, sticky=tk.NSEW)
    b1.grid(row=2, column=0, padx=70, pady=30, sticky=tk.NSEW)
    b2.grid(row=2, column=2, padx=70, pady=30, sticky=tk.NSEW)
    lab.grid(row=3, column=1)
    ids_stat.grid(row=0, column=0, columnspan=3, padx=90, sticky=tk.W+tk.E)

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
                burst_time = random.randint(1, 20)
                arr_time = random.randint(0, 20)
                m1 = tk.Label(second, text=pid, font=("Times New Roman", 18, "normal"))
                m2 = tk.Label(second, text=burst_time, font=("Times New Roman", 18, "normal"))
                m3 = tk.Label(second, text=arr_time, font=("Times New Roman", 18, "normal"))
                m1.grid(row=row1, column=0)
                m2.grid(row=row1, column=1)
                m3.grid(row=row1, column=2)
                row1+=1
                queue.append((pid, burst_time, arr_time))
            return queue
    random_queue = generate_random_queue(length=6)
    v = tk.Label(second, text="Your Queue is:", font=("New Times Roman", 25, "normal"))
    value1 = tk.Label(second, text="Process ID", font=("Times New Roman", 15, "normal")).grid(row=1, column=0)
    value2 = tk.Label(second, text="Burst Time", font=("Times New Roman", 15, "normal")).grid(row=1, column=1)
    value3 = tk.Label(second, text="Arrival Time", font=("Times New Roman", 15, "normal")).grid(row=1, column=2)
    b1 = tk.Button(second, text="Go to Main", height=2, width=18, command=lambda: goto_main(second))
    b2 = tk.Button(second, text="Submit", height=2, width=18, command=lambda: goto_submission(second, random_queue))
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
    lab1 = tk.Label(second, text="Process ID:", font=("New Times Roman", 20, "normal"))
    lab2 = tk.Label(second, text="Burst Time:", font=("New Times Roman", 20, "normal"))
    lab3 = tk.Label(second, text="Arrival Time:", font=("New Times Roman", 20, "normal"))

    e1.grid(row=1, column=0, padx=115, pady=10, ipady=4, ipadx=2)
    e2.grid(row=1, column=1, padx=115, pady=10, ipady=4, ipadx=2)
    e3.grid(row=1, column=2, padx=115, pady=10, ipady=4, ipadx=2)
    lab1.grid(row=0, column=0, padx=30, pady=30)
    lab2.grid(row=0, column=1, padx=20, pady=30)
    lab3.grid(row=0, column=2, padx=30, pady=30)

    global row
    row = 30
    global count
    count = 0
    queue = []
    def give_row():
        global row
        row += 1
        return row
    def add_process():
        global count
        count += 1
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
        if count == 1:
            lab4 = tk.Label(second, text="Process ID", font=("New Times Roman", 10, "normal"))
            lab5 = tk.Label(second, text="Burst Time", font=("New Times Roman", 10, "normal"))
            lab6 = tk.Label(second, text="Arrival Time", font=("New Times Roman", 10, "normal"))
            lab4.grid(row=3, column=0, padx=30, pady=10)
            lab5.grid(row=3, column=1, padx=20, pady=10)
            lab6.grid(row=3, column=2, padx=30, pady=10)
        value1 = tk.Label(second, text = pid, font=("Times New Roman", 15, "normal")).grid(row=row1, column=0,)
        value2 = tk.Label(second, text=burst_time, font=("Times New Roman", 15, "normal")).grid(row=row1, column=1)
        value3 = tk.Label(second, text=arr_time, font=("Times New Roman", 15, "normal")).grid(row=row1, column=2)
        queue.append(user_process)
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    count=0
    b1 = tk.Button(second, text="Go to Main", height=2, command=lambda:goto_main(second))
    b2 = tk.Button(second, text="Add Process", height=2,  command=add_process)
    b3 = tk.Button(second, text="Submit", height=2, command=lambda:goto_submission(second, queue))
    b1.grid(row=2, column=0, padx=50, pady=50, sticky=tk.NSEW)
    b2.grid(row=2, column=1, padx=50, pady=50, sticky=tk.NSEW)
    b3.grid(row=2, column=2, padx=50, pady=50, sticky=tk.NSEW)

def goto_about():
    about = tk.Toplevel()
    about.geometry(size_out)
    root.withdraw()
    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))
    contact0 = "Aadit Agarwal"
    contact1 = "Aashish B Khatri"
    contact2 = "Abhishek Jindal"
    contact3 = "Aitik Gupta"
    contact4 = "Himanshu Ruhela"
    contact5 = "Madhavik Agarwal"

    cnt0 = tk.Label(about, text=contact0)
    cnt1 = tk.Label(about, text=contact1)
    cnt2 = tk.Label(about, text=contact2)
    cnt3 = tk.Label(about, text=contact3)
    cnt4 = tk.Label(about, text=contact4)
    cnt5 = tk.Label(about, text=contact5)

    lbl0 = tk.Label(about, text=r"agarwal.aadit99@gmail.com", fg="blue", cursor="hand2", anchor="e")
    lbl1 = tk.Label(about, text=r"agarwal.aadit99@gmail.com", fg="blue", cursor="hand2", anchor="e")
    lbl2 = tk.Label(about, text=r"agarwal.aadit99@gmail.com", fg="blue", cursor="hand2", anchor="e")
    lbl3 = tk.Label(about, text=r"aitikgupta@gmail.com", fg="blue", cursor="hand2", anchor="e")
    lbl4 = tk.Label(about, text=r"agarwal.aadit99@gmail.com", fg="blue", cursor="hand2", anchor="e")
    lbl5 = tk.Label(about, text=r"agarwal.aadit99@gmail.com", fg="blue", cursor="hand2", anchor="e")
    
    lbl0.bind("<Button-1>", callback)
    lbl1.bind("<Button-1>", callback)
    lbl2.bind("<Button-1>", callback)
    lbl3.bind("<Button-1>", callback)
    lbl4.bind("<Button-1>", callback)
    lbl5.bind("<Button-1>", callback)
    
    cnt0.grid(row=0, column=0)
    cnt1.grid(row=1, column=0)
    cnt2.grid(row=2, column=0)
    cnt3.grid(row=3, column=0)
    cnt4.grid(row=4, column=0)
    cnt5.grid(row=5, column=0)

    lbl0.grid(row=0, column=1)
    lbl1.grid(row=1, column=1)
    lbl2.grid(row=2, column=1)
    lbl3.grid(row=3, column=1)
    lbl4.grid(row=4, column=1)
    lbl5.grid(row=5, column=1)
    
    b1 = tk.Button(about, text="Go to Main", height=2, command=lambda:goto_main(about)).grid(row=6, column=0, columnspan=2)

w = tk.Label(root, text = "Welcome to our project.\nChoose:", font=('Times New Roman',25,'normal'))
b1 = tk.Button(root, text="Random Queue Generation", height=3, command=goto_random_queue)
b2 = tk.Button(root, text="User-Created Queue Generation", height=3, command=goto_user_queue)
b3 = tk.Button(root, text="Quit", height=3, command=root.quit)
b4 = tk.Button(root, text="What am I looking at?", height=3, command=goto_about)
w.grid(row=0, column=1, padx=425, pady=100, columnspan=3)
b1.grid(row=1, column=1, sticky=tk.NSEW, padx=40, pady=30)
b2.grid(row=1, column=2, sticky=tk.NSEW, padx=40, pady=30)
b3.grid(row=1, column=3, sticky=tk.NSEW, padx=40, pady=30)
b4.grid(row=2, column=2, sticky=tk.NSEW, padx=40, pady=30)
root.mainloop()
