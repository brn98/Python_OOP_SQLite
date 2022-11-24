#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
bruno = Pessoa(1, "Bruno Costa")
print(bruno)

#Quero mostrar só o nome
print(bruno.nome)

print("###################")

#Chama o objeto de banco de dados
db = Database()

#instancia objeteo pessoaDao
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#quero carregar uma lista com o retorno do banco
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)