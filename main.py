#  instanciar um objeto da classe ContaBancaria de seguinte forma:

from conta_bancaria import ContaBancaria

# Cria uma nova conta bancária com saldo inicial de 2400
minha_conta = ContaBancaria('João', 2400)

# Realiza um depósito de 600
minha_conta.depositar(600)

# Realiza um saque de 200
minha_conta.sacar(200)

# Exibe o saldo atual da conta
print('Saldo atual da conta: R${:.2f} reais.'.format(minha_conta.saldo))


"""
OBS
objeto chamado minha_conta com o titular "João" e saldo inicial de 1000. Em seguida, depositamos 500 na conta e sacamos 200. Por fim, exibimos o saldo atual da conta, que deve ser 1300.

"""