# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Afinidade musical - Unidade 7

def tem_afinidade(l1, l2):
	artistas_em_comum = 0
	if len(l1) >= len(l2):
		maior = l1
		menor = l2
	else:
		maior = l2
		menor = l1
		
	for e in maior:
		for artista in menor:
			if e == artista:
				artistas_em_comum += 1

	if artistas_em_comum >= 3:
		return True
	else:
		return False
