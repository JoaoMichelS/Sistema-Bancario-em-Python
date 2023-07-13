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
import colorama
from colorama import Fore

def main():
    # pip install colorama
    colorama.init()
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

    => """
    saldo_conta = 0
    limite_sacar = 500
    extrato = ""
    num_saques = 0
    NUM_LIM_SAQUE = 3

    while True:
        opcao = int(input(menu))
        if opcao == 1: 
            saldo_conta,extrato = depositar(saldo_conta,extrato)
        elif opcao == 2:
            NUM_LIM_SAQUE,saldo_conta,limite_sacar,num_saques,extrato = sacar(NUM_LIM_SAQUE,saldo_conta,limite_sacar,num_saques,extrato)
        elif opcao == 3:
            imprimirExtrato(extrato,saldo_conta)
        elif opcao == 4:
            break
        else:
            print(Fore.RED + "\nOpção inserida é inválida. Selecione novamente." + Fore.RESET)
    
    colorama.deinit()

def depositar(saldo_conta,extrato):
    val = float(input("Inserir o valor do depósito: "))

    if val > 0:
        saldo_conta += val
        extrato += f"\n\t[1] Depósito: R$ {val:.2f}"  
    else:
        print(Fore.RED + "\nErro! Não foi possivel realizar o deposito pois o valor não era válido." + Fore.RESET)
    return saldo_conta, extrato

def sacar(NUM_LIM_SAQUE,saldo_conta,limite_sacar,num_saques,extrato):
    val = float(input("Inserir o valor do saque: "))

    if val > saldo_conta:
        print(Fore.RED + "\nErro! Não foi possivel realizar o saque pois o saldo não é suficiente." + Fore.RESET)
    elif val > limite_sacar:
        print(Fore.RED + "\nErro! Não foi possivel realizar o saque pois o saque excedeu o valor limite." + Fore.RESET)
    elif num_saques >= NUM_LIM_SAQUE:
        print(Fore.RED + "\nErro! Não foi possivel realizar o saque pois foi excedido o número máximo de saques." + Fore.RESET)
    elif val > 0:
        saldo_conta -= val
        extrato += f"\n\t[2] Saque: R$ {val:.2f}"
        num_saques += 1
    else:
        print(Fore.RED + "\nErro! O valor informado não é válido." + Fore.RESET)
    return NUM_LIM_SAQUE,saldo_conta,limite_sacar,num_saques,extrato


def imprimirExtrato(extrato,saldo_conta):
    print(Fore.BLUE + " EXTRATO ".center(40,"="))
    print("\nNão houve movimentação na conta.\n" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo_conta:.2f}\n"+("="*40) + Fore.RESET)


if __name__ == "__main__":
    main()