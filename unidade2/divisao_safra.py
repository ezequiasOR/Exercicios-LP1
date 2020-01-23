# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Divisão Safra - Unidade 2

safra = int(raw_input())
atacado_clientes = int(raw_input())
varejo_clientes = int(raw_input())

safra_atacado = safra / atacado_clientes
resto = float(safra % atacado_clientes)
safra_varejo = resto / varejo_clientes

print 'Clientes no atacado = %dkg cada.' % safra_atacado
print 'Clientes no varejo = %.2fkg cada.' % safra_varejo
