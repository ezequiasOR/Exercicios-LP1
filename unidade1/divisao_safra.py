#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Divisão Safra - Unidade 1

qtd_soja = int(raw_input())
qtd_clientes_atacado = int(raw_input())
qtd_clientes_varejo = int(raw_input())

atacado = qtd_soja / qtd_clientes_atacado
varejo = (qtd_soja % qtd_clientes_atacado) / float(qtd_clientes_varejo)

print 'Clientes no atacado = %dkg cada.' % atacado
print 'Clientes no varejo = %.2fkg cada.' % varejo
