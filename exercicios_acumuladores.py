#Calcule a média de 10 números inteiros

i = 0
x = 10
soma = 0

while i < x:
	num = int(input('Digite Número: '))
	soma = soma + num
	i = i + 1
print('A media é %i' %(soma / 10))
