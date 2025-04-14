from flask import Blueprint, jsonify, request
from models.aluno_model import listar_alunos, adicionar_aluno, atualizar_aluno, deletar_aluno

aluno_bp = Blueprint("aluno_bp", __name__)

def validar_dados_aluno(aluno):
    if not all(k in aluno for k in ("id", "nome", "idade", "turma_id", "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre", "media_final")):
        return False
    return True

@aluno_bp.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(listar_alunos()), 200

@aluno_bp.route("/alunos", methods=["POST"])
def add_aluno():
    novo = request.json
    if not validar_dados_aluno(novo):
        return jsonify({"erro": "Dados inválidos"}), 400
    return jsonify(adicionar_aluno(novo)), 201


@aluno_bp.route("/alunos/<int:id>", methods=["PUT"])
def put_aluno(id):
    dados = request.json
    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    atualizado = atualizar_aluno(id, dados)
    if atualizado:
        return jsonify(atualizado), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404




@aluno_bp.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id):
    if deletar_aluno(id):
        return jsonify({"mensagem": "Aluno removido"}), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404
