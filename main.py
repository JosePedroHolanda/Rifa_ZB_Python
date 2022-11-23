# Função que pega somente números (interos ou flutuantes).
def input_number(self):
    while True:
        getvalue = input(self)
        try:
            float(getvalue)
            return getvalue
            break
        except ValueError:
            print("\33[1;31mSó é aceito números!\33[m")


# Abrir o arquivo
with open("Teste.csv", "r") as arquivo:
    conteudo = arquivo.readlines()


# Variaveis
lista_resultado = []
separacao = []
linha = []
acionador = 0
contador_linha = 0
quantidade_sobra = 0
valor_inicial = 1801
valor_final = 1900
valor_inicial_alterado = valor_inicial
acumulado_sobra = []
quantidade_compra_pessoa = 0
acumulado_compra_total = ""
txt_resultado = ""
apresentacao_acumalado_sobra = ""

# Calculos Basicos
quantidade_sobra = 1 + valor_final - valor_inicial


# Fazer a lista de todos os números
for i in range(quantidade_sobra):
    acumulado_sobra.append(valor_inicial_alterado)
    valor_inicial_alterado += 1


# Pegar o contéudo do arquivo
for linha in conteudo:
    contador_linha += 1
    separacao = linha.split(",")
    nome = separacao[1]
    cpf = separacao[2]
    telefone_1 = separacao[3]
    telefone_2 = separacao[4]
    numero_rifa = separacao[5]
    forma_pagamento = separacao[6]
    link_pix = separacao[7]
    link_pix = link_pix[0:-1]


# Formatar o arquivo para salvar
    acionador = 1
    while acionador == 1:
        if numero_rifa.find(";") == -1:
            acionador = 0
            # Organizar o cabeçalho
            if contador_linha == 1:
                lista_resultado.append('{},{},{},{},{},{},{},{},{},{},{}'.format(nome, cpf, telefone_1, telefone_2, numero_rifa, forma_pagamento, link_pix, "Quantidade compra por pessoa (Acumulado)", "Quantidade sobra (Acumulado)", "Acumulado dos números da rifa", "Acumulado das sobras de rifa"))
            else:
                quantidade_compra_pessoa = 1
                quantidade_sobra -= 1
                acumulado_compra_total = "{};{}".format(acumulado_compra_total, numero_rifa)
                pesquisar = acumulado_sobra.index(int(numero_rifa))
                acumulado_sobra.pop(pesquisar)
                apresentacao_acumalado_sobra = ""
                for a in range(len(acumulado_sobra)):
                    apresentacao_acumalado_sobra = "{}-{}".format(apresentacao_acumalado_sobra, acumulado_sobra[a])
                lista_resultado.append('{},{},{},{},{},{},{},{},{},{},{}'.format(nome, cpf, telefone_1, telefone_2, numero_rifa, forma_pagamento, link_pix, quantidade_compra_pessoa, quantidade_sobra, acumulado_compra_total[1:], apresentacao_acumalado_sobra[1:]))
        else:
            acionador = 0
            lista_numero_rifa = numero_rifa.split(";")
            quantidade_compra_pessoa = 0
            for i in range(len(lista_numero_rifa)):
                quantidade_compra_pessoa += 1
                quantidade_sobra -= 1
                acumulado_compra_total = "{};{}".format(acumulado_compra_total, lista_numero_rifa[i])
                pesquisar = lista_numero_rifa[i]
                pesquisar = acumulado_sobra.index(int(pesquisar))
                acumulado_sobra.pop(int(pesquisar))
                apresentacao_acumalado_sobra = ""
                for a in range(len(acumulado_sobra)):
                    apresentacao_acumalado_sobra = "{}-{}".format(apresentacao_acumalado_sobra,acumulado_sobra[a])
                lista_resultado.append('{},{},{},{},{},{},{},{},{},{},{}'.format(nome, cpf, telefone_1, telefone_2, lista_numero_rifa[i], forma_pagamento, link_pix, quantidade_compra_pessoa, quantidade_sobra, acumulado_compra_total[1:], apresentacao_acumalado_sobra[1:]))
    lista_numero_rifa = []

# Salvar o arquivo
with open("resultado.csv", "w") as resultado:
    nome_vendedor = input("Digite o nome do vendedor: ")
    for i in range(len(lista_resultado)):
        if txt_resultado == "":
            txt_resultado = '{},{}\n'.format("NOME DO VENDEDOR", lista_resultado[i])
        else:
            txt_resultado = '{}{},{}\n'.format(txt_resultado, nome_vendedor, lista_resultado[i])
    resultado.write(txt_resultado)
print("Fim!")
