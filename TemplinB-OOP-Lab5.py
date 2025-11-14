import tkinter as tk
from tkinter import *

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        x = text_Box.get(1.0, "end-1c")
        self.element.append(x)
        text_Box.delete(1.0, END)

    def dequeue(self):
        self.element.pop(0)

    def displayQueue(self):
        text_Box.insert(tk.INSERT, "(FIFO) Element in Stack:")
        for i in self.element:
            text_Box.insert(tk.INSERT, f"\n{i}")

class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append((text_Box.get(1.0, "end-1c")))
        text_Box.delete(1.0, END)

    def pop(self):
        print("Removing:", self.element[-1])
        self.element.pop()

    def displayStack(self):
        text_Box.insert(tk.INSERT, "(LIFO) Element in Stack:")
        for i in self.element:
            text_Box.insert(tk.INSERT, f"\n{i}")

class Commands:
    def __init__(self):
        self.one = 1

    def clear(self):
        text_Box.delete(1.0, END)

    def backspace(self):
        current_text = text_Box.get("1.0", "end-1c")
        text_Box.delete(1.0, END)
        text_Box.insert("1.0", current_text[:-1])

c = Commands()
q1 = Queue()
q2 = Queue()
s1 = Stack()
s2 = Stack()

top = Tk()
top.geometry("500x500")

top.configure(bg="#1e1e1e")

text_Box = tk.Text(top, bg="#2d2d2d", fg="#ffffff", insertbackground="white", highlightthickness=1, highlightbackground="#3c3c3c", highlightcolor="#5a5a5a")
text_Box.place(x=50, y=50, width=400, height=100)

# Queue
B_enqueue = Button(top, text="Add to Queue", command=lambda: q1.enqueue(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_enqueue.place(x=252.5, y=155, width=197.5, height=50)

B_dequeue = Button(top, text="Remove from Queue", command=lambda: q1.dequeue(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_dequeue.place(x=252.5, y=210, width=197.5, height=50)

B_display = Button(top, text="Display Queue", command=lambda: q1.displayQueue(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_display.place(x=252.5, y=265, width=197.5, height=50)

# Stack
B_push = Button(top, text="Add to Stack", command=lambda: s1.push(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_push.place(x=50, y=155, width=197.5, height=50)

B_pop = Button(top, text="Remove from Stack", command=lambda: s1.pop(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_pop.place(x=50, y=210, width=197.5, height=50)

B_display = Button(top, text="Display Stack", command=lambda: s1.displayStack(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_display.place(x=50, y=265, width=197.5, height=50)

B_Clear = Button(top, text="Clear", command=lambda: c.clear(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_Clear.place(x=50, y=320, width=400, height=50)

B_Back = Button(top, text="Back", command=lambda: c.backspace(), bg="#2d2d2d", fg="#ffffff", activebackground="#3c3c3c", activeforeground="#00ffcc", borderwidth=1)
B_Back.place(x=50, y=375, width=400, height=50)

top.mainloop()