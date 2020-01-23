# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Roleta - Unidade 3

numero_da_aposta = int(raw_input())
cor_da_aposta = str(raw_input())

numero_sorteado = int(raw_input())
cor_sorteada = str(raw_input())

if numero_da_aposta == numero_sorteado and cor_da_aposta == cor_sorteada:
	pontos = 150
elif numero_da_aposta == numero_sorteado and cor_da_aposta != cor_sorteada:
	pontos = 100
elif numero_da_aposta != numero_sorteado and cor_da_aposta == cor_sorteada:
	pontos = 50
	if numero_sorteado > numero_da_aposta:
		pontos += 30
	elif numero_sorteado < numero_da_aposta:
		pontos += 50

else:
	pontos = 0

print pontos
