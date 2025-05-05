from flask import Blueprint, jsonify, request
from models.aluno_model import listar_alunos, adicionar_aluno, atualizar_aluno, deletar_aluno

aluno_bp = Blueprint("aluno_bp", __name__)

@aluno_bp.route("/alunos", methods=["GET"])
def get_alunos():
    """
    Lista todos os alunos
    ---
    responses:
      200:
        description: Lista de alunos retornada com sucesso
    """
    return jsonify(listar_alunos()), 200

@aluno_bp.route("/alunos", methods=["POST"])
def add_aluno():
    """
    Adiciona um novo aluno
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
            turma_id:
              type: integer
            data_nascimento:
              type: string
              format: date
            nota_primeiro_semestre:
              type: number
            nota_segundo_semestre:
              type: number
            media_final:
              type: number
    responses:
      201:
        description: Aluno adicionado com sucesso
      400:
        description: Dados inválidos
    """
    novo = request.json
    return jsonify(adicionar_aluno(novo)), 201

@aluno_bp.route("/alunos/<int:id>", methods=["PUT"])
def put_aluno(id):
    """
    Atualiza um aluno existente
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
            turma_id:
              type: integer
            data_nascimento:
              type: string
              format: date
            nota_primeiro_semestre:
              type: number
            nota_segundo_semestre:
              type: number
            media_final:
              type: number
    responses:
      200:
        description: Aluno atualizado com sucesso
      404:
        description: Aluno não encontrado
    """
    dados = request.json
    atualizado = atualizar_aluno(id, dados)
    if atualizado:
        return jsonify(atualizado), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404

@aluno_bp.route("/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id):
    """
    Deleta um aluno
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Aluno removido com sucesso
      404:
        description: Aluno não encontrado
    """
    if deletar_aluno(id):
        return jsonify({"mensagem": "Aluno removido"}), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404
