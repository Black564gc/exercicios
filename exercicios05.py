
def adicionar_aluno(nome, email, serie):
    dados_alunos = []  
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie
    }
    dados_alunos.append(aluno)
    return dados_alunos

print(adicionar_aluno("Richard", "richard564@gmail.com", "2b série"))