from flask import Blueprint, jsonify, request
from models.turma_model import listar_turmas, adicionar_turma, atualizar_turma, deletar_turma

turma_bp = Blueprint("turma_bp", __name__)

@turma_bp.route("/turmas", methods=["GET"])
def get_turmas():
    """
    Lista todas as turmas
    ---
    responses:
      200:
        description: Lista de turmas retornada com sucesso
    """
    return jsonify(listar_turmas()), 200

@turma_bp.route("/turmas", methods=["POST"])
def add_turma():
    """
    Adiciona uma nova turma
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
            professor_id:
              type: integer
            ativo:
              type: boolean
    responses:
      201:
        description: Turma adicionada com sucesso
      400:
        description: Dados inválidos para turma
    """
    nova_turma = request.json
    return jsonify(adicionar_turma(nova_turma)), 201

@turma_bp.route("/turmas/<int:id>", methods=["PUT"])
def put_turma(id):
    """
    Atualiza uma turma existente
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
            professor_id:
              type: integer
            ativo:
              type: boolean
    responses:
      200:
        description: Turma atualizada com sucesso
      404:
        description: Turma não encontrada
    """
    dados = request.json
    atualizado = atualizar_turma(id, dados)
    if atualizado:
        return jsonify(atualizado), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route("/turmas/<int:id>", methods=["DELETE"])
def delete_turma(id):
    """
    Deleta uma turma
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Turma removida com sucesso
      404:
        description: Turma não encontrada
    """
    if deletar_turma(id):
        return jsonify({"mensagem": "Turma removida"}), 200
    return jsonify({"erro": "Turma não encontrada"}), 404
