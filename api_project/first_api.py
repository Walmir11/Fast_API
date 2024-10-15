from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano_publicacao": 1899
    },
    {
        "id": 2,
        "titulo": "O Alienista",
        "autor": "Machado de Assis",
        "ano_publicacao": 1882
    },
    {
        "id": 3,
        "titulo": "Memórias Póstumas de Brás Cubas",
        "autor": "Machado de Assis",
        "ano_publicacao": 1881
    }
]

# consultar todos os livros
@app.route('/livros', methods=['GET'])
def obtar_todos_livros():
    return jsonify(livros)

# consultar um livro pelo id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro['id'] == id:
            return livro
    return None

# editar um livro pelo id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    for livro in livros:
        if livro['id'] == id:
            livro['titulo'] = request.json['titulo']
            livro['autor'] = request.json['autor']
            livro['ano_publicacao'] = request.json['ano_publicacao']
            return livro
    return None

# inserir um livro
@app.route('/livros', methods=['POST'])
def inserir_livro():
    novo_livro = {
        "id": livros[-1]['id'] + 1,
        "titulo": request.json['titulo'],
        "autor": request.json['autor'],
        "ano_publicacao": request.json['ano_publicacao']
    }
    livros.append(novo_livro)
    return jsonify(livros)

# deletar um livro pelo id
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro_por_id(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return jsonify(livros)
    return None

app.run(port=5000,host='localhost',debug=True)
