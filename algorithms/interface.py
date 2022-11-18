from tkinter import *

ws = Tk()
ws.title('Warehouse')
ws.geometry('610x200')
ws.config(bg='#BF7C41')


choose_list = ['Machine', 'Path', 'Wall']

def change_color1(choice):
    choice = variable1.get()
    if(choice=='Machine'):
        dropdown1.config(bg="red")
    elif(choice=='Path'):
        dropdown1.config(bg="black")
    elif(choice=='Wall'):
        dropdown1.config(bg="yellow")
variable1 = StringVar()
variable1.set("Choose")
dropdown1 = OptionMenu(ws, variable1, *choose_list, command=change_color1)
dropdown1.grid(pady=5, row=0, column=0)

def change_color2(choice):
    choice = variable2.get()
    if(choice=='Machine'):
        dropdown2.config(bg="red")
    elif(choice=='Path'):
        dropdown2.config(bg="black")
    elif(choice=='Wall'):
        dropdown2.config(bg="yellow")
variable2 = StringVar()
variable2.set("Choose")
dropdown2 = OptionMenu(ws, variable2, *choose_list, command=change_color2)
dropdown2.grid(pady=5, row=0, column=1)

def change_color3(choice):
    choice = variable3.get()
    if(choice=='Machine'):
        dropdown3.config(bg="red")
    elif(choice=='Path'):
        dropdown3.config(bg="black")
    elif(choice=='Wall'):
        dropdown3.config(bg="yellow")
variable3 = StringVar()
variable3.set("Choose")
dropdown3 = OptionMenu(ws, variable3, *choose_list, command=change_color3)
dropdown3.grid(pady=5, row=0, column=2)

def change_color4(choice):
    choice = variable4.get()
    if(choice=='Machine'):
        dropdown4.config(bg="red")
    elif(choice=='Path'):
        dropdown4.config(bg="black")
    elif(choice=='Wall'):
        dropdown4.config(bg="yellow")
variable4 = StringVar()
variable4.set("Choose")
dropdown4 = OptionMenu(ws, variable4, *choose_list, command=change_color4)
dropdown4.grid(pady=5, row=0, column=3)

def change_color5(choice):
    choice = variable5.get()
    if(choice=='Machine'):
        dropdown5.config(bg="red")
    elif(choice=='Path'):
        dropdown5.config(bg="black")
    elif(choice=='Wall'):
        dropdown5.config(bg="yellow")
variable5 = StringVar()
variable5.set("Choose")
dropdown5 = OptionMenu(ws, variable5, *choose_list, command=change_color5)
dropdown5.grid(pady=5, row=0, column=4)

def change_color6(choice):
    choice = variable6.get()
    if(choice=='Machine'):
        dropdown6.config(bg="red")
    elif(choice=='Path'):
        dropdown6.config(bg="black")
    elif(choice=='Wall'):
        dropdown6.config(bg="yellow")
variable6 = StringVar()
variable6.set("Choose")
dropdown6 = OptionMenu(ws, variable6, *choose_list, command=change_color6)
dropdown6.grid(pady=5, row=3, column=3)

def change_color7(choice):
    choice = variable7.get()
    if(choice=='Machine'):
        dropdown7.config(bg="red")
    elif(choice=='Path'):
        dropdown7.config(bg="black")
    elif(choice=='Wall'):
        dropdown7.config(bg="yellow")
variable7 = StringVar()
variable7.set("Choose")
dropdown7 = OptionMenu(ws, variable7, *choose_list, command=change_color7)
dropdown7.grid(pady=5, row=1, column=0)

def change_color8(choice):
    choice = variable8.get()
    if(choice=='Machine'):
        dropdown8.config(bg="red")
    elif(choice=='Path'):
        dropdown8.config(bg="black")
    elif(choice=='Wall'):
        dropdown8.config(bg="yellow")
variable8 = StringVar()
variable8.set("Choose")
dropdown8 = OptionMenu(ws, variable8, *choose_list, command=change_color8)
dropdown8.grid(pady=5, row=1, column=1)

def change_color9(choice):
    choice = variable9.get()
    if(choice=='Machine'):
        dropdown9.config(bg="red")
    elif(choice=='Path'):
        dropdown9.config(bg="black")
    elif(choice=='Wall'):
        dropdown9.config(bg="yellow")
