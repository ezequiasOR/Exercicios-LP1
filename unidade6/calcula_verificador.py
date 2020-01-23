# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Calcula Verificador - Unidade 6

def calcula_verificador(numero):
	soma = 0
	cont = 0
	while soma < 19:
		texto = str(numero)
		if len(texto)-1 == cont:
			soma += int(texto[cont])
			break
		else:
			soma += int(texto[cont])
		cont += 1

	digito_verificador = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

	resto = soma % 11

	digito = digito_verificador[resto]
	return digito
