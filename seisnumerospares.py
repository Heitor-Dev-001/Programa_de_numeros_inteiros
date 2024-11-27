#Desenvolva um programa que leia seis números inteiros e mostre 
# a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o

#Resumo: Se o número for par some, caso não, descarte e informe ao usuário

#Entrada
print('{:=^40}'.format('Heitor Cálculo'))

import emoji

numero = int 

for numero in range (0,7):
    if numero %2 == 0:
        soma = numero
        print('\033[1;31;41m O resultado é:{} \033[m'.format(numero+soma))
        
    else:
        print('Seu número é impar, desconsiderar👍')
    print('-=-'*20)
print('Fim do programa')
    
