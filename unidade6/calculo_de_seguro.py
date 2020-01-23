# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Cálculo de Seguro - Unidade 6

def calcula_seguro(valor, respostas):
	pontos = 0
	for i in range(len(respostas)):
		if i == 0:                              #Qual a idade?
			if respostas[i] <= 21:                  #até 21 anos
				pontos += 20
			elif 22 <= respostas[i] <= 30:          #de 22 a 30 anos
				pontos += 15
			elif 31 <= respostas[i] <= 40:          #de 31 a 40 anos
				pontos += 12
			elif 41 <= respostas[i] <= 60:          #de 41 até 60 anos
				pontos += 10
			else:                                   #acima de 60 anos
				pontos += 20
				
		elif i == 1:                            #Casado ou Solteiro?
			if respostas[i] == True:                #Casado
				pontos += 10
			else:                                   #Solteiro
				pontos += 20
				
		elif i == 2:                            #Mora em área de risco?
			if respostas[i] == True:                #Sim
				pontos += 20
			else:                                   #Não
				pontos += 10
				
		elif i == 3:                            #Possui portão eletrônico?
			if respostas[i] == True:                #Sim
				pontos += 20
			else:                                   #Não
				pontos += 10
				
		elif i == 4:                            #Casa ou apartamento?
			if respostas[i] == True:                #Casa
				pontos += 20
			else:                                   #Apartamento
				pontos += 10
				
		elif i == 5:                            #Casa própria ou alugada?
			if respostas[i] == True:                #Própria
				pontos += 10
			else:                                   #Alugada
				pontos += 20
				
		else:                                   #Uso do carro ('Lazer', 'Trabalho' ou 'Misto')
			if respostas[i] == 'Trabalho':
				pontos += 10
			elif respostas[i] == 'Lazer' or respostas[i] == 'Misto':
				pontos += 20

	if pontos <= 80:
		risco = 'Risco Baixo'
		valor_pagar = valor * 0.1
	elif 80 < pontos <= 100:
		risco = 'Risco Medio'
		valor_pagar = valor * 0.2
	elif pontos > 100:
		risco = 'Risco Alto'
		valor_pagar = valor * 0.3
		
	return [pontos, risco, valor_pagar]
