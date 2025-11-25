#Interface do Menu:
print("-"*9, end=" ")
print("Bem-vindo a Loja de Marmitas do Ytalo Gabriel", end=" ")
print("-"*9)
print("-"*27, end="-")
print("Cardápio", end="-")
print("-"*28)
print("-"*65)
print("---|  Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |---")
print("---|     P     |       R$16.00        |       R$15.00        |---")
print("---|     M     |       R$18.00        |       R$17.00        |---")
print("---|     G     |       R$22.00        |       R$21.00        |---")
print("-"*65)

pedirmais = "S" #Variável de prosseguir ou finalizar o pedido:
valorMarm = 0   #Variável do valor da marmita solicitada:
nomePrato = 0   #Nome do prato sem siglas:
valorTotal = 0  #Variável do valor total do pedido:

while pedirmais == "S":
    sabor = input("Qual o sabor desejado (BA/FF): ").strip().upper()
    if sabor not in ("BA", "FF"):
        print("Sabor inválido. Tente novamente\n")
        continue
    else:
        if sabor == "BA":                     #Transformando siglas no nome do prato
            nomePrato = "Bife Acebolado"
        elif sabor == "FF":
            nomePrato = "Filé de Frango"

    # Escolha do tamanho da marmita
    tamanho = input("Qual o tamanho desejado (P/M/G): ").strip().upper()
    if tamanho not in ("P", "M", "G"):      #Validação para inserir tamanho correto
        print("Tamanho inválido. Tente novamente\n")
        continue
    else:
        # Tabela de valores das marmitas de acordo com as combinações
        if sabor == "BA":
            if tamanho == "P":
                valorMarm = 16.00
            elif tamanho == "M":
                valorMarm = 18.00
            elif tamanho == "G":
                valorMarm = 22.00
        elif sabor == "FF":
            if tamanho == "P":
                valorMarm = 15.00
            elif tamanho == "M":
                valorMarm = 17.00
            elif tamanho == "G":
                valorMarm = 21.00

    valorTotal += valorMarm           #Acumulador de soma dos valores do pedido
    print(f"Você pediu um {nomePrato} no tamanho {tamanho}: R${valorMarm:.2f}\n")

    #Pergunta para continuar ou encerrar o pedido
    pedirmais = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()
    while pedirmais not in ("S", "N"):       #Validação para inserir siglas corretas
        pedirmais = input("Responda inválida, Deseja pedir mais alguma coisa? (S/N): ").strip().upper()

    if pedirmais == "N":      #Encerrar lógica quando for inserido "N" como resposta
        break
print(f"\nO valor total a ser pago: R${valorTotal:.2f}")