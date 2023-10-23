import pymongo
from bson import ObjectId
from pymongo import MongoClient


try:    
    client = MongoClient('mongodb://localhost:27017/')
    db = client['trabalhoMongoDb']
    alunosCl = db.alunos

    print("********************* MONGODB CONECTADO COM SUCESSO *********************\n\n")
except:

    print("********************* ERROR AO CONECTAR NO MONGODB *********************\n\n")


def cadastrar_aluno():
    try:
        nome = input("\nDigite o nome do aluno: ")
        idade = int(input("\nDigite a idade do aluno: "))
        opcoesTurma = int(input("*** 1 - Turma A / 2 - Turma B / 3 - Turma C ***\n\nDigite o número referente a turma do aluno: "))

        turma = verificar_turma(opcoesTurma)

        aluno = {"nome": nome,
                "idade": idade,
                "turma": turma,
                "matricula": alunosCl.count_documents({})}

        alunosCl.insert_one(aluno)

        print("\nAluno cadastrado com sucesso!")

        return aluno
    except:
        print("\nOcorreu um erro ao cadastrar o aluno, tente novamente!")

        return


def atualizar_cadastro_aluno(matricula):
    aluno = alunosCl.find_one({'matricula': matricula})

    print(f"\nAluno: {aluno['nome']}")

    print("\n*** 1 - Nome / 2 - Idade / 3 - Turma ***")

    infoAluno = int(input("\nDigite o número referente a informação que deseja atualizar: "))

    if infoAluno == 1:
        try:
            nomeAntigo = {'nome': aluno["nome"]}

            novoNome = input("\nDigite o nome do aluno: ")

            novoNome = { "$set": { "nome": novoNome } }

            alunosCl.update_one(nomeAntigo, novoNome)

            print("\nCadastro atualizado com sucesso!")

            return aluno
        except:
            print("\nOcorreu um erro ao atualizar o cadastro, tente novamente!")

            return
    
    elif infoAluno == 2:
        try:
            idadeAntiga = {'idade': aluno["idade"]}

            novaIdade = int(input("\nDigite a idade do aluno: "))

            novaIdade = { "$set": { "idade": novaIdade } }

            alunosCl.update_one(idadeAntiga, novaIdade)

            print("\nCadastro atualizado com sucesso!")

            return aluno
        except:
            print("\nOcorreu um erro ao atualizar o cadastro, tente novamente!")

            return
    
    elif infoAluno == 3:
        try:
            turmaAntiga = {'turma': aluno["turma"]}

            novaTurma = int(input("*** 1 - Turma A / 2 - Turma B / 3 - Turma C ***\n\nDigite o número referente a turma do aluno: "))

            novaTurma = verificar_turma(novaTurma)

            novaTurma = { "$set": { "turma": novaTurma } }

            alunosCl.update_one(turmaAntiga, novaTurma)

            print("\nCadastro atualizado com sucesso!")

            return aluno
        except:
            print("\nOcorreu um erro ao atualizar o cadastro, tente novamente!")

            return
    
    else:
        print("Aluno não encontrado, informe uma matrícula existente!\n")

        return


def excluir_cadastro_aluno(matricula):
    aluno = alunosCl.find_one({'matricula': matricula})

    print(f"\nAluno: {aluno['nome']}")

    try:
        alunosCl.delete_one({'_id': ObjectId(aluno['_id'])})

        print("\nCadastro excluído com sucesso!")
    except:
        print("\nOcorreu um erro ao excluir o cadastro, tente novamente!")

    return


def consultar_cadastro_alunos(matricula):
    try:

        if matricula != "todos":
            matriculaAluno = int(matricula)

            aluno = alunosCl.find_one({'matricula': matriculaAluno})

            print("\n******************************************")
            print(f'Aluno: {aluno["nome"]}\nIdade: {str(aluno["idade"])}\nTurma: {aluno["turma"]}')
        else:
            for aluno in alunosCl.find():
                print("\n******************************************")
                print(f'Aluno: {aluno["nome"]}\nIdade: {str(aluno["idade"])}\nTurma: {aluno["turma"]}')
    except:
        print("\nOcorreu um erro ao consultar, tente novamente!")

    return


def verificar_turma(turma):
    if turma == 1:
        return "Turma A"
    
    elif turma == 2:
        return "Turma B"
    
    elif turma == 3:
        return "Turma C"
    
    else:
        print("Turma não encontrada, por gentileza escolha uma das opções informadas\n")
        return


print("********************* MONGODB ESCOLA *********************\n")
print("1 - CADASTRAR ALUNO\n2 - EDITAR CADASTRO DE ALUNO\n3 - EXCLUIR CADASTRO DE ALUNO\n4 - VISUALIZAR CADASTRO DE ALUNO\n")

opcao = int(input("Digite o número referente a ação que deseja realizar: "))

if opcao == 1:

    cadastrar_aluno()
elif opcao == 2:
    
    matriculaAluno = int(input("\nDigite a matrícula do aluno: "))

    atualizar_cadastro_aluno(matriculaAluno)
elif opcao == 3:

    matriculaAluno = int(input("\nDigite a matrícula do aluno: "))

    excluir_cadastro_aluno(matriculaAluno)
elif opcao == 4:

    matriculaAluno = input('\nDigite a matrícula do aluno ou "todos" para realizar uma consulta: ')

    consultar_cadastro_alunos(matriculaAluno)
else:
    print("opção inválida, por gentileza escolha uma das opções informadas")
