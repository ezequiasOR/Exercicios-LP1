#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Classifica Letra - Unidade 4

palavra = str(raw_input())

for i in palavra:
	if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
		print '<%s> sim' % i
	elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
		print '<%s> sim' % i
	else:
		print '<%s> nao' % i
