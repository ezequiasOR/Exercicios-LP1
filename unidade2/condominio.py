# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Construção de Condomínio - Unidade 2

lado1 = float(raw_input())
lado2 = float(raw_input())
area_casas = float(raw_input())

area_condominio = lado1 * lado2
casas = area_condominio / area_casas

print '%d casa(s) pode(m) ser construída(s) no terreno.' % casas
