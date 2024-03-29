from tkinter import * 

root = Tk()   


def donothing():
    filewin = Toplevel()  # Toplevel(root)
    button = Button(filewin, text='Do nothing button', relief=GROOVE, padx=10, pady=5)
    button.pack()


def _menu():
    menubar = Menu()  # Menu(root)
    # menubar.grid(row=0, column=0, columnspan=3, padx=2, pady=2)

    filemenu = Menu(menubar, tearoff=0)
    editmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0) 

    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Edit', menu=editmenu)
    menubar.add_cascade(label='Help', menu=helpmenu)

    # filemenu.add_command(label='New', command=donothing)
    # filemenu.add_command(label='Open', command=donothing)
    # filemenu.add_command(label='Save', command=donothing)
    # filemenu.add_command(label='Save As...', command=donothing)
    # filemenu.add_command(label='Close', command=donothing)
    # filemenu.add_command(label='Print', command=donothing)
    # filemenu.add_radiobutton(label='radiobutton')
    # filemenu.add_checkbutton(label='checkbutton')
    # filemenu.add_cascade(label='cascade', menu=editmenu)
    # filemenu.add_separator()
    # filemenu.add_command(label='Exit', command=root.quit)

    # editmenu.add_command(label='Undo', command=donothing)
    # editmenu.add_separator()
    # editmenu.add_command(label='Cut', command=donothing)
    # editmenu.add_command(label='Copy', command=donothing)
    # editmenu.add_command(label='Paste', command=donothing)
    # editmenu.add_command(label='Delete', command=donothing)
    # editmenu.add_command(label='Select All', command=donothing)
                    
    # helpmenu.add_command(label='Help Index', command=donothing)
    # helpmenu.add_command(label='About...', command=donothing)
    
    root.config(menu=menubar)

# root.config(menu=menubar)
# root.mainloop()
_menu()
mainloop()           
         