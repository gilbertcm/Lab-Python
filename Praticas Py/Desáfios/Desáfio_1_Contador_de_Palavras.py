#Desáfio_1: Contador de Palavras
#Escreva um programa que contenha o número de palavras em uma frase digitada pelo usuário.

#variável que armazena o conjunto de palavras
frase = input("Digite uma frase: ")

#função split, divide o texto/frase em palavras
palavras = frase.split()
#len() obtém a contagem de palavras em palavras
contagem_palavras = len(palavras)

#teste da frase
print(contagem_palavras)











"""
Nesse exemplo, usamos a função split() para dividir o texto em palavras.
Em seguida, usamos a função len() para obter o número de palavras no texto.
"""

#fonte de apoio: 
#https://awari.com.br/string-contagem-de-strings/#:~:text=Uma%20forma%20simples%3A%20m%C3%A9todo%20count(),-Uma%20das%20formas&text=Nesse%20exemplo%2C%20utilizamos%20o%20m%C3%A9todo,ocorre%20duas%20vezes%20na%20frase.