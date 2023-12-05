from tkinter import *
from tkinter import ttk

color1 = "#3E4040"
color2 = "#0f43ff"
color3 = "#000000"

janela = Tk()
janela.geometry('235x380')
frame_superior = Frame(janela,width=235,height=50,bg=color1)
frame_superior.grid(row=0, column=0)

frame_corpo = Frame(janela,width = 235, height=350,bg=color3)
frame_corpo.grid(row=1,column = 0)
janela.title('Calculadora')


b_c = Button(frame_corpo,text = 'c',width=12,height=3)
b_c.place(x=-3,y=1)
b_c1 = Button(frame_corpo,text = '%',width = 4,height =3) 
b_c1.place(x=120,y=1)
b_c1 = Button(frame_corpo,text = '/',width = 4,height =3) 
b_c1.place(x=180,y=1)
#segunda linha
b_7 = Button(frame_corpo,text = '7',width=4,height=3)
b_7.place(x=0,y=66)
b_8 = Button(frame_corpo,text = '8',width = 4,height =3) 
b_8.place(x=60,y=66)
b_9 = Button(frame_corpo,text = '9',width = 4,height =3) 
b_9.place(x=120,y=66)
z_2 = Button(frame_corpo,text = '*',width = 4,height =3) 
z_2.place(x=180,y=66)
#terceira linha
b_7 = Button(frame_corpo,text = '4',width=4,height=3)
b_7.place(x=0,y=130)
b_8 = Button(frame_corpo,text = '5',width = 4,height =3) 
b_8.place(x=60,y=130)
b_9 = Button(frame_corpo,text = '6',width = 4,height =3) 
b_9.place(x=120,y=130)
z_2 = Button(frame_corpo,text = '-',width = 4,height =3) 
z_2.place(x=180,y=130)
#quarto linha
b_7 = Button(frame_corpo,text = '1',width=4,height=3)
b_7.place(x=0,y=195)
b_8 = Button(frame_corpo,text = '2',width = 4,height =3) 
b_8.place(x=60,y=195)
b_9 = Button(frame_corpo,text = '3',width = 4,height =3) 
b_9.place(x=120,y=195)
z_2 = Button(frame_corpo,text = '+',width = 4,height =3) 
z_2.place(x=180,y=195)

#quinta linha
b_c = Button(frame_corpo,text = '0',width=12,height=3)
b_c.place(x=-3,y=260)
b_c1 = Button(frame_corpo,text = '.',width = 4,height =3) 
b_c1.place(x=120,y=260)
b_c1 = Button(frame_corpo,text = '=',width = 4,height =3) 
b_c1.place(x=180,y=260)




janela.mainloop()