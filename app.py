from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = []

@app.route('/alunos', methods=['GET'])
def listar():
    return jsonify(alunos)

@app.route('/add', methods=['POST'])
def add():
    novo_aluno = {
        'cpf': request.json['cpf'],
        'nome': request.json['nome'],
        'curso': request.json['curso'],
        'periodo': request.json['periodo']
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno)

if __name__ == '__main__':
    app.run(debug=True)
