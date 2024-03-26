from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aluno.aluno_in import Aluno
from escola.escola_in import Escola

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('SysInfinity')

        self.label_matricula = Label(self.janela, text='Matricula', font='Arial 14',
                                     fg='blue')
        self.label_matricula.grid(row=0, column=0)
        
        self.txt_matricula = Entry(self.janela, width=27, font='Tahoma 14', state='readonly')
        self.txt_matricula.grid(row=0, column=1)

        self.label_nome = Label(self.janela, text='Nome', font='Arial 14',
                                     fg='blue')
        self.label_nome.grid(row=1, column=0)
        
        self.txt_nome = Entry(self.janela, width=27, font='Tahoma 14')
        self.txt_nome.grid(row=1, column=1)

        self.label_idade = Label(self.janela, text='Idade', font='Arial 14',
                                     fg='blue')
        self.label_idade.grid(row=2, column=0)
        
        self.txt_idade = Entry(self.janela, width=27, font='Tahoma 14')
        self.txt_idade.grid(row=2, column=1)

        self.label_curso = Label(self.janela, text='Curso', font='Arial 14',
                                     fg='blue')
        self.label_curso.grid(row=3, column=0)

        self.curso = ('Python', 'Java', 'JavaScript', 'Flask', 'Node')
        self.cb_curso = ttk.Combobox(self.janela, width=28, font='Tahoma 12',
                                      values=self.curso)
        self.cb_curso.grid(row=3, column=1)

        self.label_nota = Label(self.janela, text='Nota', font='Arial 14',
                                     fg='blue')
        self.label_nota.grid(row=4, column=0)
        
        self.txt_nota = Entry(self.janela, width=27, font='Tahoma 14')
        self.txt_nota.grid(row=4, column=1)

        self.btn_adcionar = Button(self.janela, font='Tahoma 14', width=27, 
                                   text='Adicionar', fg= 'blue')
        self.btn_adcionar.grid(row=5, column=0)

        self.btn_editar = Button(self.janela, font='Tahoma 14', width=27, 
                                   text='Editar', fg= 'blue')
        self.btn_editar.grid(row=5, column=1)

        self.btn_excluir = Button(self.janela, font='Tahoma 14', width=27, 
                                   text='Excluir', fg= 'blue')
        self.btn_excluir.grid(row=5, column=2)

        self.frame =  Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)
        self.colunas =


        self.janela.mainloop()

App()        