import psycopg2

# Estabelecendo a conexão
def conectardb():
    conexao = psycopg2.connect(database="minicursobd",
                               host="localhost",
                               user="postgres",
                               password="1234",
                               port="5432")
    return conexao

# Chame a função para testar a conexão
conexao = conectardb()

def inserir_usuario(email, nome, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuario (email, nome, senha) VALUES ('{email}', '{nome}', '{senha}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def buscar_usuario(nome):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT email,nome FROM usuario where nome= '{nome}' ")
    recset = cur.fetchall()
    conexao.close()

    return recset

def listar_usuarios():
    conexao = conectardb()

    cur = conexao.cursor()
    cur.execute(f"SELECT email,nome FROM usuario")
    recset = cur.fetchall()
    conexao.close()

    return recset

def verificarlogin(email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT * FROM usuario WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    conexao.close()

    return recset

def deletar_usuario(email):
    con = conectardb()  # Conectando ao banco de dados
    cur = con.cursor()  # Criando um cursor
    try:
        cur.execute('DELETE FROM usuario WHERE email = %s', (email,))
        con.commit()  # Use a conexão para commit
        print("Usuário deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        con.rollback()  # Use a conexão para rollback
    finally:
        cur.close()  # Fechando o cursor
        con.close()  # Fechando a conexão


def atualiza_usuario(nome, email):
    con = conectardb()  # Conectando ao banco de dados
    cur = con.cursor()  # Criando um cursor
    try:
        # Consulta SQL para atualizar o nome onde o email corresponde
        cur.execute('UPDATE usuario SET nome = %s WHERE email = %s', (nome, email))
        con.commit()  # Usando a conexão para commit
        print("Usuário atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        con.rollback()  # Usando a conexão para rollback
    finally:
        cur.close()  # Fechando o cursor
        con.close()  # Fechando a conexão




conexao.close()