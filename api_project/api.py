import requests

# 1. O que é uma API?
# Imagine que temos uma API que nos permite acessar informações de usuários.

# 2. APIs REST
# A API REST permite que façamos pedidos de informações ou enviemos dados. Vamos usar a API para obter a lista de usuários.
print("Exemplo de API REST - Pegando lista de usuários: ")
response = requests.get("https://api.exemplo.com/users")
print(response.json())  # Suponha que recebemos uma lista de usuários

# 3. APIs SOAP
# SOAP usa XML para fazer requisições formais. Aqui está como seria uma requisição SOAP.
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
# JSON é mais simples, enquanto XML é mais estruturado. Aqui estão exemplos de cada um.
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
# Vamos imaginar que o endpoint para obter informações de usuários é "https://api.exemplo.com/users".
endpoint = "https://api.exemplo.com/users"
print(f"\nExemplo de Endpoint API: {endpoint}")

# 6. Métodos HTTP
# Vamos fazer requisições GET, POST, PUT e DELETE.
print("\nExemplo de métodos HTTP:")

# GET - Pedindo informações de usuários (equivalente a "quero ver o cardápio")
response = requests.get(endpoint)
print(f"GET - Status: {response.status_code}, Dados: {response.json()}")

# POST - Enviando um novo usuário (equivalente a "quero fazer um pedido")
novo_usuario = {"nome": "Maria", "idade": 30}
response = requests.post(endpoint, json=novo_usuario)
print(f"POST - Status: {response.status_code}, Novo Usuário: {response.json()}")

# PUT - Atualizando um usuário existente (equivalente a "mude o meu pedido")
usuario_atualizado = {"nome": "Maria", "idade": 31}
response = requests.put(endpoint + "/1", json=usuario_atualizado)  # Atualizando o usuário com ID 1
print(f"PUT - Status: {response.status_code}, Usuário Atualizado: {response.json()}")

# DELETE - Apagando um usuário (equivalente a "cancele o meu pedido")
response = requests.delete(endpoint + "/1")  # Deletando o usuário com ID 1
print(f"DELETE - Status: {response.status_code}")

# 7. HTTP Status Codes
# Estes códigos mostram o resultado das requisições. Vamos ver exemplos:
print("\nExemplos de HTTP Status Codes:")
status_codes = {
    200: "Sucesso - Pedido foi feito com sucesso!",
    404: "Erro - Endereço não encontrado.",
    500: "Erro - Algo deu errado no servidor."
}
for code, description in status_codes.items():
    print(f"Status {code}: {description}")

# 8. Authentication and Authorization
# Autenticação: Provando quem você é. Aqui usamos um token para acessar uma área restrita da API.
print("\nExemplo de Autenticação usando Bearer Token:")
headers = {
    "Authorization": "Bearer meu_token_secreto"
}
response = requests.get("https://api.exemplo.com/meus_dados", headers=headers)
print(f"Autenticação - Status: {response.status_code}, Dados: {response.json()}")

# 9. Testing APIs
# Testamos APIs para garantir que estão funcionando corretamente.
print("\nExemplo de Teste de API:")

def test_api_users():
    response = requests.get("https://api.exemplo.com/users")
    assert response.status_code == 200  # Verifica se a resposta foi bem-sucedida (200 OK)
    print("Teste passou! A API de usuários está funcionando.")

# Executa o teste
test_api_users()

