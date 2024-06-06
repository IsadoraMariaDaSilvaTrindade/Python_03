a = int(input("quantidade: "))
lista = []
inf = 2454545454

for i in range( a):
    nome = input("Digite o nome: ")
    nome = nome.capitalize()
    if nome in lista:
        for i in range(inf):
            if nome in lista:
                nome =  input(f"Nome {nome} já esta na lista digite novamente")
                nome = nome.capitalize() 
            else:
                lista.append(nome)
                break
        else:
            lista.append(nome)
    print(lista)

