import os

def transform(dados):
    inf = 0
    for c in dados:
        if ('.png' in c) or ('jpg' in c) or ('jpeg' in c):
            inf = inf + 1
            if 'png' in c:
                while True:
                    if f'{inf}.png' in dados:
                        print(f'existente: {inf}.png')
                        inf +=1
                    else:
                        os.rename(f'{c}',f'{inf}.png')
                        break
            elif 'jpg' in c:
                while True:
                    if f'{inf}.jpg' in dados:
                        print(f'existente: {inf}.jpg')
                        inf +=1
                    else:
                        os.rename(f'{c}',f'{inf}.jpg')
                        break
            elif 'jpeg' in c:
                while True:
                    if f'{inf}.jpeg' in dados:
                        print(f'existente: {inf}.jpeg')
                        inf +=1
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