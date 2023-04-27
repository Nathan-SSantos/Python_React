from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/postgres'
db = SQLAlchemy(app)


class Aluno(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.String(50))
    cpf = db.Column('cpf', db.String(50))
    curso = db.Column('curso', db.String(50))
    periodo = db.Column('periodo', db.String(50)),
    
    def __init__(self, nome, cpf, curso, periodo):
            self.nome = nome
            self.cpf = cpf
            self.curso = curso
            self.periodo = periodo



@app.route('/')
def index():
    alunos = Aluno.query.all()
    alunos = []
    for aluno in alunos:
        aluno_dict = {
            'id': aluno.id,
            'nome': aluno.nome,
            'cpf': aluno.cpf,
            'curso': aluno.curso,
            'periodo': aluno.periodo
        }
        alunos.append(aluno_dict),
    return jsonify(alunos)

@app.route('/add', methods=['POST']) 
 def add():  
  
     nome = request.json.get('nome') 
     cpf = request.json.get('cpf') 
     curso = request.json.get('curso') 
     periodo = request.json.get('periodo') 

  
     aluno = Alunos(nome=nome, cpf=cpf, curso=curso, periodo=periodo) 

     db.session.add(aluno) 
     db.session.commit()



if __name__ == '__main__':
    app.run(debug=True)