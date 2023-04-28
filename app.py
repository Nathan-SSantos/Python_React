from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/pool'
db = SQLAlchemy(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

class Aluin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(50), unique=True)
    curso = db.Column(db.String(50))
    periodo = db.Column(db.String(50))
    
    def _init_(self, nome, cpf, curso, periodo):
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.periodo = periodo


@app.route('/')
def index():
    alunos = Aluin.query.all()
    alunos_list = []
    for aluno in alunos:
        aluno_dict = {
            'id': aluno.id,
            'nome': aluno.nome,
            'cpf': aluno.cpf,
            'curso': aluno.curso,
            'periodo': aluno.periodo
        }
        alunos_list.append(aluno_dict)
    return jsonify(alunos_list)


@app.route('/alunos', methods=['POST'])
def create_aluno():
    nome = request.json.get('nome')
    cpf = request.json.get('cpf')
    curso = request.json.get('curso')
    periodo = request.json.get('periodo')

    aluno = Aluin(nome=nome, cpf=cpf, curso=curso, periodo=periodo)
    db.session.add(aluno)
    db.session.commit()

    return jsonify({
        'id': aluno.id,
        'nome': aluno.nome,
        'cpf': aluno.cpf,
        'curso': aluno.curso,
        'periodo': aluno.periodo
    }), 201


if _name_ == '_main_':
    app.run(debug=True)
