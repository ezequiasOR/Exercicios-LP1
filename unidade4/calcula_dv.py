# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Calcula DV - Unidade 4

numero_de_banco = str(raw_input())
posicao_par = []
posicao_impar = []

for i in range(len(numero_de_banco)):
	if i % 2 == 0:
		posicao_par.append(numero_de_banco[i])
	else:
		posicao_impar.append(numero_de_banco[i])

soma_par = 0
soma_impar = 0

for c in posicao_par:
	par = int(c)
	soma_par += par

for e in posicao_impar:
	impar = int(e)
	soma_impar += impar

par_vezes_impar = (soma_par * soma_impar) % 11

if par_vezes_impar == 10:
	print numero_de_banco + '-X'
else:
	print numero_de_banco + '-%d' % par_vezes_impar
