from flask import Blueprint, jsonify, request
from models.turma_model import listar_turmas, adicionar_turma, atualizar_turma, deletar_turma

turma_bp = Blueprint("turma_bp", __name__)

def validar_dados_turma(turma):
    if not all(k in turma for k in ("id", "descricao", "professor_id", "ativo")):
        return False
    return True

@turma_bp.route("/turmas", methods=["GET"])
def get_turmas():
    return jsonify(listar_turmas()), 200

@turma_bp.route("/turmas", methods=["POST"])
def add_turma():
    nova_turma = request.json
    if not validar_dados_turma(nova_turma):
        return jsonify({"erro": "Dados inválidos para turma"}), 400
    return jsonify(adicionar_turma(nova_turma)), 201

@turma_bp.route("/turmas/<int:id>", methods=["PUT"])
def put_turma(id):
    dados = request.json
    atualizado = atualizar_turma(id, dados)
    if atualizado:
        return jsonify(atualizado), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id):
    if deletar_turma(id):
        return jsonify({"mensagem": "Turma removida"}), 200
    return jsonify({"erro": "Turma não encontrada"}), 404
