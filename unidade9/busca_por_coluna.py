#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Busca por Coluna - Unidade 9

def busca_todos_por_coluna_em_matriz(m, e):
	posicoes = []
	for coluna in range(len(m[0])):
		for linha in range(len(m)):
			if m[linha][coluna] == e:
				posicao = (linha, coluna)
				posicoes.append(posicao)
	
	return posicoes
