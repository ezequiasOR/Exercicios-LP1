#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Conta Inversa - Unidade 4

palavra = str(raw_input())

nova_palavra = ''

for i in range(len(palavra)-1, -1, -1):
	nova_palavra += palavra[i]

cont = 0
coincidente = 0

for i in palavra:
	if i == nova_palavra[cont]:
		coincidente += 1
	cont += 1

print 'A palavra %s contém %d caractere(s) coincidente(s) com a sua inversa.' % (palavra, coincidente)
