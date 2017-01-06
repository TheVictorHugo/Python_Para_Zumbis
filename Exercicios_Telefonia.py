'''
Considere a empresa de telefonia Tchau.
Abaixo de 200 minutos, a empresa cobra R$
R$ 0,20 po minuto. Entre 200 e 400 minutos, o 
preço é R$ 0,18. Acima de 400 minutos o preço po minuto é 
R$ 0,15. Calcule sua conta de telefone.



x = float(input('Digite quantos minutos usados no mês: '))

if x < 200:
	cal = x * 0.20
	print('O gatso foi de R$%.2f por mês' %cal)
if x > 200 and x < 400:
	cal = x * 0.18
	print('O gatso foi de R$%.2f por mês' %cal)
if x > 400:
	cal = x * 0.15
	print('O gatso foi de R$%.2f por mês' %cal

'''

minutos = int(input('Minutos utilizados: '))
if minutos < 200:
	preço = 0.20
else:
	if minutos <= 400:
		preço = 0.18
	else:
		preço = 0.15
print('Conta telefônica: R$%6.2f' %(minutos * preço))