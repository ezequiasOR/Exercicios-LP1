# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Dígitos de Verificação do CPF - Unidade 6

def calcula_digitos_verificacao(string):
	multiplicador = 10
	soma = 0
	nova_string = ''
	saida = ''

	for i in range(len(string)):
		soma += int(string[i]) * multiplicador
		multiplicador -= 1
		nova_string += string[i]
		
	divisao = (soma * 10) % 11
	if divisao == 10:
		divisao = 0
		saida += str(divisao)
	else:
		saida += str(divisao)

	nova_string += str(divisao)
	multiplicador = 11
	soma = 0

	for i in range(len(nova_string)):
		soma += int(nova_string[i]) * multiplicador
		multiplicador -= 1

	divisao = (soma * 10) % 11
	if divisao == 10:
		divisao = 0
		saida += str(divisao)
	else:
		saida += str(divisao)
	return saida
