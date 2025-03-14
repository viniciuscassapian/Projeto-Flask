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
