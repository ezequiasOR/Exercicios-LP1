#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Calculadora de Médias - Unidade 8

def media_aritmetica(valores):
	n = len(valores)
	soma = 0
	for e in valores:
		soma += float(e)
	media = soma / n
	return media

def media_geometrica(valores):
	n = len(valores)
	media = float(valores[0])
	
	for i in range(1, n):
		media *= float(valores[i])
	media **= (1.0/n)
	return media

def media_harmonica(valores):
	n = len(valores)
	soma = 0
	for e in valores:
		soma += (1/float(e))
	media = n / soma
	return media

while True:
	tipo_da_media = str(raw_input()).split()
	if tipo_da_media[0] == 'Q': break
	
	valores = str(raw_input()).split()
	
	for j in range(len(tipo_da_media)):
		
		if tipo_da_media[j] == 'MA':
			print 'Média Aritmética: %.4f' % media_aritmetica(valores)
		elif tipo_da_media[j] == 'MG':
			print 'Média Geométrica: %.4f' % media_geometrica(valores)
		elif tipo_da_media[j] == 'MH':
			print 'Média Harmônica: %.4f' % media_harmonica(valores)
	print '----'
