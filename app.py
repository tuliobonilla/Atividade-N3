from flask import Flask, request, jsonify
from estudante import Estudante

#indicando qua a aplicaçao vai ser flask
app = Flask(__name__)

estudante = Estudante()

#mapear o recurso
@app.route("/")
def contextoApp():
    return "Bem Vindo ao CRUD Estudante"

#post para cadastrar
@app.route(f"/estudantes/cadastrar", methods=['POST'])
def cadastrarEstudante():
    nome = request.args.get('nome')
    matricula = request.args.get('matricula')
    try:
        return estudante.cadastrar(nome, matricula)
    except Exception as e:
        return str(e)
    return

#get para consultar
@app.route("/estudantes/consultar", methods=['GET'])
def consultarEstudante():
    estudantes = estudante.consultar()
    return jsonify(estudantes)

#put para editar
@app.route(f"/estudantes/editar", methods=['PUT'])
def editarEstudante():
    nome = request.args.get('nome')
    matricula = request.args.get('matricula')
    try:
        return estudante.editar(nome, matricula)
    except Exception as e:
        return str(e)
    return

#delete para remover
@app.route(f"/estudantes/remover", methods=['DELETE'])
def removerEstudante():
    matricula = request.args.get('matricula')
    try:
        return estudante.remover(matricula)
    except Exception as e:
        return str(e)
    return

if __name__ == '__main__':
    app.run(debug=True)