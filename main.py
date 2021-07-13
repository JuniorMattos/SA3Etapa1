import calculadoradetroco

totalCompra = calculadoradetroco.valorCompra()

pagamento = calculadoradetroco.valorPagamento(totalCompra)

troco = calculadoradetroco.valorTroco(totalCompra, pagamento)

calculadoradetroco.notas(troco)
