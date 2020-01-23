# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Controle de Água - Unidade 1

import math

velocidade_de_vazao = float(raw_input())
diametro_cano = float(raw_input())
tempo = int(raw_input())                          #em segundos

seccao = (math.pi * diametro_cano**2) / 4
vazao = velocidade_de_vazao * seccao * 1000       #convertendo para litros
quantidade_de_agua = tempo * vazao

print "Quantidade de água =", quantidade_de_agua, "litros."
