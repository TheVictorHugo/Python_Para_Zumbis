'''
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a
porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.
'''

x = int(input('Qual é o salario: '))
y = int(input('Qual é a porcentadem de almento: '))

cal = x * (y/100)
cal2 = x + cal
print('O valor do salário com o aumento é %i' %cal2)
