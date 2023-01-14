from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Warehouse')
root.geometry('500x300')
global nameE, heightEntry, widthEntry, rowEntry, columnEntry
buttonNames=[]
buttonDic = {}
buttonColors = {}
window = Toplevel(root)
window.geometry('500x300')
window.config(bg='#7F7FFF')
bg=PhotoImage(file="C:/Users/amr01/OneDrive/Documents/GitHub/Bachelor/interface/warehouse.png")
my_label = Label(root, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1,)
def area():
    string1=nameE.get()
    string2=heightEntry.get()
    string3=widthEntry.get()
    string4=rowEntry.get()
    string5=columnEntry.get()
    buttonNames.append(string1)        
    def clear():
        list = window.grid_slaves()
        for l in list:
            l.destroy()
    for i,name in enumerate(buttonNames):
        for j,x in enumerate(buttonNames):
            if(name=='Machine' or name=='machine'):
                buttonDic[name] = Button(window, text=name, command=clear, height=string2, width=string3, bg="#FFFF00", bd=0)
            elif(name=='Path' or name=='path'):
                buttonDic[name] = Button(window, text=name, command=clear, height=string2, width=string3, bg="#0A0A0A",bd=0)
            elif(name=='Wall' or name=='wall'):
                buttonDic[name] = Button(window, text=name, command=clear, height=string2, width=string3, bg="#9A9AC0",bd=0) 
    #window.grid(row=string4, column=string5)
    for i,name in enumerate(buttonNames):
        for j,x in enumerate(buttonNames):
            buttonDic[name].grid(row=string4,column=string5)
    buttonNames.remove(string1)
choose_list=["Machine", "Path", "Wall"]
"""l1= Label(root, text='Choose what do you want to add', font=("Courier 12 bold"),bd=0)
l1.grid(columnspan = 2, row=0,column=1)
l1.config()"""
nameLabel = Label(root, text="Name",bd=0,width=15).grid(padx=15, pady=5, row=0, column=0)
nameE = StringVar()
nameE.set("Choose")
nameEntry = OptionMenu(root, nameE, *choose_list)
nameEntry.grid(padx=15, pady=5, row=0, column=1)
nameEntry.config(text="Choose",bd=0)
heightLabel = Label(root, text="Length", bd=0, width=15).grid(padx=15, pady=5, row=1, column=0)
height = IntVar()
heightEntry = Entry(root, textvariable=height, bd=0, width=20)
heightEntry.grid(padx=15, pady=5, row=1, column=1)
widthLabel = Label(root, text="Width",bd=0, width=15).grid(padx=15, pady=5, row=2, column=0)
width = IntVar()
widthEntry = Entry(root, textvariable=width,bd=0, width=20)
widthEntry.grid(padx=15, pady=5, row=2, column=1)
rowLabel = Label(root, text="Row",bd=0, width=15).grid(padx=15, pady=5, row=3, column=0)
row = IntVar()
rowEntry = Entry(root, textvariable=row,bd=0, width=20)
rowEntry.grid(padx=15, pady=5, row=3, column=1)
columnLabel = Label(root, text="Column",bd=0, width=15).grid(padx=15, pady=5, row=4, column=0)
column = IntVar()
columnEntry = Entry(root, textvariable=column,bd=0, width=20)
columnEntry.grid(padx=15, pady=5, row=4, column=1)

Button(root, text='add', width=15, command=area, bg="green", bd=0).grid(padx=15, pady=5, row=6, column=1)
exit_button = Button(root, text="Exit", width=10, command=root.destroy, bg="red", bd=0)
exit_button.grid(padx=15, pady=5, row=7, column=1)
root.mainloop()