from tkinter import *
from tkinter import ttk

color1 = "#3b3b3b"  #black/preta
color2 = "#feffff"  #white
color3 = "#38576b"  #azul
color4 = "#ECEFF1" #cizenta
color5 = "#FFAB40" #orange/

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg = color1)
# criando frames
frame_superior = Frame(janela,width=235,height=50,bg=color3)
frame_superior.grid(row=0, column=0)

frame_corpo = Frame(janela,width = 235, height=268)
frame_corpo.grid(row=1,column = 0)

#criação label

app_label = Label(frame_superior, text='123456789', width=16,height = 2,padx=-100, relief = FLAT, anchor = 'e', justify = RIGHT, font = ('ivy 18 bold'), bg = color3,fg=color2)
app_label.place(x=0,y=0)




#criando botões
b_c = Button(frame_corpo,text = 'c',width=11,height=2,bg = color4,font=('Ivy 13 bold'),relief = RAISED, overrelief = RIDGE)
b_c.place(x=0,y=0)
b_c1 = Button(frame_corpo,text = '%',width = 5,height =2,bg = color4,font=('Ivy 13 bold'),relief = RAISED, overrelief = RIDGE) 
b_c1.place(x=118,y=0)
b_c1 = Button(frame_corpo,text = '/',width = 5,bg = color5,height =2,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_c1.place(x=177,y=0)
#segunda linha
b_7 = Button(frame_corpo,text = '7',width=5,height=2,bg = color4,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_7.place(x=0,y=52)
b_8 = Button(frame_corpo,text = '8',width = 5,height =2,bg = color4,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_8.place(x=59,y=52)
b_9 = Button(frame_corpo,text = '9',width = 5,height =2,bg = color4,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_9.place(x=118,y=52)
z_2 = Button(frame_corpo,text = '*',width = 5,height =2, bg = color5,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
z_2.place(x=177,y=52)
#terceira linha
b_7 = Button(frame_corpo,text = '4',width=5,height=2,bg = color4,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_7.place(x=0,y=104)
b_8 = Button(frame_corpo,text = '5',width = 5,height =2,bg = color4,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_8.place(x=59,y=104)
b_9 = Button(frame_corpo,text = '6',width = 5,height =2,bg = color4,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_9.place(x=118,y=104)
z_2 = Button(frame_corpo,text = '-',width = 5,height =2, bg = color5,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
z_2.place(x=177,y=104)
#quarto linha
b_7 = Button(frame_corpo,text = '1',width=5,height=2, bg = color4 ,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_7.place(x=0,y=156)
b_8 = Button(frame_corpo,text = '2',width = 5,height =2, bg = color4 ,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_8.place(x=59,y=156)
b_9 = Button(frame_corpo,text = '3',width = 5,height =2, bg = color4 ,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_9.place(x=118,y=156)
z_2 = Button(frame_corpo,text = '+',width = 5,height =2, bg = color5 ,font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
z_2.place(x=177,y=156)

#quinta linha
b_c = Button(frame_corpo,text = '0',width=11,height=2, bg = color4, font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_c.place(x=0,y=208)
b_c1 = Button(frame_corpo,text = '.',width = 5,height =2, bg = color4, font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_c1.place(x=118,y=208)
b_c1 = Button(frame_corpo,text = '=',width = 5,height =2, bg = color5, font=('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE) 
b_c1.place(x=177,y=208)




janela.mainloop()