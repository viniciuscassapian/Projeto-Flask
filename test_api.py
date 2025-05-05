import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestAPI(unittest.TestCase):
    def test_get_professores(self):
        response = requests.get(f"{BASE_URL}/professores")
        self.assertEqual(response.status_code, 200)
    
    def test_add_professor(self):
        novo_professor = {"id": 3, "nome": "Prof. Carlos", "idade": 45, "materia": "Física", "observacoes": "Especialista em mecânica"}
        response = requests.post(f"{BASE_URL}/professores", json=novo_professor)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), novo_professor)
    
    def test_add_professor_invalido(self):
        response = requests.post(f"{BASE_URL}/professores", json={"nome": "Prof. Pedro"})
        self.assertEqual(response.status_code, 400)
    
    def test_update_professor(self):
        update_data = {"nome": "Prof. João Silva", "idade": 41}
        requests.post(f"{BASE_URL}/professores", json={"id": 10, "nome": "Prof. Temporário", "idade": 50, "materia": "Biologia", "observacoes": ""})
        response = requests.put(f"{BASE_URL}/professores/10", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["nome"], "Prof. João Silva")
    
    def test_update_professor_inexistente(self):
        response = requests.put(f"{BASE_URL}/professores/99", json={"nome": "Prof. Inexistente"})
        self.assertEqual(response.status_code, 404)
    
    def test_delete_professor(self):
        requests.post(f"{BASE_URL}/professores", json={"id": 11, "nome": "Prof. Deletar", "idade": 38, "materia": "Química", "observacoes": ""})
        response = requests.delete(f"{BASE_URL}/professores/11")
        self.assertEqual(response.status_code, 200)
    
    def test_delete_professor_inexistente(self):
        response = requests.delete(f"{BASE_URL}/professores/99")
        self.assertEqual(response.status_code, 404)

    def test_get_turmas(self):
        response = requests.get(f"{BASE_URL}/turmas")
        self.assertEqual(response.status_code, 200)
    
    def test_add_turma(self):
        nova_turma = {"id": 3, "descricao": "Turma 3C", "professor_id": 1, "ativo": True}
        response = requests.post(f"{BASE_URL}/turmas", json=nova_turma)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), nova_turma)
    
    def test_update_turma(self):
        requests.post(f"{BASE_URL}/turmas", json={"id": 10, "descricao": "Turma Temporária", "professor_id": 1, "ativo": True})
        update_data = {"descricao": "Turma Atualizada"}
        response = requests.put(f"{BASE_URL}/turmas/10", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["descricao"], "Turma Atualizada")
    
    def test_delete_turma(self):
        requests.post(f"{BASE_URL}/turmas", json={"id": 11, "descricao": "Turma Deletar", "professor_id": 1, "ativo": True})
        response = requests.delete(f"{BASE_URL}/turmas/11")
        self.assertEqual(response.status_code, 200)
    
    def test_add_turma_invalida(self):
        response = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma sem professor"})
        self.assertEqual(response.status_code, 400)
    
    def test_update_turma_inexistente(self):
        response = requests.put(f"{BASE_URL}/turmas/99", json={"descricao": "Turma Fantasma"})
        self.assertEqual(response.status_code, 404)
    
    def test_delete_turma_inexistente(self):
        response = requests.delete(f"{BASE_URL}/turmas/99")
        self.assertEqual(response.status_code, 404)

    def test_get_alunos(self):
        response = requests.get(f"{BASE_URL}/alunos")
        self.assertEqual(response.status_code, 200)
    
    def test_add_aluno(self):
        novo_aluno = {
            "id": 3,
            "nome": "Pedro",
            "idade": 14,
            "turma_id": 1,
            "data_nascimento": "2010-05-10",
            "nota_primeiro_semestre": 9,
            "nota_segundo_semestre": 8.5,
            "media_final": 8.75
        }
        response = requests.post(f"{BASE_URL}/alunos", json=novo_aluno)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), novo_aluno)
    
    def test_update_aluno(self):
        requests.post(f"{BASE_URL}/alunos", json={
            "id": 10, "nome": "Aluno Teste", "idade": 13, "turma_id": 1,
            "data_nascimento": "2011-01-01", "nota_primeiro_semestre": 6,
            "nota_segundo_semestre": 7, "media_final": 6.5
        })
        update_data = {"nome": "Aluno Atualizado"}
        response = requests.put(f"{BASE_URL}/alunos/10", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["nome"], "Aluno Atualizado")
    
    def test_delete_aluno(self):
        requests.post(f"{BASE_URL}/alunos", json={
            "id": 11, "nome": "Aluno Deletar", "idade": 15, "turma_id": 1,
            "data_nascimento": "2009-09-09", "nota_primeiro_semestre": 5,
            "nota_segundo_semestre": 6, "media_final": 5.5
        })
        response = requests.delete(f"{BASE_URL}/alunos/11")
        self.assertEqual(response.status_code, 200)
    
    def test_add_aluno_invalido(self):
        response = requests.post(f"{BASE_URL}/alunos", json={"nome": "Aluno sem turma"})
        self.assertEqual(response.status_code, 400)
    
    def test_update_aluno_inexistente(self):
        response = requests.put(f"{BASE_URL}/alunos/99", json={"nome": "Aluno Fantasma"})
        self.assertEqual(response.status_code, 404)
    
    def test_delete_aluno_inexistente(self):
        response = requests.delete(f"{BASE_URL}/alunos/99")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
