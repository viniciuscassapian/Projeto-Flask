from base_de_dados import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Aluno {self.nome}>"

def listar_alunos():
    return Aluno.query.all()

def adicionar_aluno(aluno_data):
    aluno = Aluno(**aluno_data)
    db.session.add(aluno)
    db.session.commit()
    return aluno

def buscar_aluno(id):
    return Aluno.query.get(id)

def atualizar_aluno(id, dados):
    aluno = buscar_aluno(id)
    if aluno:
        for key, value in dados.items():
            setattr(aluno, key, value)
        db.session.commit()
        return aluno
    return None

def deletar_aluno(id):
    aluno = buscar_aluno(id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        return True
    return False
