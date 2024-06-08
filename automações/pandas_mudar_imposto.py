from IPython.display import display
import os 
import pandas as pd
#o Python vai nessa pasta.
os.chdir('C:/Users/paulo/Documents/estudos/excel')

#você vai ler um tabela em excel e atribuir-la à variavel tabela.
tabela = pd.read_excel('Produtos.xlsx')
display(tabela)

tabela.loc[tabela["Tipo"]=="Serviço","Multiplicador Imposto"] = 1.5

tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela['Preço Base Original']

tabela.to_excel("ProdutosPandasPandas.xlsx", index=False)






