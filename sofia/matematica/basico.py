from time import sleep
def soma(dadoc):
        result = 0
        for c in range(0,len(dadoc)):
            result = result  + dadoc[c]
        print('=-'*25)
        print('O resultado da soma é igual: {:.2f}'.format(result))
        sleep(2)
        print('-=-'*25)

def multiplique(dadomult):
    result_mult = 1
    for c in range(0,len(dadomult)):
        result_mult = result_mult  * dadomult[c]
    print('-=-'*20)
    print('O valor da Multiplicação é {:.2f}'.format(result_mult))
    sleep(2)
    print('-=-'*20)

def quantity(dadoquant):
    listquant = list()
    for c in range(0,dadoquant):
        listquant.append(float(input(f'Digiti o {c+1} da operação:')))
    return listquant
def divi(dadodivid,dadodivis):
     resul_divid = resul_divis = 0
     resul_divid = dadodivid / dadodivis
     resul_divis = dadodivid % dadodivis
     return resul_divid,resul_divis