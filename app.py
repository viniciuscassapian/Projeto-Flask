from flask import Flask
from controllers.professor_controller import professor_bp
from controllers.turma_controller import turma_bp
from controllers.aluno_controller import aluno_bp
from config import DEBUG

app = Flask(__name__)
app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)
app.register_blueprint(aluno_bp)

@app.route('/')
def index():
    return 'API Flask funcionando! Acesse os endpoints disponíveis.'

if __name__ == "__main__":
    app.run(debug=DEBUG)
