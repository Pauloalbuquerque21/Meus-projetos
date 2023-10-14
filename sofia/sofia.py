from time import sleep
from matematica import basico 
print('Ola amigo, meu nome é Sofia!!!!')
sleep(1)
n1 = 0
n2 = [1,2]
while True:
    n1 = int(input('Escolha uma das opções:\nMatemática[1]\nPortuguês[2]\nSair[10]\nQual dessas opções você precisa de ajuda?'))
    sleep(1)
    if n1 == 1:
        print('=-'*20)
        while  True:
            options = int(input('O escolhido foi Matemática.\nCalculadora[1]\nProgreção Aritimetica[2]\nGeometria Plana[3]\nTrigonometria[4]\nLogaritimo[5]\nVoltar[10]\nEscolhe uma das opções:'))
            print('-=-'*10)
            if options == 1:
                print('-=-'*20)
                print('CALCULADORA')
                print('-=-'*20)
                calculadora = int(input('Soma[1]\nMultiplicação[2]\ndivisão[3]\nEscolha umas das opções:'))
                if calculadora == 1:
                    cal_soma = int(input('quantos números vão ser somados ?'))
                    soma_numb = basico.quantity(cal_soma)
                    basico.soma(soma_numb)
                elif calculadora == 2:
                    print('-=-'*20)
                    numb=int(input('Quantos números vão ser multiplicados:'))
                    num_mult = basico.quantity(numb)
                    basico.multiplique (num_mult)
                elif calculadora == 3:
                    print('-=-'*20)
                    dividendo = float(input('Informe o Dividendo:'))
                    divisor = float(input('Informe o divisor:'))
                    resultado_division = basico.division(dividendo,divisor)
                    print(f'O resultado da divisão {resultado_division[0]:.2f} e o resto {resultado_division[1]}')
                    sleep(1)
            elif options == 2:
                print('-=-'*20)
                print('PROGREÇÃO ARITIMÉTICA')
                print('-=-'*20)
                sleep(1)
                print('Fomula:\nan=a1+(n-1).r')
                print('-=-'*20)
                sleep(2)
                information = str(input('Informações:\nPrimeiro termo (a1) opção[A]\nUltimo termo (an) opção[B]\nRazão (r) opção[C]\nNúmero de termos n opção[D]\nQuais dessas opções você tem.Obs:Não coloca espaço entre as opçãos?')).strip().lower()
                information_size = len(information)
                #print('{}'.format(len(n12)))
                if information_size >= 3:
                    if  information in 'abc' or 'acb' or 'bac' or 'bca' or 'cab' or 'cba':
                        n14 = int(input('Informe o Primeiro termo:'))
                        n15 = int(input('Informe o ultimo termo: '))
                        n16 = int(input('informe a razão:'))
                        pa1 = 1+((n15-n14)/n16)
                        print('O número de termos e igual {}'.format(pa1))
                        sleep(1)
                        perg = str(input('Você quer ver todos os termos[S/N]?')).strip().lower()
                        if perg == 's':
                            print('Segue os termos:')
                            for c in range(n14,n15,n16):
                                print('{}'.format(c),end=' ')
                    elif information in 'bcd' or 'bdc' or 'cbd' or 'cdb' or 'dcb' or 'dbc':
                        n15 = int(input('Informe o Ultimo termo:'))
                        n16 = int(input('Informe a razão:'))
                        n17 = int(input('Informe o número de termos:'))
                    elif information in 'acd' or 'adc' or 'dac' or 'dca' or 'cad' or 'cda':
                        n18 = int(input('Informe o primeiro termo:'))
                        n19 = int(input('Informe a razão:'))
                        n20 = int(input('Informe o Número de termos:'))
                    elif information in 'abd' or 'adb' or 'dab' or 'dba' or 'bad' or 'bda':
                        n21 = int(input('informe o primeiro termo:'))
                        n22 = int(input('Informe o ultimo termo:'))
                        n23 = int(input('Informe o número de termos:'))
                elif information_size == 2:
                    print('-=-'*20)
                    print(f'Desculpa com apenas {information_size} opções não posso te ajudar')
                    print('-=-'*20)
                    sleep(1)
                elif information_size ==1:
                    print('-=-'*20)
                    print(f'Desculpa com apenas {information_size} apção não posso te ajudar')
                    print('-=-'*20)
                    sleep(1)
            elif options == 3:
                print('-=-'*20)
                print('GEOMETRIA PLANA')
                print('-=-'*20)
                geometria_plana = int(input('Aprender conceitos básicos[1]\nCalcular Área[2]\nEscolha uma das opções:'))
                if g1 == 1:
                    print('-=-'*20)
                    print('Ponto,Retas, planos, semirreta,semento de reta  e plano[1]')
                    print('-=-'*20)
                    sleep(2)
                    print('PONTOS:\nSão sempre representados por letras maiúsculas do nosso alfabeto.')
                    sleep(1)
                    print('RETAS\nSão sempre representadas por letras minúsculas do nosso alfabeto.\n OBS: lembre que consideramos as reta infita em ambos os lados, por isso existe os conceitos de Semirreta e segmento de reta.')
                    sleep(1)
                    print('SEMIRRETA\nÉ parte de uma que existe inicio, porem não existe fim')
                    sleep(1)
                    print('SEGUIMENTO DE RETA\nÉ uma reta que é limitada entre dois ponto, ou seja, ela tem início e fim.')
                    sleep(1)
                    print('PLANO\nÉ representada pelas letras do alfabeto grego.\nOBS:Se o plano não tiver suas dimenções definida por um valor escalar entenda que ele seja infinito.')
                    sleep(2)
                elif g1 == 2:
                    print('-=-'*20)
                    print('Calcular Area')   
                    print('-=-'*20) 
                    ca1 = int(input('Formas geometricas\nQuadrilátero[1]\nTrianfulo[2]\nEscolha uma das opções:'))
                    if ca1 == 1:
                        print('-=-'*20)
                        print('Quadrilátero')
                        print('-=-'*20)
                        ca2 = int(input('Formas de Quadrilátero:\nParalelogramo[1]\nQuadrado[2]\nRetangulo[3]\nLosango[4]\nTrapézio[5]\nEscolha uma das opções:'))
                        if ca2 == 1:
                            print("PARALELOGRAMO")
                            sleep(1)
                            pa1=float(input('Informe o valor da base:'))    
                            pa2=int(input('informe a altura'))
                            pa0=pa1*pa2
                            print('O valor da área do paralelograma com {} de base de {} de altura é igual a {}'.format(pa1,pa2,pa0))
                            sleep(1)
                        elif ca2 == 2: 
                            print('QUADRADO')  
                            sleep(1)
                            qua1=int(input('Informe um dos lados:'))
                            qua2=qua1*qua1
                            print('A area do quadrado que tem um dos lados igual a {} é igual a {}'.format(qua1,qua2))
                            sleep(1)
                            print("-=-"*10)
                        elif ca2 == 3:
                            print('Retangulo')
                            sleep(1)
                            re1 = int(input('Informe a base:'))
                            re2 = int(input('informe a altura:'))
                            re0 = re1 * re2
                            print('O a area do retnagulo com base {} e altura {} é igual {}'.format(re1,re2,re0))
                            sleep(1)
                            print('-=-'*10)
                        elif ca2 == 4:
                            print('Losango')    
                            sleep(1)
                            lo1 = int(input('Informe o diametro maior:'))
                            lo2 = int(input('Informe o diametro menor:'))
                            lo0 = (lo1*lo2)/2
                            print('A área do losango com dimetro {} e {} é igual {}'.format(lo1,lo2,lo0)) 
                        elif ca2 == 5:
                            print('Trapézio')
                            sleep(1)                     
                            tr1 = int(input('Informe a base maior:'))
                            tr2 = int(input('Informe a base menor:'))
                            tr3 = int(input('Informe a altura:'))
                            tr0 = ((tr1+tr2)*tr3)/2
                            print('A área do trapézio é {}'.format(tr0))
                            sleep(1)
                            print('-=-'*10)
            elif options == 4:
                print("-=-"*20)
                print("Trigonometria")
                print("-=-"*20)
                tg1 = int(input('Triangulo[1]'))
                if tg1 == 1:
                    tgt1 = int(input('Qual informação você precisa saber \n Cateto aposto[1]  Cateto adjacente[2]\nHipotenusa[3]  Angulo[4]\nQual dessas informações:'))
                    if tgt1 == 1:
                        tgt2 = int(input('Cateto adjacente?'))
                        tgt3 = int(input('Hipotenusa?'))
            elif options == 5:
                print("-=-"*20)
                print("LOGARITIMO")
                print("-=-"*20)
                log1=str(input('Informações:\nLogaritmando[A]\nLogaritmo[B]\nBase[C]\nQuais dessas opções você tem.Obs:Não coloca espaço entre as opçãos?')).lower().strip()
                log2 = len(log1)
                #print(log2)
                if log2 == 1:
                    print('Com apenas uma informação, não consigo te ajudar')
                elif log2 == 3:
                    print('Se você tem todas as informações, por que está me perguntando?')
                elif log2 == 2:
                    if log1 == "ab":
                        log3=int(input('Qual o Logaritmando?'))
                        log4=int(input('Qual o Logaritimo?'))
                        log5 = log3**(1/log4)
                        print(f'A base é igual {log5}')
                        sleep(1)
                    print('test')
                
            elif options == 10:
                break              
    if n1 == 10:
        print('-=-'*10)
        print('Foi um prazer te ajudar')
        print('-=-'*10)
        break

