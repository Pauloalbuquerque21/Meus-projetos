from tkinter import ttk
from tkinter import *

#tela de fundo
tela_principal = Tk()
tela_principal.title('Oraganizador')
tela_principal.geometry('435x310')

frame_supeior = Frame(tela_principal, bg = 'white')
frame_supeior.place(relx =0.05,rely=0.1, relwidth = 0.9, relheight = 0.5)


bt_organizar = Button(tela_principal, text = "Organizar")
bt_organizar.place(relx = 0.4, rely = 0.9)

tela_princial = mainloop()

