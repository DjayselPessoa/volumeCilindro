ativo = True

while ativo:
    try:
        print("Informe agora os dados para obtenção do volume do cilindro: ")
        raioCilindro = float(input("raio(r) -> "))
        alturaCilindro = float(input("altura(h) -> "))

        volume = (3.14 * (raioCilindro ** 2)) * alturaCilindro
        print(f"Volume do Cilindro: 3.14 * r² * h = {volume}³")

        onOff = str(input("S para sair - C para continuar: "))
        if onOff == "S" or onOff == "s":
            print("Saindo do programa!")
            ativo = False
            # você pode usar o break aq no lugar de mudar pra False
        elif onOff == "C" or onOff == "c":
            print("Reiniciando!")
            ativo = True
        else:
            raise ValueError("Informação não reconhecida! Reiniciando aplicação!")
    except ValueError as e:
        print("Erro", e)
