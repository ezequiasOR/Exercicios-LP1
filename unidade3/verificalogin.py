# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Verifica Login - Unidade 3

email = str(raw_input())
senha = str(raw_input())

login_adm = 'admin@tst.ufcg.edu.br'
senha_adm = 'TstAdminProg1'

if email == login_adm and senha == senha_adm:
	print 'Login efetuado com sucesso!'
elif email == login_adm and senha != senha_adm:
	print 'Senha inválida. Tente novamente.'
elif email != login_adm and senha == senha_adm:
	print 'Email inválido.'
else:
	print 'Login inválido.'
