from time import sleep
print('Ola amigo, bom dia!!!!')
sleep(1)
n1 = int(input('Você precisa de ajuda ?\nMatemática[1]\nPortuguês[2]\nEscolha uma das opções que deseja ajuda:'))
n2 = [1,2]
while n1 != 1 and n1!=2:
    n1 = int(input('Não entendi, matemática[1] ou português[2]?'))
if n1 == 1:
    print('=-'*20)
    n3 = int(input('O escolhido foi Matemática.\nCalculadora[1]\nEscolhe uma das opções:'))
    if n3 == 1:
        print('=-'*20)
        n4 = int(input('[1]Soma\n[2]Multiplicação\n[3]divisão\nEs'))
        if n4 == 1:
            n5 = int(input('quantos números vão ser somados ?'))
            f = 0
            for c in range(1,n5+1):
                n6 = int(input('Número nº {}:'.format(c)))
                f= f + n6  
            print('O resultado da soma é igual: {}'.format(f))