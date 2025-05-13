from exercicios04 import calcular_media


def adicionar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):
    dados_alunos = []

    notas = [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": notas,
        "media": calcular_media(notas)
    }
    dados_alunos.append(aluno)
    return dados_alunos

print(adicionar_aluno("Richard", "richard564@gmail.com", "2b série", 10, 10, 10))