from flask import Flask
from flasgger import Swagger
from controllers.professor_controller import professor_bp
from controllers.turma_controller import turma_bp
from controllers.aluno_controller import aluno_bp
from base_de_dados import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['HOST'] = '0.0.0.0'
app.config['PORT']=5000
app.config['DEBUG'] = True

app.config['SWAGGER'] = {
    'title': 'API de Gestão Escolar',
    'uiversion': 3
}
swagger = Swagger(app)

db.init_app(app)

app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)
app.register_blueprint(aluno_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'API Flask funcionando! Acesse /apidocs para ver a documentação Swagger.'

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
