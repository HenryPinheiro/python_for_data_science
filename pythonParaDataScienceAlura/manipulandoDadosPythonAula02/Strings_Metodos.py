#texto para ser tratado:
texto = ' Geovana Alessandra dias Sanyos '

#O Objetivo é que o nome esteja da seguinte forma: 'GEOVANA ALESSANDRA DIAS SANTOS'

#Texto Maisuculo
print(texto.upper())

#Texto Minusculo
print(texto.strip())

#Alterando
print(texto.replace("y","t"))

#Todas alterações em conjunto
texto = texto.strip().replace("y","t").upper()
print(texto)