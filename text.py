d = [[2,3],[4,6]]
c = [[1,3,0],[2,1,1]]


def multiplicaMatrizes(a,b):
    mult = 0
    matriz_result_mult = list()
    if len(a[0]) == len(b):
        for linhas in range(0,len(a)):
            test = list()
            for colunas in range(0,len(b[0])):
                test.append(0)
            matriz_result_mult.append(test)
        for c in range(0,len(a)):
            for c3 in range(0,len(b[0])):
                result = 0
                for c2 in range(0,len(a[0])):
                    mult = a[c][c2] * b[c2][c3]
                    result = mult + result
                matriz_result_mult[c][c3] = result
        result_mult = matriz_result_mult
    else:
        result_mult = 'Inexistente!!'
    return result_mult

x = multiplicaMatrizes(d,c)
print(x)