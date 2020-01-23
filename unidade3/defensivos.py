# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Defensivos - Unidade 3

tipo = str(raw_input())
area = int(raw_input())            #Em hectares

if tipo == 'Fungicida':
	if area % 50 != 0:
		quantidade = area / 50 + 1
	else:
		quantidade = area / 50
	preco = 320 * quantidade
	
elif tipo == 'Herbicida':
	if area % 3 != 0:
		quantidade = int(area * 0.3 + 1)
	else:
		quantidade = area * 0.3
	preco = 100 * quantidade
	
elif tipo == 'Inseticida':
	if area % 12 != 0:
		quantidade = area / 12 + 1
	else:
		quantidade = area / 12
	preco = 400 * quantidade

print '%d %s(s). %.02f reais.' % (quantidade, tipo, preco)
