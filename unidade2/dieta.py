# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Dieta - Unidade 2

peso = float(raw_input())                #Em Kg
tempo_exercicios = float(raw_input())    #Em horas
calorias = float(raw_input())            #Por dia

kg_calorias = peso * 7700
consumo_calorias = 2000 - calorias
exercicios_para_calorias = tempo_exercicios * 900 + consumo_calorias
dias = kg_calorias / exercicios_para_calorias

print 'Você precisará de %.2f dias de dieta' % dias
