#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Código de César - Unidade 8

def cesar(texto, delta):
	codigo = ''
	for e in texto:
		if 60 <= ord(e)+delta <= 90 or 97 <= ord(e)+delta<= 122:
			codigo += chr(ord(e)+delta)
		elif ord(e)+delta > 122 or ord(e)+delta > 90:
			codigo += chr(ord(e)+delta-26)
		else:
			codigo += chr(ord(e))

	return codigo
