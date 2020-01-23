#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Verifica Desordenação - Unidade 8

def check_unsorted(seq):
	for i in range(len(seq)-1):
		if seq[i] > seq[i+1]:
			return i+1
	return -1

def main():
	while True:
		seq = raw_input()
		if seq == '0': break
		
		seq = map(int, seq.split())
		if len(seq) == 0 or len(seq) == 1:
			print 'ordenada'
		else:
			verifica = check_unsorted(seq)
			if verifica == -1:
				print 'ordenada'
			else:
				print 'desordenada: %s' % str(verifica)

if __name__ == "__main__":
	main()
