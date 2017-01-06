'''
Determine se um ano é bissexto. Verifique no Google como fazer isso...

Como determinar se um ano é bissexto

Para determinar se um ano é um ano bissexto, siga estas etapas:
Se o ano for divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
Se o ano for divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
Se o ano for divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
O ano é bissexto (ele tem 366 dias).
O ano não é um ano bissexto (ele tem 365 dias).
'''

ano = int(input("Digite o ano: "))

if ano % 4 == 0:#etapa 1
	if ano % 100 == 0:
		if ano % 400 == 0:
			print('O ano é bissexto (ele tem 356 dias)')
		else:
			print('O ano não é um ano bissexto (ele tem 365 dias)')	
	else:
		print('O ano é bissexto (ele tem 356 dias)')
else:
	print('O ano não é um ano bissexto (ele tem 365 dias)')		

