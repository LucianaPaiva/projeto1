class Pessoa:
    matricula = 0
    def __init__(self, nome: str, idade: int):
        Pessoa.matricula += 1
        self.matricula = Pessoa.matricula
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"({self.matricula}, {self.nome}, {self.idade})"

    
if __name__ == '__main__':
    p1 = Pessoa('Jonas', 21)
    p2 = Pessoa('Marta', 19)
    print(p1)
    print(p2)
