import os
from tkinter import tkk

def transform(dados):
    lista_pasta = dados
    lista_ideal = list()
    inf = 0
    for c in dados:    
        if ('.png' in c) or ('jpg' in c) or ('jpeg' in c):
            inf = inf + 1
            if 'png' in c:
                while True:
                    if f'{inf}.png' in dados:
                        if f'{inf}.png' == c:
                            print(f'{c} já atualizado')
                            break
                        else:
                            inf += 1
                    else:
                        os.rename(f'{c}',f'{inf}.png')
                        break
            elif 'jpg' in c:
                while True:
                    if f'{inf}.jpg' in dados:
                        if f'{inf}.jgp' == c:
                            print(f'{c} já atualizado')
                            break
                        else:
                            inf += 1
                    else:
                        os.rename(f'{c}',f'{inf}.jpg')
                        break
            elif 'jpeg' in c:
                while True:
                    if f'{inf}.jpeg' in dados:
                        if f'{inf}.jgep' == c:
                            print(f'{c} já atualizado')
                            break
                        else:
                            inf += 1
                    else:
                        os.rename(f'{c}',f'{inf}.jpeg')
                        break
while True:
    caminho = input('Digite o caminho:').strip()
    os.chdir(caminho)
    dados_arquivo = os.listdir() 
    print(dados_arquivo)
    resultado = input('Deseja organizar arquivo:[y/n]:').lower()
    if resultado == 'y':
        transform(dados_arquivo)
    else:
        break

