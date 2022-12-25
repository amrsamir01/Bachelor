from tkinter import *

root = Tk()

text = [[None]*3]*3
buttons = [[None]*3]*3

def action(i, j):
    text[i][j].set('Clicked')

for i in range(3):
    for j in range(3):
        text[i][j] = StringVar()
        text[i][j].set('(%d, %d)' % (i,j))
        buttons[i][j] = Button(root, command = lambda i=i, j=j : action(i, j))
        buttons[i][j].config(textvariable = text[i][j], width = 9, height = 5)
        buttons[i][j].grid(row = i, column = j)

root.mainloop()