from flask import Blueprint, jsonify, request
from models.professor_model import listar_professores, adicionar_professor, atualizar_professor, deletar_professor

professor_bp = Blueprint("professor_bp", __name__)

@professor_bp.route("/professores", methods=["GET"])
def get_professores():
    """
    Lista todos os professores
    ---
    responses:
      200:
        description: Lista de professores retornada com sucesso
    """
    return jsonify(listar_professores()), 200

@professor_bp.route("/professores", methods=["POST"])
def add_professor():
    """
    Adiciona um novo professor
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            idade:
              type: integer
            materia:
              type: string
            observacoes:
              type: string
    responses:
      201:
        description: Professor adicionado com sucesso
      400:
        description: Dados inválidos
    """
    novo = request.json
    return jsonify(adicionar_professor(novo)), 201

@professor_bp.route("/professores/<int:id>", methods=["PUT"])
def put_professor(id):
    """
    Atualiza um professor existente
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
            nome:
              type: string
            idade:
              type: integer
            materia:
              type: string
            observacoes:
              type: string
    responses:
      200:
        description: Professor atualizado com sucesso
      404:
        description: Professor não encontrado
    """
    dados = request.json
    atualizado = atualizar_professor(id, dados)
    if atualizado:
        return jsonify(atualizado), 200
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    """
    Deleta um professor
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Professor deletado com sucesso
      404:
        description: Professor não encontrado
    """
    if deletar_professor(id):
        return jsonify({"mensagem": "Professor removido"}), 200
    return jsonify({"erro": "Professor não encontrado"}), 404
