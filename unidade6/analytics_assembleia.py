# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Analytics Assembleia - Unidade 6

def meu_split(votacoes):
	lista = []
	palavra = ''
	for i in range(len(votacoes)):
		if votacoes[i] == ',':
			lista.append(palavra)
			palavra = ''
		elif votacoes[i] != ',':
			palavra += votacoes[i]
		
	lista.append(palavra)

	return lista

def meu_in_voto(votacoes):
	for e in meu_split(votacoes):
		if e == 'sim':
			return 'sim'
		elif e == 'nao':
			return 'nao'

def meu_in_id(votacoes, id_votacao):
	for e in meu_split(votacoes):
		if e == str(id_votacao):
			return True
	return False

def conta_votos(votacoes, id_votacao):
	votos_sim = 0
	votos_nao = 0
	
	for e in votacoes:
		if meu_in_id(e, id_votacao) == True:
			if meu_in_voto(e) == 'sim':
				votos_sim += 1
			elif meu_in_voto(e) == 'nao':
				votos_nao += 1
				
	return [votos_sim, votos_nao]
