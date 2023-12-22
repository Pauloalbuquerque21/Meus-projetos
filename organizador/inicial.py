import os

def transform(dados):
    inf = 0
    for c in dados:
        if ('.png' in c) or ('jpg' in c) or ('jpeg' in c):
            inf = inf + 1
            if 'png' in c:
                os.rename(f'{c}',f'{inf}.png')
            elif 'jpg' in c:
                os.rename(f'{c}',f'{inf}.jpg')
            elif 'jpeg' in c:
                os.rename(f'{c}',f'{inf}.jpeg')

historico = ['/home/paulo']
while True:
    os.chdir(historico[0])
    print(os.listdir())
    break

    

#while True:
#    caminho = input('Digite o caminho:').strip()
#    os.chdir(caminho)
#    dados_arquivo = os.listdir() 
#    print(dados_arquivo)
#    resultado = input('Deseja organizar arquivo:[y/n]:').lower()
#    if resultado == 'y':
#        transform(dados_arquivo)
#    else:
#        break