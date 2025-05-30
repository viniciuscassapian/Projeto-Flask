from base_de_dados import db

class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Turma {self.descricao}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo
        }

def listar_turmas():
    return Turma.query.all()

def adicionar_turma(turma_data):
    turma = Turma(**turma_data)
    db.session.add(turma)
    db.session.commit()
    return turma

def buscar_turma(id):
    return Turma.query.get(id)

def atualizar_turma(id, dados):
    turma = buscar_turma(id)
    if turma:
        for key, value in dados.items():
            setattr(turma, key, value)
        db.session.commit()
        return turma
    return None

def deletar_turma(id):
    turma = buscar_turma(id)
    if turma:
        db.session.delete(turma)
        db.session.commit()
        return True
    return False
