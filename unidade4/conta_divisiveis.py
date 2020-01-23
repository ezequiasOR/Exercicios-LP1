#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Conta Divisíveis - Unidade 4

k = int(raw_input())
n = int(raw_input())

inteiros_divisiveis_por_k = 0

for i in range(n):
	valores = int(raw_input())
	if valores % k == 0:
		inteiros_divisiveis_por_k += 1

porcentagem = (inteiros_divisiveis_por_k * 100.0) / n

print '%d (%.1f%%)' % (inteiros_divisiveis_por_k, porcentagem)
