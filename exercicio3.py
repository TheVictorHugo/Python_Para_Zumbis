#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
#Calcule o total em segundos.

x = int(input('Digite um dia: '))
y = int(input('Digte uma hora: '))
z = int(input('Digite um minuto: '))
a = int(input('Digite um segundo: '))

cal = a + (z * 60) + (y * 60 * 60) + (x * 24 * 60 * 60)

print('A Quantidade de segundos é: %i ' %cal)