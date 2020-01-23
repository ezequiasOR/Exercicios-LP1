# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Dígito Verificador de 5 Dígitos - Unidade 2

num_conta = str(raw_input())

soma = int(num_conta[0]) + int(num_conta[1]) + int(num_conta[2]) + int(num_conta[3]) + int(num_conta[4])
resto = soma % 11

print num_conta + '-' + '%02d' % resto
