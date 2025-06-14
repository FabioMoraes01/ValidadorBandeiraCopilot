def identificar_bandeira(numero):
    """
    Recebe um número de cartão (string ou int) e retorna a bandeira correspondente.
    """
    numero = str(numero)
    if numero.startswith('4'):
        return 'Visa'
    if (numero.startswith(tuple(str(i) for i in range(51, 56))) or
        numero.startswith(tuple(str(i) for i in range(2221, 2721)))):
        return 'MasterCard'
    if (numero.startswith('4011') or numero.startswith('4312') or
        numero.startswith('4389')):
        return 'Elo'
    if numero.startswith('34') or numero.startswith('37'):
        return 'American Express'
    if (numero.startswith('6011') or numero.startswith('65') or
        (numero.startswith('64') and 4 <= int(numero[2:4]) <= 9)):
        return 'Discover'
    if numero.startswith('6062'):
        return 'Hipercard'
    if (numero.startswith('30') or numero.startswith('36') or
        numero.startswith('38')):
        return 'Diners Club'
    if numero.startswith('2014') or numero.startswith('2149'):
        return 'EnRoute'
    if numero.startswith('35'):
        return 'JCB'
    if numero.startswith('86'):
        return 'Voyager'
    if numero.startswith('50'):
        return 'Aura'
    return 'Desconhecida'

def validar_luhn(numero):
    """
    Valida o número do cartão usando o algoritmo de Luhn.
    """
    numero = str(numero).replace(' ', '')
    soma = 0
    invertido = numero[::-1]
    for i, digito in enumerate(invertido):
        n = int(digito)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
    return soma % 10 == 0

if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ").replace(' ', '')
    bandeira = identificar_bandeira(numero)
    valido = validar_luhn(numero)
    print(f"Bandeira: {bandeira}")
    print(f"Válido pelo Luhn: {'Sim' if valido else 'Não'}")