variable9 = StringVar()
variable9.set("Choose")
dropdown9 = OptionMenu(ws, variable9, *choose_list, command=change_color9)
dropdown9.grid(pady=5, row=1, column=2)

def change_color10(choice):
    choice = variable10.get()
    if(choice=='Machine'):
        dropdown10.config(bg="red")
    elif(choice=='Path'):
        dropdown10.config(bg="black")
    elif(choice=='Wall'):
        dropdown10.config(bg="yellow")
variable10 = StringVar()
variable10.set("Choose")
dropdown10 = OptionMenu(ws, variable10, *choose_list, command=change_color10)
dropdown10.grid(pady=5, row=1, column=3)

def change_color11(choice):
    choice = variable11.get()
    if(choice=='Machine'):
        dropdown11.config(bg="red")
    elif(choice=='Path'):
        dropdown11.config(bg="black")
    elif(choice=='Wall'):
        dropdown11.config(bg="yellow")
variable11 = StringVar()
variable11.set("Choose")
dropdown11 = OptionMenu(ws, variable11, *choose_list, command=change_color11)
dropdown11.grid(pady=5, row=1, column=4)

def change_color12(choice):
    choice = variable12.get()
    if(choice=='Machine'):
        dropdown12.config(bg="red")
    elif(choice=='Path'):
        dropdown12.config(bg="black")
    elif(choice=='Wall'):
        dropdown12.config(bg="yellow")
variable12 = StringVar()
variable12.set("Choose")
dropdown12 = OptionMenu(ws, variable12, *choose_list, command=change_color12)
dropdown12.grid(pady=5, row=2, column=0)

def change_color13(choice):
    choice = variable13.get()
    if(choice=='Machine'):
        dropdown13.config(bg="red")
    elif(choice=='Path'):
        dropdown13.config(bg="black")
    elif(choice=='Wall'):
        dropdown13.config(bg="yellow")
variable13 = StringVar()
variable13.set("Choose")
dropdown13 = OptionMenu(ws, variable13, *choose_list, command=change_color13)
dropdown13.grid(pady=5, row=2, column=1)

def change_color14(choice):
    choice = variable14.get()
    if(choice=='Machine'):
        dropdown14.config(bg="red")
    elif(choice=='Path'):
        dropdown14.config(bg="black")
    elif(choice=='Wall'):
        dropdown14.config(bg="yellow")
variable14 = StringVar()
variable14.set("Choose")
dropdown14 = OptionMenu(ws, variable14, *choose_list, command=change_color14)
dropdown14.grid(pady=5, row=2, column=3)

def change_color15(choice):
    choice = variable15.get()
    if(choice=='Machine'):
        dropdown15.config(bg="red")
    elif(choice=='Path'):
        dropdown15.config(bg="black")
    elif(choice=='Wall'):
        dropdown15.config(bg="yellow")
variable15 = StringVar()
variable15.set("Choose")
dropdown15 = OptionMenu(ws, variable15, *choose_list, command=change_color15)
dropdown15.grid(pady=5, row=2, column=4)

def change_color16(choice):
    choice = variable16.get()
    if(choice=='Machine'):
        dropdown16.config(bg="red")
    elif(choice=='Path'):
        dropdown16.config(bg="black")
    elif(choice=='Wall'):
        dropdown16.config(bg="yellow")
variable16 = StringVar()
variable16.set("Choose")
dropdown16 = OptionMenu(ws, variable16, *choose_list, command=change_color16)
dropdown16.grid(pady=5, row=3, column=0)

def change_color17(choice):
    choice = variable17.get()
    if(choice=='Machine'):
        dropdown17.config(bg="red")
    elif(choice=='Path'):
        dropdown17.config(bg="black")
    elif(choice=='Wall'):
        dropdown17.config(bg="yellow")
variable17 = StringVar()
variable17.set("Choose")
dropdown17 = OptionMenu(ws, variable17, *choose_list, command=change_color17)
dropdown17.grid(pady=5, row=3, column=1)

def change_color18(choice):
    choice = variable18.get()
    if(choice=='Machine'):
        dropdown18.config(bg="red")
    elif(choice=='Path'):
        dropdown18.config(bg="black")
    elif(choice=='Wall'):
        dropdown18.config(bg="yellow")
