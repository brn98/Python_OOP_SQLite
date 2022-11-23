#Importar nosso aquivo Pessoa.py do diretorio model
from model.Pessoa import Pessoa

#exemplos de uso
bruno = Pessoa(1, "Bruno Costa")
print(bruno)

#mostrando somento o nome
print(bruno.nome)