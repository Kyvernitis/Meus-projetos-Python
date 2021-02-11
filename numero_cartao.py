lista_numeros_mastercard = ['51', '52', '53', '54', '55']
lista_numeros_americanExpress = ['34', '37']
lista_numeros_visaEletron = ['4026', '417500', '4508', '4844', '4913', '4917']
bandeira = 'Inderteminado'

numero_cartao = str(input('Digite os 4 primeiros numeros do seu cartão : ')).strip()
while len(numero_cartao) != 4 or numero_cartao in 'abcdefghijklmnopqrstuvwxyz':
	numero_cartao = str(input('Digite os 4 primeiros numeros do seu cartão : ')).strip()

if numero_cartao[0] in '3456':
	e_cartao_credito_ou_debito = True
	if numero_cartao[0] in '4':
		bandeira = 'VISA'
		if numero_cartao in lista_numeros_visaEletron:
			bandeira = 'Visa Eletron'
	elif numero_cartao[:2] in lista_numeros_mastercard:
		bandeira = 'Mastercard'
	elif numero_cartao[:2] in lista_numeros_americanExpress:
		bandeira = 'AMERICAN EXPRESS'
	else:
		bandeira = 'DESCONHECIDO'

else:
	e_cartao_credito_ou_debito = False

if e_cartao_credito_ou_debito:
	print(f'A bandeira do seu cartão de crédito ou débito é {bandeira}.')
else:
	print(f'Seu cartão NÃO é de crédito e nem de débito.')
