'''
Considere a empresa de telefonia Tchau.
Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
Entre 200  e 400 minutos, o preço é R$ 0,18. Acima de 400 minutos
o preço por minuto é R$ 0,15. Calcule sua conta de telefone
'''

x = float(input('Digite quantos minutos ligados no telefone:'))

if x < 200:
	#preço 0,20
	cal = x * 0,20
	print("Total a pagar é %f" cal)

