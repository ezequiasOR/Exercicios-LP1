# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Converte matrícula - Unidade 4

matricula_antiga = str(raw_input())
matricula_nova = ''

if matricula_antiga[0] == '2' and len(matricula_antiga) == 8:
	for i in range(len(matricula_antiga)):
		if i == 0:
			matricula_nova += '1'
		elif i ==  4:
			matricula_nova += matricula_antiga[i] + '0'
		else:
			matricula_nova += matricula_antiga[i]
	
	print int(matricula_nova)
