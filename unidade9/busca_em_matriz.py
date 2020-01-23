#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Busca em Matriz - Unidade 9

def busca_matriz(m, e):
	for linha in range(len(m)):
		for coluna in range(len(m[0])):
			if m[linha][coluna] == e:
				return linha, coluna
