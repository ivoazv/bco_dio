from abc import ABC
from datetime import datetime  

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



	def sacar(self, valor):
		numero_saques = len (
			[transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
		)

		excedeu_limite = valor > self.limite
		excedeu_saques = numero_saques >= self.limite_saques

		if excedeu_limite:
			print ("O valor excede o limite de saque.")
		elif excedeu_saques:
			print ("Número de saques excedido!")
		else:
			return super().sacar(valor)
		
		return False
	


	def __str__(self):
		return f"""
				Agência:\t{self.agencia}
				C/C:\t{self.numero}
				Titular:\t{self.cliente.nome}
		"""
	



class Historico():
	def __init__(self):
		self._transacoes = []

	@property
	def get_transacoes(self):
		return self._transacoes


	def adicionar_transacao(transacao):
		self._transacoes.append(
			{
				"tipo" : transacao.__class__.__name__,
				"valor" : transacao.valor,
				"data" : datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
			}
		)


class Transacao(ABC):
	@property
	@abstractproperty
	def valor(self):
		pass


	@abstractclassmethod
	def registrar(self, conta):
		pass



class Saque(Transacao):
	def __init__(self, valor):
		self._valor = valor


	@property
	def valor(self):
		return self._valor
	

	def registrar(self, conta):
		sucesso_transacao = conta.sacar(self.valor)

		if sucesso_transacao:
			conta.historico.adicionar_transacao(self)




class Deposito(Transacao):
	def __init__(self, valor):
		self._valor = valor


	@property
	def valor(self):
		return self._valor
	

	def registrar(self, conta):
		sucesso_transacao = conta.depositar(self.valor)

		if sucesso_transacao:
			conta.historico.adicionar_transacao(self)
