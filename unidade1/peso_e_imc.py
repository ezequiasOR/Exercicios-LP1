#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Peso e IMC - Unidade 1

peso = float(raw_input())
altura = float(raw_input())

imc = peso / (altura ** 2)
peso_ideal = 24.9 * (altura ** 2)

peso_ganhar_perder = peso_ideal - peso

print 'IMC atual = %.2f' % imc
print 'Peso a ser ganho/perdido = %.2f' % peso_ganhar_perder
