import os
caminho = input('Digite o caminho:')
os.chdir(caminho)
dados_arquivo = os.listdir()

def transform(dados):
    inf = 0
    for c in dados:
        print(c)
        if ('.png' in c) or ('jpg' in c) or ('jpeg' in c):
            inf = inf + 1
            if 'png' in c:
                os.rename(f'{c}',f'{inf}.png')
            elif 'jpg' in c:
                os.rename(f'{c}',f'{inf}.jpg')
            elif 'jpeg' in c:
                os.rename(f'{c}',f'{inf}.jpeg')

transform(dados_arquivo)