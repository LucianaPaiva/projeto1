from aluno.aluno_in import Aluno
class Escola:
    def __init__(self):
        self.alunos = []

    def adicionarAlunos(self, aluno: Aluno):
        self.alunos.append(aluno)

    def editarAluno(self, aluno: Aluno):
        for alu in self.alunos:
            if alu.matricula == aluno.matricula:
                alu.nome = aluno.nome
                alu.idade = aluno.idade
                alu.curso = aluno.curso
                alu.nota = aluno.nota
                return alu
        return None
    
if __name__=='__main__':
    a1 = Aluno('Jonas', 21, 'Python', 8.5)
    a2 = Aluno('Mariana', 19, 'JavaScript', 9.7)
    e1 = Escola()
    e1.adicionarAlunos(a1)
    e1.adicionarAlunos(a2)
    print(e1.alunos)



