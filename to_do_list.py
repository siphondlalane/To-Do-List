
import tkinter
import tkinter.messagebox
import pickle


def add_task():
    task = edit.get()

    if task != "":
        listbox.insert(tkinter.END, task)
        edit.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="You must enter a task")


def del_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="You must select a task")

def load_task():
    try:

        tasks = pickle.load(open("tasks.dat","rb"))
        listbox.delete(0, tkinter.END)
        for task in tasks:
            listbox.insert(tkinter.END, task)
    except:
           tkinter.messagebox.showwarning(title="Warning!",message="File not found!!")

def save_task():

    if listbox.size() == 0:
        tkinter.messagebox.showwarning(title="Warning!",message="No tasks found!")
    else:

        tasks = listbox.get(0, listbox.size())
        pickle.dump(tasks, open("tasks.dat","wb"))
        tkinter.messagebox.showinfo("Confirmation","Succesfully Saved")
        listbox.delete(0, listbox.size())


    # Main Function #
if __name__=="__main__":

    root = tkinter.Tk()
    root.title("\t\tTo Do List")

    frame = tkinter.Frame(root)
    frame.pack()

    listbox = tkinter.Listbox(frame, height = 10, width = 50)
    listbox.pack(side=tkinter.LEFT)

    scroll = tkinter.Scrollbar(frame)
    scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    listbox.config(yscrollcommand=scroll.set)
    scroll.config(command=listbox.yview)

    edit = tkinter.Entry(root, width = 50)
    edit.pack()

    btn_add = tkinter.Button(root, text = "Add Tasks",width = 48, command = add_task)
    btn_add.pack()

    btn_delete = tkinter.Button(root, text = "Delete Tasks",width = 48, command = del_task)
    btn_delete.pack()

    btn_load = tkinter.Button(root, text = "Load Tasks",width = 48, command = load_task)
    btn_load.pack()

    btn_save = tkinter.Button(root, text = "Save Tasks",width = 48, command = save_task)
    btn_save.pack()

    root.mainloop()









