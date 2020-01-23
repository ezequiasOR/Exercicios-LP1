# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Adivinhão - Unidade 5

numero_alvo = int(raw_input())

cont = 1

while True:
	numeros_chutados = int(raw_input())
	if numeros_chutados == numero_alvo or abs(numero_alvo - numeros_chutados) > 100: break
	cont += 1

if numeros_chutados == numero_alvo:
	print 'Acertou o número alvo %d! Ganhou com %d tentativa(s).' % (numero_alvo, cont)
else:
	print 'Não acertou o número alvo %d! Foi eliminado com %d tentativa(s).' % (numero_alvo, cont)
