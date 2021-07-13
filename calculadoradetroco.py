def valorCompra():
    return float(input("Valor Total das Compras: "))


def valorPagamento(totalCompra):
    valido = False
    print (totalCompra)
    while valido == False:
        pagamento = float(input("Valor Recebido: "))
        print (pagamento)
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

def notas(troco):
    print (troco % 50)
    if (troco % 50 != 0):
        numDeNota = int(troco / 50)
        troco = troco - (numDeNota * 50)
        print(f'{numDeNota} Notas: {50}')
    if (troco % 20 != 0):
        numDeNota = int(troco / 20)
        troco = troco - (numDeNota * 20)
        print(f'{numDeNota} Notas: {20}')
    if (troco % 10 != 0):
        numDeNota = int(troco / 10)
        troco = troco - (numDeNota * 10)
        print(f'{numDeNota} Notas: {10}')
    if (troco % 5 != 0):
        numDeNota = int(troco / 5)
        troco = troco - (numDeNota * 5)
        print(f'{numDeNota} Notas: {5}')
    if (troco % 1 != 0):
        numDeNota = int(troco / 1)
        troco = troco - (numDeNota * 1)       
        print(f'{numDeNota} Notas: {1}')         