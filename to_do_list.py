
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("\t\tTo Do List")


def add_task():
    task = edit.get()
    listbox.insert(tkinter.END, task)

listbox = tkinter.Listbox(root, height = 15, width = 50)
listbox.pack()

edit = tkinter.Entry(root, width = 50)
edit.pack()

button_add = tkinter.Button(root, text = "Add Task",width = 48, command = add_task)
button_add.pack()

root.mainloop()
##




