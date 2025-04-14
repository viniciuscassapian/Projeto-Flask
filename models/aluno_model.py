alunos = [
    {"id": 1, "nome": "Ana", "idade": 14, "turma_id": 1, "data_nascimento": "2010-05-14", "nt_prim_sem": 8.5, "nt_seg_sem": 9.0, "media_final": 8.75},
    {"id": 2, "nome": "Bruno", "idade": 15, "turma_id": 2, "data_nascimento": "2009-08-22", "nota_primeiro_semestre": 7.0, "nota_segundo_semestre": 6.5, "media_final": 6.75}
]

def listar_alunos():
    return alunos

def adicionar_aluno(aluno):
    alunos.append(aluno)
    return aluno

def buscar_aluno(id):
    for a in alunos:
        if a['id'] == id:
            return a
    return None

def atualizar_aluno(id, dados):
    aluno = buscar_aluno(id)
    if aluno:
        aluno.update(dados)
        return aluno
    return None

def deletar_aluno(id):
    aluno = buscar_aluno(id)
    if aluno:
        alunos.remove(aluno)
        return True
    return False
