#Criação de um dicionário
cadastro = {"matricula": 2000168933,"dia_cadastro": 25,"mes_cadastro": 10,"turma": "2E"}
print(cadastro["turma"])

#Chamando uma chave específica
cadastro["turma"] = "2G"
print(cadastro["turma"])

#Adicionando uma nova chave
cadastro["modalidade"] = "EAD"
print(cadastro)

#POP: remove um item do dicionário
cadastro.pop("turma")
print(cadastro)

#items: retorna uma lista de pares chaves-valor do dicionário
print(cadastro.items())

#Keys: Retorna todas as chaves do dicionário
print(cadastro.keys())

#Values: Retorna todas os valores do dicionário
print(cadastro.values())
