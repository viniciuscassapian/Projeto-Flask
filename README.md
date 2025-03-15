from flask import Flask, jsonify, request
from data import professores, turmas, alunos

app = Flask(__name__)

professores = [
    {"id": 1, "nome": "Prof. João", "idade": 40, "materia": "Matematica", "observacoes": "Experiente"},
    {"id": 1, "nome": "Prof. Maria", "idade": 35, "materia": "Historia", "observacoes": "Experiente em história antiga"},
]

turmas = [
    {"id": 1, "descricao": "Turma 1A", "professor_id": 1, "ativo": True},
    {"id": 2, "descricao": "Turma 2B", "professor_id": 2, "ativo": True}
]

alunos = [
    {"id": 1, "nome": "Ana", "idade": 14, "turma_id": 1, "data_nascimento": "2010-05-14", "nt_prim_sem": 8.5, "nt_seg_sem": 9.0, "media_final": 8.75},
    {"id": 2, "nome": "Bruno", "idade": 15, "turma_id": 2, "data_nascimento": "2009-08-22", "nota_primeiro_semestre": 7.0, "nota_segundo_semestre": 6.5, "media_final": 6.75}
]   
# Essa parte é o CRUD dos professores
# Esse GET serve para retornar a lista de professores
@app.route('/professores', methods = ['GET'])
def get_professores():
    return jsonify(professores), 200
# O POST vai adicionar um novo professor
@app.route('/professores', methods=['POST'])
def add_professor():
    novo_professor = request.json
    professores.append(novo_professor), 201
# O PUT vai servir para atualizar um professor que já existe
app.route('/professores/<int:id>', methods =['PUT'])
def update_professor(id):
    for professor in professores:
        dados = request.json
        professor.update(dados)
        return jsonify(professor), 200
    return jsonify({"erro": "Professor não encontrado"}), 404
# O DELETE vai servir para deletar/remover um professor
@app.route('/professores/<int:id>', methods = ['DELETE'])
def deletar_professor(id):
    for professor in professores:
        if professor['id'] == id:
            professores.remove(professor)
            return jsonify({"mensagem": "Professor removido"}), 200
        return jsonify({"erro": "Professor não encontrado"}), 404
# Essa é a parte do CRUD das turmas
# Esse é o GET das turmas
@app.route('/turmas', methods = ['GET'])
def get_turmas():
    return jsonify(turmas), 200
# O POST das turmas
@app.route('/turmas', methods = ['POST'])
def add_turma():
    nova_turma = request.json
    turmas.append(nova_turma)
    return jsonify(nova_turma), 201
# Esse é o PUT das turmas
@app.route('/turmas/<int:id>', methods = ['PUT'])
def update_turma(id):
    for turma in turmas:
        if turma ['id'] == id:
            dados = request.json
            turma.update(dados)
            return jsonify(turma), 200
        return jsonify({"erro": "Turma não encontrada"}), 404
# Esse é o DELETE das turmas
@app.route('/turmas/<int:id>', methods = ['DELETE'])
def deletar_turmas(id):
    for turma in turmas:
        if turma ['id'] == id:
            turmas.remove(turma)
            return jsonify({"mensagem": "Turma removida"}), 200
        return jsonify({"erro": "Turma não encontrada"}), 404
# Esse é o CRUD dos alunos
# #Esse é o GET dos alunos
app.route('/alunos', methods = ['GET'])
def get_alunos():
    return jsonify(alunos), 200
# Esse é o POST dos alunos
app.route('/alunos', methods = ['POST'])
def add_aluno():
    novo_aluno = request.json
    alunos.append(novo_aluno)
    return jsonify(alunos), 201
# Esse é PUT dos alunos
app.route('/alunos/<int:id>', methods = ['PUT'])
def update_aluno(id):
    for aluno in alunos:
        if aluno ['id'] == id:
            dados = request.json
            aluno.update(dados)
            return jsonify(aluno), 200
        return jsonify({"erro": "Aluno não encontrado"}), 404
# Esse é o DELETE dos alunos
app.route('/alunos/<int:id>', methods = ['DELETE'])
def deletar_aluno(id):
    for aluno in alunos:
        if alunos['id'] == id:
            alunos.remove(aluno)
            return jsonify({'mensagem': "Aluno removido"}), 200
        return jsonify({"erro": "Aluno não encontrado"})
