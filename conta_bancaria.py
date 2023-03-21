class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if valor > self.saldo:
            print('Não é possível sacar um valor maior do que o saldo.')
        else:
            self.saldo -= valor


"""
OBS: a classe ContaBancaria é definida com um construtor que recebe um titular e um saldo. A variável self.titular é definida como o titular e self.saldo como o saldo inicial.

Em seguida, temos dois métodos, depositar e sacar. O método depositar adiciona o valor passado como parâmetro ao saldo da conta. Já o método sacar verifica se o valor a ser sacado é maior do que o saldo atual da conta. Se for, é exibida uma mensagem de erro. Caso contrário, o valor é subtraído do saldo atual.

"""            




