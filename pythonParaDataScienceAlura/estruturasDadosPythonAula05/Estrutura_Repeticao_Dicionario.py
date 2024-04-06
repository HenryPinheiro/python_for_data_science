cadastro = {"matricula": 2000168933,"dia_cadastro": 25,"mes_cadastro": 10,"turma": "2E"}

for chaves in cadastro.keys():
    print(cadastro[chaves])

for valores in cadastro.values():
    print(valores)

for chaves, valores in cadastro.items():
    print(f"{chaves} --- {valores}")