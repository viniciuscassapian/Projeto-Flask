from flask import Blueprint, jsonify, request
from models.professor_model import listar_professores, adicionar_professor, atualizar_professor, deletar_professor

professor_bp = Blueprint("professor_bp", __name__)

def validar_dados_professor(professor):
    if not all(k in professor for k in ("id", "nome", "idade", "materia", "observacoes")):
        return False
    return True

@professor_bp.route("/professores", methods=["GET"])
def get_professores():
    return jsonify(listar_professores()), 200

@professor_bp.route("/professores", methods=["POST"])
def add_professor():
    novo = request.json
    if not validar_dados_professor(novo):
        return jsonify({"erro": "Dados inválidos para professor"}), 400
    return jsonify(adicionar_professor(novo)), 201

@professor_bp.route("/professores/<int:id>", methods=["PUT"])
def put_professor(id):
    dados = request.json
    atualizado = atualizar_professor(id, dados)
    if atualizado:
        return jsonify(atualizado), 200
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    if deletar_professor(id):
        return jsonify({"mensagem": "Professor removido"}), 200
    return jsonify({"erro": "Professor não encontrado"}), 404
