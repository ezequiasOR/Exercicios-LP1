# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Caixa Alta - Unidade 6

def caixa_alta(frase):
	nova_frase = ''

	for letra in range(len(frase)-1):
		
		if letra == 0 and frase[1] == ' ':
			nova_frase += frase[letra].lower()
		elif letra == 0 and frase[1] != ' ':
			nova_frase += frase[letra].upper()
		else:
			
			if (frase[letra] >= 'A' and frase[letra] <= 'Z'):
				if frase[letra + 1] == ' ' and frase[letra - 1] == ' ':
					nova_frase += frase[letra].lower()
				else:
					nova_frase += frase[letra]
			elif (frase[letra] >= 'a' and frase[letra] <= 'z'):
				if (frase[letra + 1] != ' ' and frase[letra - 1] == ' '):
					nova_frase += frase[letra].upper()
				else:
					nova_frase += frase[letra]
			else:
				nova_frase += frase[letra]
				
	nova_frase += frase[-1].lower()

	return nova_frase
