# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Conversão de Medidas - Unidade 1

milhas = float(raw_input())
libras = float(raw_input())
galoes = float(raw_input())

km = milhas * 1.60934
kg = libras * 0.453592
litros = galoes * 3.78541

print km, kg, litros
