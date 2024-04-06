contador = 1

while contador <= 3:
    print(f"Digite as notas do {contador} Aluno")
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))

    print(f'Média: {(nota_1 + nota_2) / 2}')
    contador = contador+1



for contador in range(1,4):
    print(f"Digite as notas do {contador} Aluno")
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))

    print(f'Média: {(nota_1 + nota_2) / 2}')
    contador = contador + 1