#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Agenda Telefônica - Unidade 8

def inserir(lista_nome, lista_numero):
	num = int(raw_input())
	for i in range(num):
		nome = str(raw_input())
		numero = str(raw_input())
		lista_nome.append(nome)
		lista_numero.append(numero)
		
def buscar(nome_buscar, lista_nome, lista_numero):
	saida = []
	final = '----------'
	
	for i in range(len(lista_nome)):
		if nome_buscar == lista_nome[i]:
			saida.append(lista_nome[i])
			saida.append(lista_numero[i])
			saida.append(final)
			
	return saida

def ordenar(lista_nome, lista_numero):
	for e in lista_nome:
		for i in range(len(lista_nome)-1):
			if lista_nome[i] > lista_nome[i+1]:
				lista_nome[i], lista_nome[i+1] = lista_nome[i+1], lista_nome[i]
				lista_numero[i], lista_numero[i+1] = lista_numero[i+1], lista_numero[i]
				
	for elemento in lista_nome:
		for j in range(len(lista_nome)-1):
			if lista_nome[j] == lista_nome[j+1]:
				lista_nome[j], lista_nome[j+1] = lista_nome[j+1], lista_nome[j]
				lista_numero[j], lista_numero[j+1] = lista_numero[j+1], lista_numero[j]

def meu_in(nome_buscar, lista_nome):
	for e in lista_nome:
		if e == nome_buscar:
			return True
	return False

lista_nome = []
lista_numero = []

while True:
	operacao = str(raw_input())
	if operacao == 'finalizar': break
	elif operacao == 'inserir':
		inserir(lista_nome, lista_numero)
	elif operacao == 'buscar':
		nome_buscar = str(raw_input())
		if meu_in(nome_buscar, lista_nome) == False:
			print 'Nome inexistente'
			print '----------'
		else:
			cont = 0
			for e in buscar(nome_buscar, lista_nome, lista_numero):
				if cont == 0:
					print 'Nome:', e
					cont += 1
				elif cont == 1:
					print 'Fone:', e
					cont += 1
				else:
					print e
					cont = 0
				
	elif operacao == 'imprimir':
		ordenar(lista_nome, lista_numero)
		for i in range(len(lista_nome)):
			print 'Nome:', lista_nome[i]
			print 'Fone:', lista_numero[i]
			print '----------'
