def valorCompra():

    return float(input("Valor Total das Compras: "))


def valorPagamento(totalCompra):
    
    valido = False
    
    while valido == False:
        
        pagamento = float(input("Valor Recebido: "))

        valido = validarPagamneto(totalCompra, pagamento)
        
    return pagamento

def validarPagamneto(total, pgt):

    if total > pgt:
    
        print("Valor Recebido Inválido!!!")
        return False

    else:
        
        return True

def valorTroco(totalCompra, pagamento):

    troco = float(pagamento - totalCompra)
    return troco

def quantidadeDeTroco(troco):
    
    if troco > 1:

        print ('-' * 50)
        print (f'Quantidade Minima de Notas de Troco - R$ {troco}')
        print ('-' * 50)

        for n in (50, 20, 10, 5, 1):

            numDeNota = int(troco / n)
            troco = round(troco - (numDeNota * n), 2)
            print(f'{numDeNota} Notas: {n}')

    if troco < 1:
        
        print ('-' * 50)
        print (f'Quantidade Minima de Moedas de Troco - R$ {troco}')
        print ('-' * 50)

        for i in (0.50, 0.25, 0.10, 0.05, 0.01):
        
            numDeMoeda = int(troco / i)
            troco = round(troco - (numDeMoeda * i), 2)
            print(f'{numDeMoeda} Moedas: {i}')


def menu():
    
    print ('-' * 50)
    print ('CALCULADORA DE TROCO')
    print ('-' * 50)
    
    totalCompra = valorCompra()

    pagamento = valorPagamento(totalCompra)

    troco = valorTroco(totalCompra, pagamento)

    print (f'Troco: {troco}')

    quantidadeDeTroco(troco)

    print ('-' * 50)