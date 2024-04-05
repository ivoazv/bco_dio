

class Cliente:
	def __init__(self, endereco):
		self.endereco = endereco
		self.contas = []



	def realizar_transacao(self, conta, transacao):
		transacao.registrar(conta)


	def adicionar_conta(self, conta):
		self.contas.append(conta)





class PessoaFisica(Cliente):
	def __init__(self, nome, cpf, data_nascimento, endereco):
		super().__init__(endereco)
		self.nome = nome
		self.cpf = cpf
		self.data_nascimento = data_nascimento




class Conta:
	def __init__(self, saldo, numero, agencia, cliente, historico):
		self._saldo = saldo
		self._numero = numero
		self._agencia = "001"
		self._cliente = cliente
		self._historico = Historico()


	@property
	def get_saldo():
		return self._saldo



	@property
	def get_numero():
		return self._numero



	@property
	def get_agencia():
		return self._agencia



	@property
	def get_cliente():
		return self._cliente



	@classmethod
	def nova_conta(cls, cliente, numero):
		return cls(numero, cliente)




	def sacar(self, valor):
		saldo = self._saldo
		excedeu_limite = valor > self._saldo
		if excedeu_limite:
			print("Saldo insuficiente!")
		elif valor > 0:
			self._saldo -= valor
			print ("Saque realizado com sucesso!!!")
			return True
		else:
			print ("Valor invalido!")

		return False




	def depositar(self, valor):
		if valor > 0:
			self._saldo += valor
			print("Deposito realizado com sucesso!")
		else:
			print("O valor informado e invalido!")
			return False

		return True



class ContaCorrente(Conta):
	def __init__(self, numero, cliente, limite=500, limite_saques=3):
		super().__init__(numero, cliente)
		self.limite = limite
		self.limite_saques = limite_saques



class Historico():
	def adicionar_transacao(transacao):