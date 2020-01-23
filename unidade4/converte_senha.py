# coding: utf-8

#######################################
#UFCG - Programação I - 2018.1        #
#Aluno: Ezequias Rocha								#
#Questão: Converte Senha - Unidade 4  #
#######################################

palavra = str(raw_input())
senha = ''
troca = 0
for i in range(len(palavra)):
	if i == 0:
		senha += palavra[i]
	elif palavra[i] == 'a' or palavra[i] == 'A':
		senha += '4'
		troca += 1
	elif palavra[i] == 'e' or palavra[i] == 'E':
		senha += '3'
		troca += 1
	elif palavra [i] == 'i' or palavra[i] == 'I':
		senha += '1'
		troca += 1
	elif palavra[i] == 'o' or palavra[i] == 'O':
		senha += '0'
		troca += 1
	else:
		senha += palavra[i]

print '%s (%d troca(s))' % (senha, troca)
