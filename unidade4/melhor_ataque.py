#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Melhor Ataque - Unidade 4

num_times = int(raw_input())

lista_times = []
lista_gols = []
soma = 0.0

#Lê a quantidade de gols e coloca na lista_gols, lê o nome dos times e coloca na lista_times
#Soma o total de gols

for i in range(num_times):
	nome_time = str(raw_input())
	quant_gols = int(raw_input())
	lista_times.append(nome_time)
	lista_gols.append(quant_gols)
	soma += quant_gols
	
maior_gol = 0
cont = 0
time_maior_gol = []

#Vê qual a maior quantidade de gols
for i in lista_gols:
	if lista_gols[cont] > maior_gol:
		time_maior_gol = []
		maior_gol = lista_gols[cont]
		time_maior_gol.append(lista_times[cont])
		
	elif lista_gols[cont] == maior_gol:
		maior_gol = lista_gols[cont]
		time_maior_gol.append(lista_times[cont])
	cont += 1

media = soma / num_times
print 'Time(s) com melhor ataque (%d gol(s)):' % maior_gol

for i in time_maior_gol:
	print i

print
print 'Média de gols marcados: %.1f' % media
