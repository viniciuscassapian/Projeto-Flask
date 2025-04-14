professores = [
    {"id": 1, "nome": "Prof. João", "idade": 40, "materia": "Matematica", "observacoes": "Experiente"},
    {"id": 2, "nome": "Prof. Maria", "idade": 35, "materia": "Historia", "observacoes": "Experiente em história antiga"},
]

def listar_professores():
    return professores

def adicionar_professor(professor):
    professores.append(professor)
    return professor

def buscar_professor(id):
    for p in professores:
        if p['id'] == id:
            return p
    return None

def atualizar_professor(id, dados):
    professor = buscar_professor(id)
    if professor:
        professor.update(dados)
        return professor
    return None

def deletar_professor(id):
    professor = buscar_professor(id)
    if professor:
        professores.remove(professor)
        return True
    return False