variable18 = StringVar()
variable18.set("Choose")
dropdown18 = OptionMenu(ws, variable18, *choose_list, command=change_color18)
dropdown18.grid(pady=5, row=3, column=2)

def change_color19(choice):
    choice = variable19.get()
    if(choice=='Machine'):
        dropdown19.config(bg="red")
    elif(choice=='Path'):
        dropdown19.config(bg="black")
    elif(choice=='Wall'):
        dropdown19.config(bg="yellow")
variable19 = StringVar()
variable19.set("Choose")
dropdown19 = OptionMenu(ws, variable19, *choose_list, command=change_color19)
dropdown19.grid(pady=5, row=2, column=2)

def change_color20(choice):
    choice = variable20.get()
    if(choice=='Machine'):
        dropdown20.config(bg="red")
    elif(choice=='Path'):
        dropdown20.config(bg="black")
    elif(choice=='Wall'):
        dropdown20.config(bg="yellow")
variable20 = StringVar()
variable20.set("Choose")
dropdown20 = OptionMenu(ws, variable20, *choose_list, command=change_color20)
dropdown20.grid(pady=5, row=3, column=4)

def change_color21(choice):
    choice = variable21.get()
    if(choice=='Machine'):
        dropdown21.config(bg="red")
    elif(choice=='Path'):
        dropdown21.config(bg="black")
    elif(choice=='Wall'):
        dropdown21.config(bg="yellow")
variable21 = StringVar()
variable21.set("Choose")
dropdown21 = OptionMenu(ws, variable21, *choose_list, command=change_color21)
dropdown21.grid(pady=5, row=4, column=0)

def change_color22(choice):
    choice = variable22.get()
    if(choice=='Machine'):
        dropdown22.config(bg="red")
    elif(choice=='Path'):
        dropdown22.config(bg="black")
    elif(choice=='Wall'):
        dropdown22.config(bg="yellow")
variable22 = StringVar()
variable22.set("Choose")
dropdown22 = OptionMenu(ws, variable22, *choose_list, command=change_color22)
dropdown22.grid(pady=5, row=4, column=1)

def change_color23(choice):
    choice = variable23.get()
    if(choice=='Machine'):
        dropdown23.config(bg="red")
    elif(choice=='Path'):
        dropdown23.config(bg="black")
    elif(choice=='Wall'):
        dropdown23.config(bg="yellow")
variable23 = StringVar()
variable23.set("Choose")
dropdown23 = OptionMenu(ws, variable23, *choose_list, command=change_color23)
dropdown23.grid(pady=5, row=4, column=2)

def change_color24(choice):
    choice = variable24.get()
    if(choice=='Machine'):
        dropdown24.config(bg="red")
    elif(choice=='Path'):
        dropdown24.config(bg="black")
    elif(choice=='Wall'):
        dropdown24.config(bg="yellow")
variable24 = StringVar()
variable24.set("Choose")
dropdown24 = OptionMenu(ws, variable24, *choose_list, command=change_color24)
dropdown24.grid(pady=5, row=4, column=3)

def change_color25(choice):
    choice = variable25.get()
    if(choice=='Machine'):
        dropdown25.config(bg="red")
    elif(choice=='Path'):
        dropdown25.config(bg="black")
    elif(choice=='Wall'):
        dropdown25.config(bg="yellow")
variable25 = StringVar()
variable25.set("Choose")
dropdown25 = OptionMenu(ws, variable25, *choose_list, command=change_color25)
dropdown25.grid(pady=5, row=4, column=4)

l1 = Label(ws, text = "Machines are in Red")
l1.config(bg="red", font =("Courier", 11))
l1.grid(padx=5,row=1, column=5)

l2 = Label(ws, text = "Path in Black")
l2.config(bg="white", font =("Courier", 11))
l2.grid(padx=5,row=2, column=5)

l3 = Label(ws, text = "Wall in Yellow")
l3.config(bg="yellow", font =("Courier", 11))
l3.grid(padx=5,row=3, column=5)

l4 = Label(ws, text = "<----------")
l4.config(bg="#BF7C41", font =("Courier", 14))
l4.grid(padx=5,row=0, column=5)

l4 = Label(ws, text = "<----------")
l4.config(bg="#BF7C41", font =("Courier", 14))
l4.grid(padx=5,row=4, column=5)



# infinite loop 
ws.mainloop()