class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
      return self.nome
    
    def get_idade(self):
      return self.idade
        

    def faixa_etaria(self, idade:int) -> str:
        if idade >= 65:
            self.etaria = "Idoso"
        elif idade >= 20:
            self.etaria = "Adulto"
        elif idade >= 12:
            self.etaria = "Adolescente"
        else:
            self.etaria = "Criança"
        

    def __repr__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Classificação Etária: {self.etaria}"
