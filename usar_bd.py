import DAO

#DAO.inserir_pessoa('teste@teste.com', 'user teste', 'senha123')

#saida = DAO.buscar_pessoa('user teste')

saida = DAO.listar_usuarios()

#saida = DAO.verificarlogin('teste@teste.com', 'senha123')

#saida = DAO.deletar_usuario('amanda@amanda.com')

#saida = DAO.atualiza_usuario('amanda','teste@teste.com')

print(saida)