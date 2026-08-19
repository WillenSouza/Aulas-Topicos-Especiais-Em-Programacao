import sys
from .aluno import Aluno
from .lancamento import LancamentoNotas
from .classificacao import classificar
from .storage import Storage


ARQUIVO_CSV = "notas.csv"

def listar_turma(alunos):
    print("\n--- Turma ---")
    print(f"{'Matrícula':<15} {'Nome':<20} {'N1':<5} {'N2':<5} {'N3':<5} {'Média':<7} {'Status':<10}")
    print("-" * 65)
    for aluno in alunos:
        media = aluno.media_ponderada()
        status = classificar(aluno)
        print(f"{aluno.matricula:<15} {aluno.nome:<20} {aluno.notas[0]:<5} {aluno.notas[1]:<5} {aluno.notas[2]:<5} {media:<7.2f} {status:<10}")
    print()

def menu():
    alunos = []

    while True:
        print("\n--- Menu de Notas ---")
        print("1. Cadastrar aluno")
        print("2. Lançar avaliações")
        print("3. Listar turma")
        print("4. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            matricula = input("Matrícula: ").strip()
            nome = input("Nome: ").strip()
            aluno = Aluno(matricula, nome)
            alunos.append(aluno)
            print(f"Aluno {nome} cadastrado com matrícula {matricula}.")

        elif opcao == "2":
            if not alunos:
                print("Nenhum aluno cadastrado.")
                continue
            print("Alunos disponíveis:")
            for i, a in enumerate(alunos, 1):
                print(f"{i}. {a.nome} (matrícula: {a.matricula})")
            idx = input("Selecionar aluno (número): ").strip()
            try:
                i = int(idx) - 1
                if i < 0 or i >= len(alunos):
                    print("Índice inválido.")
                    continue
                aluno = alunos[i]
                n1 = float(input("Nota 1: "))
                n2 = float(input("Nota 2: "))
                n3 = float(input("Nota 3: "))
                LancamentoNotas(aluno).lançar(n1, n2, n3)
                print(f"Avaliações lançadas para {aluno.nome}.")
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "3":
            if not alunos:
                print("Nenhum aluno cadastrado.")
                continue
            Storage.salvar(alunos, ARQUIVO_CSV)
            alunos_carregados = Storage.carregar(ARQUIVO_CSV)
            listar_turma(alunos_carregados)

        elif opcao == "4":
            print("Até mais!")
            sys.exit(0)

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
