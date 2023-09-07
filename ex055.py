""" Faça um programa que leia o peso de 5 pessoas, no final mostre qual foi o Maior e Menor peso lidos.
"""
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de \33[0;32m{}\33[0m KG'.format(maior))
print('O menor peso lido foi de \33[0;31m{}\33[0m   KG'.format(menor))
