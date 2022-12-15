import os
import pandas as pd

diretorio = r"" #Inclua o caminho especifico.
caminho = os.listdir(diretorio)

print(caminho) #Lista de arquivos e pastas no diretorio especificado

for x in caminho : #para cada arquivo no diretotio, um tipo de arquivo especificado sera retornado. No caso, arquivos Python.
    if x.endswith(".py"):
        print(f"Arquivos python: {x}")



