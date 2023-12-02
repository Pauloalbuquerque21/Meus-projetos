from tkinter import *
from tkinter import ttk

color1 = "#d4281c"
color2 = "#0f43ff"

janela = Tk()
janela.geometry('235x318')
frame_superior = Frame(janela,width=235,height=50,bg=color1)
frame_superior.grid(row=0, column=0)

frame_corpo = Frame(janela,width = 235, height=278,bg=color2)
frame_corpo.grid(row=1,column = 0)
janela.title('Calculadora')
b_c = Button(frame_corpo,)
janela.mainloop()