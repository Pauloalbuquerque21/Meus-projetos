from time import sleep
print('Ola amigo, bom dia!!!!')
sleep(1)
n1 = int(input('Você precisa de ajuda ?\nMatemática[1]\nPortuguês[2]\nEscolha uma das opções que deseja ajuda:'))
n2 = [1,2]
while n1 != 1 and n1!=2:
    n1 = int(input('Não entendi, matemática[1] ou português[2]?'))
