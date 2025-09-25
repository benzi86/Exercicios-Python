def decompor_numero():
    while True:
        try:
            numero_str = input("Digite um número entre 0 e 9999: ")
            numero = int(numero_str)

            if 0 <= numero <= 9999:
                # Cálculo das ordens
                unidade = numero % 10
                dezena = (numero // 10) % 10
                centena = (numero // 100) % 10
                milhar = (numero // 1000) % 10

                print(f"Unidade: {unidade}")
                print(f"Dezena: {dezena}")
                print(f"Centena: {centena}")
                print(f"Milhar: {milhar}")
                break  # Sai do loop se o número for válido
            else:
                print("Número inválido. Digite um número entre 0 e 9999.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

decompor_numero()