# Funções
def valid_num(lower, higher, can_exit=False):
	while True:
		num = ""
		while num == "":
			num = input("Qual seu antecedente?: ")
			if can_exit and (num == "end" or num == "exit" or num == "fim" or num == "sair"):
				print()
				return "exit"
			try:
				num = int(num)
				if num >= lower and num <= higher:
					for i in range(1, num+1):
						if num == i:
							print()
							return num 
				else: print("Digite um número válido!\n")
			
			except Exception:
				try:
					num = float(num)
				except Exception:
					pass
				if isinstance(num, float):
					print("Digite um número válido!\n")
				else:
					print("Digite um número!\n")
				pass