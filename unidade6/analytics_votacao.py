# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Analytics Votação - Unidade 6

def meu_split(votacoes):
	lista = []
	palavra = ''
	for i in range(len(votacoes)):
		if votacoes[i] == ',':
			lista.append(palavra)
			palavra = ''
		else:
			palavra += votacoes[i]
	lista.append(palavra)

	return lista
	
def meu_in(condicao, votacoes):
	for e in meu_split(votacoes):
		if e == condicao:
			return True
	return False

def conta_votos(votacoes, id):
	sim = 'sim'
	nao = 'nao'
	votos_sim = 0
	votos_nao = 0
	
	for e in votacoes:
		if meu_in(str(id), e) == True:
			if meu_in(sim, e) == True:
				votos_sim += 1
			elif meu_in(nao, e) == True:
				votos_nao += 1
	votos = [votos_sim, votos_nao]
	return votos
