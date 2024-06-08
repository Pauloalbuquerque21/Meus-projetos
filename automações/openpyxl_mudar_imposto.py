from openpyxl import Workbook, load_workbook
import os 

#Vai levar o código para esse caminho 
os.chdir('C:/Users/paulo/Documents/estudos/excel')

# Abrir esse arquivo e vincular essas informações em uma variavel chamado planilha  
planilha = load_workbook('Produtos.xlsx')

#vai pegar a primeira aba, da planilha
aba_ativa = planilha.active


for celula in aba_ativa["C"]:
    if celula.value =="Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5

planilha.save("ProdutosOpenPy.xlsx")