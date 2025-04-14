turmas = [
    {"id": 1, "descricao": "Turma 1A", "professor_id": 1, "ativo": True},
    {"id": 2, "descricao": "Turma 2B", "professor_id": 2, "ativo": True}
]

def listar_turmas():
    return turmas

def adicionar_turma(turma):
    turmas.append(turma)
    return turma

def buscar_turma(id):
    for t in turmas:
        if t['id'] == id:
            return t
    return None

def atualizar_turma(id, dados):
    turma = buscar_turma(id)
    if turma:
        turma.update(dados)
        return turma
    return None

def deletar_turma(id):
    turma = buscar_turma(id)
    if turma:
        turmas.remove(turma)
        return True
    return False
