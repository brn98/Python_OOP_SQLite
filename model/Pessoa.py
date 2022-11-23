class Pessoa: 
  #atributos
  id = None
  nome = None

  #Método Const
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

  #metodo para ajudar na exibição
  def __str__(self):
    return f"{self.nome} ({self.id})"