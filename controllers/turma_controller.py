from flask import Blueprint, jsonify, request
from models.turma_model import listar_turmas, buscar_turma, adicionar_turma, atualizar_turma, deletar_turma

turma_bp = Blueprint("turma_bp", __name__)

@turma_bp.route("/turmas", methods=["GET"])
def get_turmas():
    """
    Lista todas as turmas
    """
    return jsonify([turma.to_dict() for turma in listar_turmas()]), 200

@turma_bp.route("/turmas/<int:id>", methods=["GET"])
def get_turma_por_id(id):
    turma = buscar_turma(id)
    if turma:
        return jsonify(turma.to_dict()), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route("/turmas", methods=["POST"])
def add_turma():
    nova_turma = request.json
    
    if 'ativo' in nova_turma:
        ativo_val = nova_turma['ativo']
        if isinstance(ativo_val, str):
            nova_turma['ativo'] = ativo_val.lower() in ['sim', 'true', '1']

    turma_obj = adicionar_turma(nova_turma)
    return jsonify(turma_obj.to_dict()), 201

@turma_bp.route("/turmas/<int:id>", methods=["PUT"])
def put_turma(id):
    dados = request.json

    if 'ativo' in dados:
        ativo_val = dados['ativo']
        if isinstance(ativo_val, str):
            dados['ativo'] = ativo_val.lower() in ['sim', 'true', '1']

    atualizado = atualizar_turma(id, dados)
    if atualizado:
        return jsonify(atualizado.to_dict()), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id):
    if deletar_turma(id):
        return jsonify({"mensagem": "Turma removida"}), 200
    return jsonify({"erro": "Turma não encontrada"}), 404
