from time import sleep
print('Ola amigo, bom dia!!!!')
sleep(1)
n1 = int(input('Você precisa de ajuda ?\nMatemática[1]\nPortuguês[2]\nEscolha uma das opções que deseja ajuda:'))
n2 = [1,2]
while n1 != 1 and n1!=2:
    n1 = int(input('Não entendi, matemática[1] ou português[2]?'))
if n1 == 1:
    print('=-'*20)
    n3 = int(input('O escolhido foi Matemática.\nCalculadora[1]\nProgreção Aritimetica[2]\nEscolhe uma das opções:'))
    if n3 == 1:
        print('-=-'*20)
        print('CALCULADORA')
        print('-=-'*20)
        n4 = int(input('[1]Soma\n[2]Multiplicação\n[3]divisão\nEscolha umas das opções:'))
        if n4 == 1:
            n5 = int(input('quantos números vão ser somados ?'))
            f = 0
            for c in range(1,n5+1):
                n6 = float(input('Número nº {}:'.format(c)))
                f= f + n6  
            print('O resultado da soma é igual: {:.2f}'.format(f))
        elif n4 == 2:
            print('-=-'*20)
            numb=int(input('Quantos números vão ser multiplicados:'))
            g=1
            for d in range(1,numb+1):
                n7 = float(input('Número nª{}:'.format(d)))
                g=g*n7
            print('O valor da Multiplicação é {:.2f}'.format(g))
        elif n4 == 3:
            print('-=-'*20)
            n8 = float(input('Informe o Dividendo:'))      
            n9 = float(input('Informe o divisor:')) 
            n10 = n8 / n9
            n11 = n8 % n9
            print('O resultado da divisão {:.2f} e o resto {:.2f}'.format(n10,n11))
    elif n3 == 2:
        print('-=-'*20)
        print('PROGREÇÃO ARITIMÉTICA')
        print('-=-'*20)
        sleep(2)
        print('\033[32mFomula:\nan=a1+(n-1).r\033[m')
        print('-=-'*20)
        sleep(2)
        n12 = int(input('Informações:\nPrimeiro termo (a1) [1]\nUltimo termo (an) [2]\nRazão (n) [3]\nNúmero de termos (n) [4]\nQuais dessas informações você tem?'))
                