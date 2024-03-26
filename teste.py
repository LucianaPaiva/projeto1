from escola.escola_in import Escola
from aluno.aluno_in import Aluno

a1 = Aluno('Jonas', 21, 'Python', 8.5)
a2 = Aluno('Mariana', 19, 'JavaScript', 9.7)
e1 = Escola()
e1.adicionarAlunos(a1)
e1.adicionarAlunos(a2)
print(e1.alunos)
a3 = Aluno ('Jonas Lopes', 31, 'Python', 10)
a3.matricula = 1
e1.editarAluno(a3)
print(e1.alunos)