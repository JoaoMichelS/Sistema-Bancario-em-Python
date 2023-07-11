'''
Desafio v1.0

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

Desafio v2.0

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, 
depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: 
criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

Separação em funções 

Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada 
função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por
você da forma que acha melhor.

Saque 

A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, 
extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

Depósito

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, 
valor, extrato. Sugestão de retorno: saldo e extrato.

Extrato

Afunção extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais:
saldo, argumentos nomeados: extrato.

Novas Funções

Precisamos criar duas funções: criar usuários e criar conta corrente. Fique a vontade para adicionar mais funções, 
exemplo: listar contas.

Criar Usuário (cliente)

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e
endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade / sigla estado. Deve ser armazenado
somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

Criar Conta Corrente

O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número
da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas
uma conta pertence a somente um usuário.

Dica 

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário 
da lista.
'''

import os
import msvcrt

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
        print("\nPressione uma tecla para continuar...")
        msvcrt.getch() # Aguarda a pressionar alguma tecla
        os.system("cls") # Limpa termial
             
        
    elif opcao == "s":
        print("-----Saque-----")
        print(f"Saldo da Conta: {saldo}")
        saq = float(input("Valor do Saque: "))
        if (saq <= 0) or (saq > 500):
            print("Valor do saque incorreto!")
        else:
            if saq > saldo:
                print("Saldo insuficiente!")
            else:
                if numeros_saques >= 3:
                    print("Limite de saques no dia alcançado!")
                else:
                    saldo -= saq
                    print(f"Saque realizado, novo saldo: {saldo}")
                    extrato.append(saq)
                    numeros_saques += 1
        print("\nPressione uma tecla para continuar...")
        msvcrt.getch() # Aguarda a pressionar alguma tecla
        os.system("cls") # Limpa termial
        
    elif opcao == "e":
        print("-----Extrato-----")
        extrato_formatados = ["R$ {:.2f}".format(ext) for ext in extrato]
        print(f"extrato: {extrato_formatados}")
        print("\nPressione uma tecla para continuar...")
        msvcrt.getch() # Aguarda a pressionar alguma tecla
        os.system("cls") # Limpa termial
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")