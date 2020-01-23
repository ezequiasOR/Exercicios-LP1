# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Caixa Registradora - Unidade 6

def caixa_registradora(valores, meta):
	soma = 0
	soma_comissao = 0

	for e in valores:
		soma += e
		if e < 1000.0:
			comissao = e * 0.05
			soma_comissao += comissao
		elif 1000.0 <= e < 5000.0:
			comissao = e * 0.1
			soma_comissao += comissao
		else:
			comissao = e * 0.15
			soma_comissao += comissao

	if soma - soma_comissao >= meta:
		situacao_do_dia = 'Lucro'
	else:
		situacao_do_dia = 'Prejuizo'

	return [soma, soma_comissao, situacao_do_dia]
