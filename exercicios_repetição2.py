'''
Modifique o programa anterior para imprimir
 de 1 até o número digitado pelo usuário, mas dessa vez os números ímpares
 
 
fim = int(input('Digite um numero: '))
x = 1

while x <= fim:
	print (x)
	x = x + 2



Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3
'''

x = 1
cont = 0
i = 10

while cont < i:
	if x % 3 ==0:
		print(x)
		x = x + 1
		cont = cont + 1
	else:
		x = x + 1