# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Consumo Gasolina MT1 - Unidade 1

#ler a posição (em Km) e a quantidade de Litros
pos_inicial = float(raw_input())
litros_inicial = float(raw_input())
pos_final = float(raw_input())
litros_final = float(raw_input())

#Calcula a distância, a quantidade de litros gasto e o consumo
distancia = pos_final - pos_inicial
delta_consumo = litros_inicial - litros_final
consumo = distancia / delta_consumo

print '%.1f' % consumo

