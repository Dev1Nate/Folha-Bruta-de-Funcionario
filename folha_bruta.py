#valor_porcentagem = valor * (percentual / 100)

valor = float(input('Digite quanto ganha por hora: '))
horas = float(input('Digite o numero de horas trabalhas: '))

def folha_de_pagamento(valor,horas):
    salario_bruto = valor * horas
    while True:
        imposto_de_renda = str(input("Paga Imposto de Renda?\n Digite Sim ou Não: "))
        if imposto_de_renda.lower() == "sim":
            IR = salario_bruto * (11 / 100)
            break
        elif imposto_de_renda.lower() == 'nao' or imposto_de_renda.lower() == 'não':
            IR = 0
            break
        else:
            print('Resposta invalida')
            continue
        
    
    INSS = salario_bruto * (8 / 100)

    descontos = INSS + IR
    while True:
        pergunta = str(input("recebe algum Desconto Alem do Inss?\n Digite Sim ou Não: "))
        if pergunta.lower() == "sim":
            outros = float(input("Qual o Valor do Desconto em % (*PORCENTAGEM/100):"))
            descontos += salario_bruto * (outros/100)
            break
        elif pergunta.lower() == 'nao' or  pergunta.lower() == 'não':
            outros = "Não Possui Outros Descontos"
            break
        print('Resposta invalida')
        continue
    if isinstance(outros,str):
        desconto_extras = 0
    elif isinstance(outros,(int,float)):
        desconto_extras = salario_bruto * (outros / 100)
    salario_liquido = salario_bruto - descontos
    return print(f' + Salário Bruto : R$ {salario_bruto:.2f}\n'
               f' - IR (11%) : R$ {IR:.2f}\n'
               f' - INSS (8%) : R$ {INSS:.2f}\n'
               f' - Outros ({outros}) : R$ {desconto_extras:.2f} \n'
               f' = Salário Liquido : R$ {salario_liquido:.2f}')
folha_de_pagamento(valor, horas)