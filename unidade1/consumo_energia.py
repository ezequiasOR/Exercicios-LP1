# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Consumo Energia - Unidade 1

potencia = int(raw_input())
tempo_ligado = int(raw_input())

kwatts = potencia / 1000.0
tempo_hora = tempo_ligado / 60.0
quilowatt_hora = kwatts * tempo_hora

print str(quilowatt_hora) + " kWh" 
