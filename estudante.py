import psycopg2
from conexao import Conexao

class Estudante():

    def cadastrar(self, nome, matricula):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            #cadastrar os registros na tabela
            cadastrar = f"INSERT INTO estudante (nome, matricula) VALUES ('{nome}', '{matricula}');"
            cursor.execute(cadastrar)
            #comitar os registros no database
            conexao.commit()
            return f"Estudante {nome} e com a matricula {matricula} foi cadastrado com sucesso"
        #exceção caso ocorra um erro ao cadastrar os registros na tabela
        except (Exception, psycopg2.DatabaseError) as error:
            print("\nFalha ao cadastrar o registro\n", error)
        #se tudo ocorrer corretamente, a conexão com o database é encerrada
        finally:
            if conexao:
                cursor.close()
                conexao.close()
                print("A conexão com PostgreSQL foi encerrada\n")

    def consultar(self):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            select = f"SELECT * FROM estudante;"
            cursor.execute(select)
            estudante = cursor.fetchall()

            if len(estudante):
                return estudante
            else:
                return "Nenhum registro foi encontrado"

        except (Exception, psycopg2.Error) as error:
            print("\nFalha ao consultar o registro\n", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()
                print("A conexão com PostgreSQL foi encerrada\n")

    def editar(self, nome, matricula):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            editar = f"UPDATE estudante SET matricula='{matricula}' WHERE nome='{nome}';"
            cursor.execute(editar)
            conexao.commit()
            return f"O estudante {nome} teve seus dados atualizados"

        except (Exception, psycopg2.Error) as error:
            print("\nFalha ao atualizar o registro\n", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    def remover(self, matricula):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            remover = f"DELETE FROM estudante WHERE matricula='{matricula}';"
            cursor.execute(remover)
            conexao.commit()
            return f"O estudante com a matricula {matricula} foi removido"

        except (Exception, psycopg2.Error) as error:
            print("\nFalha ao remover o registro\n", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()
                print("A conexão com PostgreSQL foi encerrada\n")