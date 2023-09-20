from os import system
import pickle

interfaceMenu = """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|       Cadastro de alunos        |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|                                 |
|1 - Cadastrar novo aluno         |
|2 - Pesquisar por nome           |
|3 - Exibir alunos cadastrados    |
|4 - Excluir cadastros existentes |
|5 - Sair                         |
|                                 |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
interfaceExcluir = """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|        Excluir cadastros        |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|                                 |
|1 - Excluir somente um           |
|2 - Excluir tudo                 |
|3 - Voltar para o menu principal |
|                                 |
|                                 |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""


class Alunos:
    def __init__(self):
        self.listaNomes = []
        self.listaMatriculas = []

    def inserir(self, nome_a, matricula_a):
        self.listaNomes.append(nome_a)
        self.listaMatriculas.append(matricula_a)
        self.salvar_alunos()

    def exibir(self):
        if len(self.listaNomes) == 0 and len(self.listaMatriculas) == 0:
            print("\nNão há alunos cadastrados.")
        else:
            for i in range(len(self.listaNomes)):
                print(
                    f"\nAluno {i+1}: \nNome: {self.listaNomes[i]} \nMatricula: {self.listaMatriculas[i]}"
                )

    def pesquisarAluno(self, nome_p):
        if len(self.listaNomes) == 0:
            print("\nNão há alunos cadastrados")
        else:
            for i, aluno_nome in enumerate(self.listaNomes):
                if aluno_nome.find(nome_p) != -1:
                    print(
                        f"\nAluno {i+1}: \nNome: {self.listaNomes[i]} \nMatricula: {self.listaMatriculas[i]}"
                    )

    def excluirTudo(self):
        opcao = input("\nTem certeza que deseja excluir tudo? (S/n) ")
        if opcao.lower() in ("s", "sim"):
            self.listaNomes.clear()
            self.listaMatriculas.clear()
            self.salvar_alunos()
            print("\nTodos os cadastros foram excluídos com sucesso!")
            return True
        else:
            return False

    def excluir1por1(self, indice):
        indice = int(indice)

        if indice == 0:
            print("\nDigite um número valido!")
        else:
            if indice < 0:
                indice = indice * -1
            print(
                f"\nO aluno {self.listaNomes[indice-1]} ({self.listaMatriculas[indice-1]}) foi excluído."
            )
            self.listaNomes.pop(indice - 1)
            self.listaMatriculas.pop(indice - 1)
            self.salvar_alunos()

    def excluirGeral(
        self,
    ):
        if len(self.listaNomes) == 0 and len(self.listaMatriculas) == 0:
            print("\nNão há alunos cadastrados.")
        else:
            while True:
                print(interfaceExcluir)
                opcao = input("Digite sua escolha: ")
                if opcao == "1":
                    self.exibir()
                    indice = input("\nDigite o número do aluno que será excluido: ")
                    self.excluir1por1(indice)
                    input("\nPressione ENTER para continuar")
                    system("cls")
                elif opcao == "2":
                    boolean = self.excluirTudo()
                    if boolean is True:
                        input("\nPressione ENTER para continuar")
                        break
                    else:
                        continue
                elif opcao == "3":
                    break

    def salvar_alunos(self):
        with open("alunos.pkl", "wb") as arquivo:
            pickle.dump((self.listaNomes, self.listaMatriculas), arquivo)

    def carregar_alunos(self):
        try:
            with open("alunos.pkl", "rb") as arquivo:
                self.listaNomes, self.listaMatriculas = pickle.load(arquivo)
        except FileNotFoundError:
            self.listaNomes = []
            self.listaMatriculas = []


alu = Alunos()
alu.carregar_alunos()


while True:
    try:
        print(interfaceMenu)
        opcao = input("Digite sua escolha: ")
        if opcao == "1":
            nome = input("\nDigite o nome: ")
            matricula = input("Digite a matricula: ")
            alu.inserir(nome, matricula)
            system("cls")
        elif opcao == "2":
            nome_p = input("\nFiltrar por nome de aluno: ")
            alu.pesquisarAluno(nome_p)
            input("\nPressione ENTER para continuar")
            system("cls")
        elif opcao == "3":
            alu.exibir()
            input("\nPressione ENTER para continuar")
            system("cls")
        elif opcao == "4":
            system("cls")
            alu.excluirGeral()
            system("cls")
        elif opcao == "5":
            print("\nFechando o programa...")
            break
        else:
            continue
    except ValueError:
        print("\nDigite um valor inteiro.")
    except IndexError:
        print("\nDigite um número de um aluno que exista.")
