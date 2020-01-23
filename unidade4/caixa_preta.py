# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Caixa Preta - Unidade 4

quantidade = int(raw_input())

dados_validos = 0
controle = True

for i in range(quantidade):
	entrada = str(raw_input()).split()
	peso = int(entrada[0])
	combustivel = int(entrada[1])
	altitude = int(entrada[2])
	
	if controle == True and peso < 0:
		print 'dado inconsistente. peso negativo.'
		controle = False
	elif controle == True:
		dados_validos += 1
	
	if controle == True and combustivel < 0:
		print 'dado inconsistente. combustível negativo.'
		controle = False
	elif controle == True:
		dados_validos += 1
	
	if controle == True and altitude < 0:
		print 'dado inconsistente. altitude negativa.'
		controle = False
	elif controle == True:
		dados_validos += 1
		
print '%d dados válidos.' % dados_validos
