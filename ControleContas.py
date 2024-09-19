#definir as contas
class Conta:
    def __init__(self, valor, descricao, data_vencimento, tipo):
        self.valor = valor
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.tipo = tipo  # 'pagar' ou 'receber'
        self.paga = False
#exibir paga ou pendente
    def __repr__(self):
        status = "Pago" if self.paga else "Pendente"
        return f"{self.descricao} - R${self.valor:.2f} - {self.data_vencimento} - {status}"

#trabalhar com as contas
class GestorContas:

    #criação da variavel
    def __init__(self):
        self.contas = []

    # armazenamento da nova conta
    def lancar_conta(self, valor, descricao, data_vencimento, tipo):
        nova_conta = Conta(valor, descricao, data_vencimento, tipo)
        self.contas.append(nova_conta)
        print("Conta lançada com sucesso!")

    # listar contars, se contas estiver vazia o if retorna verdadeiro executando
    # o comando e o return impede o loop, caso if retorne falso o comando segue e o loop roda
    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta registrada.")
            return
        for conta in self.contas:
            print(conta)

    # define uma soma com a condição de tipo, caso atenda soma
    def total_contas(self, tipo):
        total = sum(conta.valor for conta in self.contas if conta.tipo == tipo)
        return total

    # define o os totais baseado em cada tipo, fazendo a conta do geral depois das variaveis prontas
    def total_geral(self):
        total_pagar = self.total_contas('pagar')
        total_receber = self.total_contas('receber')
        return total_receber - total_pagar

    # puxa novamente os totai baseados nos tipos e o geral e imprime eles na formatação de real com 2c decimais
    def visualizar_totais(self):
        total_pagar = self.total_contas('pagar')
        total_receber = self.total_contas('receber')
        total_geral = self.total_geral()
        print(f"Total de contas a pagar: R${total_pagar:.2f}")
        print(f"Total de contas a receber: R${total_receber:.2f}")
        print(f"Total geral: R${total_geral:.2f}")

#integra o menu
def main():
    gestor = GestorContas()
    while True:
        print("\nMenu:")
        print("1. Lançar conta")
        print("2. Listar contas")
        print("3. Visualizar totais")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        # if pra verificar a opção escolhida e excutar a função
        if escolha == "1":
            valor = float(input("Digite o valor da conta: "))
            descricao = input("Digite a descrição da conta: ")
            data_vencimento = input("Digite a data de vencimento (DD/MM/AAAA): ")
            tipo = input("Digite o tipo (pagar/receber): ").strip().lower()
            gestor.lancar_conta(valor, descricao, data_vencimento, tipo)

        elif escolha == "2":
            gestor.listar_contas()

        elif escolha == "3":
            gestor.visualizar_totais()

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

