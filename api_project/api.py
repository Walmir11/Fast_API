import requests

# 1. O que é uma API?
# API (Interface de Programação de Aplicações) é um conjunto de definições e protocolos que permite a comunicação entre diferentes sistemas de software.
# Elas permitem que aplicações acessem dados ou funcionalidades de outros serviços.

# 2. APIs REST
# REST (Representational State Transfer) é um estilo de arquitetura que usa métodos HTTP para realizar operações em recursos, são simples, escaláveis.
print("Exemplo de API REST - Pegando lista de usuários:")
response = requests.get("https://api.exemplo.com/users")
print(response.json())  # Suponha que recebemos uma lista de usuários

# 3. APIs SOAP
# SOAP (Simple Object Access Protocol) é um protocolo baseado em XML para troca de informações estruturadas em uma rede descentralizada e distribuída.
print("\nExemplo de API SOAP (requisição usando XML):")
soap_request = """
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetUserInfo xmlns="http://api.exemplo.com/">
      <UserID>123</UserID>
    </GetUserInfo>
  </soap:Body>
</soap:Envelope>
"""
print(soap_request)

# 4. JSON e XML
# JSON (JavaScript Object Notation) é um formato leve de troca de dados, fácil de ler e escrever para humanos e fácil de analisar e gerar para máquinas.
# XML (eXtensible Markup Language) é um formato de dados mais estruturado e flexível, mas mais verboso que JSON.
print("\nExemplo de JSON:")
json_data = {
    "nome": "João",
    "idade": 25
}
print(json_data)

print("\nExemplo de XML:")
xml_data = """
<pessoa>
    <nome>João</nome>
    <idade>25</idade>
</pessoa>
"""
print(xml_data)

# 5. Endpoints API
# Endpoint é a URL onde a API está disponível. É o ponto de acesso para interagir com a API.
# Endpoint para informações de usuários
endpoint = "https://api.exemplo.com/users"
print(f"\nExemplo de Endpoint API: {endpoint}")

# 6. Métodos HTTP
# Métodos HTTP são usados para realizar diferentes operações em recursos da API.
# Os métodos mais comuns são GET, POST, PUT e DELETE.
print("\nExemplo de métodos HTTP:")

# GET - Pedir informações
response = requests.get(endpoint)
print(f"GET - Status: {response.status_code}, Dados: {response.json()}")

# POST - Enviar informações para criar
novo_usuario = {"nome": "Maria", "idade": 30}
response = requests.post(endpoint, json=novo_usuario)
print(f"POST - Status: {response.status_code}, Novo Usuário: {response.json()}")

# PUT - Atualizando um dado existente
usuario_atualizado = {"nome": "Maria", "idade": 31}
response = requests.put(endpoint + "/1", json=usuario_atualizado)  # Atualizando o usuário com ID 1
print(f"PUT - Status: {response.status_code}, Usuário Atualizado: {response.json()}")

# DELETE - Apagando um dado
response = requests.delete(endpoint + "/1")  # Deletando o usuário com ID 1
print(f"DELETE - Status: {response.status_code}")

# 7. HTTP Status Codes
# Códigos de status HTTP indicam o resultado das requisições.
# Por exemplo, 200 significa sucesso, 404 significa que o recurso não foi encontrado, e 500 indica um erro no servidor.
print("\nExemplos de HTTP Status Codes:")
status_codes = {
    200: "Sucesso - Pedido foi feito com sucesso!",
    404: "Erro - Endereço não encontrado.",
    500: "Erro - Algo deu errado no servidor."
}

# 8. Authentication and Authorization
# Autenticação é o processo de verificar a identidade de um usuário ou sistema.
# Autorização é o processo de verificar se o usuário ou sistema tem permissão para acessar um recurso.
# Aqui usamos um token para acessar uma área restrita da API.
print("\nExemplo de Autenticação usando Bearer Token:")
headers = {
    "Authorization": "Bearer meu_token_secreto"
}
response = requests.get("https://api.exemplo.com/meus_dados", headers=headers)
print(f"Autenticação - Status: {response.status_code}, Dados: {response.json()}")
