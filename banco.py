##nome e saldos opcionais:

nome = input("Digite seu nome: ")
saldo = float(input("digite seu saldo: "))


##opções bancárias pré estabelecidas:

tipo_conta = "corrente"


menu = "nome: {}        saldo: {}       tipo de conta: {}       opções: 1 - Verificar saldo  2 - Receber valor  3 - Transferir valor  4 - sair".format(nome, saldo,tipo_conta)

print(menu)

##interação com o usuário:

escolha_do_usuario  = int(input("o que deseja fazer?: "))

##operação:

while escolha_do_usuario == 1:
    escolha_do_usuario = 0
    print("seu saldo é: {} ".format(saldo))
    print(menu)
    escolha_do_usuario = int(input("o que deseja fazer?: "))

while escolha_do_usuario == 2:
    escolha_do_usuario = 0
    valor_recebido = float(input("Quanto será o valor recebido?: "))
    saldo = saldo + valor_recebido
    print("Você recebeu {}".format(valor_recebido))
    print("Seu saldo atual é de {}".format(saldo))
    print(menu)
    escolha_do_usuario = int(input("o que deseja fazer?: "))

while escolha_do_usuario == 3:
    escolha_do_usuario = 0
    valor_transferido = float(input("Quanto gostaria de transferir?: "))
    if valor_transferido > saldo:
        valor_transferido = 0
        print("Saldo insuficiente")
        while valor_transferido > saldo:
            print(menu)
            escolha_do_usuario = int(input("o que deseja fazer?: "))
    saldo = saldo - valor_transferido
    print("Você transferiu: {}".format(valor_transferido))
    print("Seu saldo atual é de: {}". format(saldo))
    print(menu)
    escolha_do_usuario = int(input("o que deseja fazer?: "))

if escolha_do_usuario == 4:
    print("saindo...")

