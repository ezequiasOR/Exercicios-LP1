#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Busca Todos - Unidade 9

def busca_matriz(m, e):
	posicoes = []
	for linha in range(len(m)):
		for coluna in range(len(m[0])):
			if m[linha][coluna] == e:
				posicao = (linha, coluna)
				posicoes.append(posicao)
	
	return posicoes
