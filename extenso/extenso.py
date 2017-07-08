#!/usr/bin/env python
# -*- coding: utf-8 -*-


def extenso(numero):
    if (numero < 0):
        return 'menos ' + extenso(-numero)

    unidades = [
        "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
        "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove"
    ]

    dezenas = [
        '_NOTUSED_', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
        'setenta', 'oitenta', 'noventa'
    ]

    centenas = [
        'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
        'seiscentos', 'setecentos', 'oitocentos', 'novecentos'
    ]

    if numero < 20:
        return unidades[numero]
    elif numero == 100:
        return "cem"
    elif numero < 100:
        result = dezenas[numero // 10 - 1]
        if numero % 10 != 0:
            result += ' e ' + extenso(numero % 10)
        return result
    elif numero < 1000:
        result = centenas[numero // 100 - 1]
        if numero % 100 != 0:
            result += ' e ' + extenso(numero % 100)
        return result
    else:
        raise ValueError("Valor %s nao suportado" % numero)
