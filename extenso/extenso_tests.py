#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from extenso import extenso


class ExtensoTest(unittest.TestCase):
    def test_numero_simples(self):
        self.assertEqual(extenso(1), "um")
        self.assertEqual(extenso(4), "quatro")
        self.assertEqual(extenso(5), "cinco")
        self.assertEqual(extenso(7), "sete")
        self.assertEqual(extenso(20), "vinte")

    def test_dezenas(self):
        self.assertEqual(extenso(11), "onze")
        self.assertEqual(extenso(15), "quinze")
        self.assertEqual(extenso(19), "dezenove")
        self.assertEqual(extenso(20), "vinte")
        self.assertEqual(extenso(30), "trinta")
        self.assertEqual(extenso(90), "noventa")

    def test_numero_composto(self):
        self.assertEqual(extenso(27), "vinte e sete")
        self.assertEqual(extenso(94), "noventa e quatro")

    def test_numero_negativo(self):
        self.assertEqual(extenso(-1), "menos um")
        self.assertEqual(extenso(-13), "menos treze")
        self.assertEqual(extenso(-42), "menos quarenta e dois")

    def test_numero_centenas(self):
        self.assertEqual(extenso(100), "cem")
        self.assertEqual(extenso(124), "cento e vinte e quatro")
        self.assertEqual(extenso(224), "duzentos e vinte e quatro")
        self.assertEqual(extenso(200), "duzentos")
        self.assertEqual(extenso(225), "duzentos e vinte e cinco")
        self.assertEqual(extenso(999), "novecentos e noventa e nove")


if __name__ == '__main__':
    unittest.main()
