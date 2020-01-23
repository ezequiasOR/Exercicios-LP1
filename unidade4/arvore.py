#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Árvore de Natal - Unidade 4

altura = int(raw_input())

cont = 1
os = 0
espacos = ' '

for i in range(altura):
	print espacos * (altura - cont) + 'o' + 2 * os * 'o'
	cont += 1
	os += 1

print espacos * (altura - 1) + 'o'
