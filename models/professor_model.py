from base_de_dados import db

class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text)

    def __repr__(self):
        return f"<Professor {self.nome}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia,
            "observacoes": self.observacoes
        }

def listar_professores():
    return Professor.query.all() 

def adicionar_professor(professor_data):
    professor = Professor(**professor_data)
    db.session.add(professor)
    db.session.commit()
    return professor 

def buscar_professor(id):
    return Professor.query.get(id) 

def atualizar_professor(id, dados):
    professor = buscar_professor(id)
    if professor:
        for key, value in dados.items():
            setattr(professor, key, value) 
        db.session.commit()
        return professor 
    return None

def deletar_professor(id):
    professor = buscar_professor(id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
        return True
    return False
