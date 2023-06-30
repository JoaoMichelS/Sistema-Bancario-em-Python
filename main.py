'''
Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar 
suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar 
apenas 3 operações: depósito, saque e extrato.

Operação de Depósito

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com
1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

Operação de Saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não 
tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por 
falta de saldo. Todos os saques devem der armazenados em uma variável e exibidos na operação de extrato.

Operação de Extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido 
o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
'''

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("-----Depósito-----")
        print(f"Saldo da Conta: {saldo}")
        dep = float(input("Valor do Depósito: "))
        if dep <= 0:
            print("Valor de depósito incorreto!")
        else:
            saldo += dep
            print(f"Depósito realizado, novo saldo: {saldo}")
            extrato.append(dep)        
        
    elif opcao == "s":
        print("Saque")
    elif opcao == "e":
        extrato_formatados = ["R$ {:.2f}".format(ext) for ext in extrato]
        print(f"extrato: {extrato_formatados}")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")