from time import sleep
print('Ola amigo, bom dia!!!!')
sleep(1)
n1 = 0
n2 = [1,2]
while True:
    n1 = int(input('Escolha uma das opções:\nMatemática[1]\nPortuguês[2]\nSair[10]\nQual?'))
    sleep(1)
    if n1 == 1:
        print('=-'*20)
        n3 = 0
        while  n3 !=1 and n3!=2:
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
                sleep(1)
                print('Fomula:\nan=a1+(n-1).r')
                print('-=-'*20)
                sleep(2)
                n12 = str(input('Informações:\nPrimeiro termo (a1) opção[A]\nUltimo termo (an) opção[B]\nRazão (r) opção[C]\nNúmero de termos n opção[D]\nQuais dessas opções você tem.Não coloca espaço entre as opçãos?')).strip().lower()
                n13 = len(n12)
                #print('{}'.format(len(n12)))
                if n13 >= 3:
                    if  n12 in 'abc' or 'acb' or 'bac' or 'bca' or 'cab' or 'cba':
                        n14 = int(input('Informe o Primeiro termo:'))
                        n15 = int(input('Informe o ultimo termo: '))
                        n16 = int(input('informe a razão:'))
                        pa1 = 1+((n15-n14)/n16)
                        print('O número de termos e igual {}'.format(pa1))
                        perg = str(input('Você quer ver todos os termos[S/N]?')).strip().lower()
                        if perg == 's':
                            print('Segue os termos:')
                            for c in range(n14,n15,n16):
                                print('{}'.format(c),end=' ')
                    elif n12 in 'bcd' or 'bdc' or 'cbd' or 'cdb' or 'dcb' or 'dbc':
                        n15 = int(input('Informe o Ultimo termo:'))
                        n16 = int(input('Informe a razão:'))
                        n17 = int(input('Informe o número de termos:'))
                    elif n12 in 'acd' or 'adc' or 'dac' or 'dca' or 'cad' or 'cda':
                        n18 = int(input('Informe o primeiro termo:'))
                        n19 = int(input('Informe a razão:'))
                        n20 = int(input('Informe o Número de termos:'))
                    elif n12 in 'abd' or 'adb' or 'dab' or 'dba' or 'bad' or 'bda':
                        n21 = int(input('informe o primeiro termo:'))
                        n22 = int(input('Informe o ultimo termo:'))
                        n23 = int(input('Informe o número de termos:'))
    if n1 == 10:
        break
                    