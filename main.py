import csv
import requests

from config import URL,ARQUIVO_CSV
#Requisicao  para o link do arquivo.csv
response = requests.get(URL)
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    writer = csv.writer(novo_arquivo)
    for linha in response.iter_lines():
        writer.writerow(linha.decode('utf-8').split(','))

#Abrir o arquivo .csv apartir do projeto raiz
with open(ARQUIVO_CSV) as arquivo:
    leitor_exemplo = csv.reader(arquivo)
    for linha in leitor_exemplo:
        if linha[2] == 'Brazil' and linha[3] == '2020-09-07':
            print(f" Linha # {leitor_exemplo.line_num} {linha}")
