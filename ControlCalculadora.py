import this
import ModelCalculadora
opcao = 0 #instanciando a minha variável
num1 = 0
num2 = 0

def Menu():
    print('Escolha uma das opções abaixo:\n' +
          '1. Soma\n' +
          '2. Subtração\n' +
          '3. Divisão\n' +
          '4. Multiplicação\n' +
          '5. Tabuada')
    this.opcao = int(input())

def ColetarNum1():
    print('Informe o primeiro número:')
    this.num1 = float(input())

def ColetarNum2():
    print('Informe o segundo número:')
    this.num2 = float(input())

def Operacao():
    Menu()#Chamando o método menu, para mostrar os dados em tela
    while(this.opcao != -1):
        if(this.opcao == 1):
            ColetarNum1()#Pedindo para digitar o primeiro número
            ColetarNum2()#Pedindo para digitar o segundo número
            print(ModelCalculadora.somar(this.num1, this.num2))
        elif this.opcao == 2:
            ColetarNum1()
            ColetarNum2()
            print(ModelCalculadora.subtrair(this.num1, this.num2))
        elif this.opcao == 3:
            ColetarNum1()
            ColetarNum2()
            print(ModelCalculadora.dividir(this.num1, this.num2))
        elif this.opcao == 4:
            ColetarNum1()
            ColetarNum2()
            print(ModelCalculadora.multiplicar(this.num1, this.num2))
        elif this.opcao == 5:
            ColetarNum1()
            print(ModelCalculadora.tabuada(this.num1))
        else:
            print('Número digitado invalido!')

