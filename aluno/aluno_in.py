from aluno.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str, nota: float):
        super().__init__(nome, idade)
        self.curso = curso
        self.nota = nota
    
    def __repr__(self):
        return f"{super().__repr__()}, {self.curso}, {self.nota})"
    
if __name__ == '__main__':
    a1 = Aluno('jonas', 21, 'Python', 8.5)
    print(a1)
