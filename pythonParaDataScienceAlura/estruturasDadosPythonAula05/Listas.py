lista = ["João Antonio", 9.5,9.0,8.0,True]

#Partição, usado para retirar uma parte específica da lista
print(lista[1:4])

#Append: Adiciona um elemento ao final da lista
media = 9.5
lista.append(media)
print(lista)

#Extend, adiciona varios elementos ao final da lista
lista.extend([10.0,8.0,9.0])
print(lista)

#Remove: remove elementos específicos da lista
lista.remove([10.0,8.0,9.0])
print(lista)