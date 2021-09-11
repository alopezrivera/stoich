# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

import unittest

from stoich.element import Element


# Elements
H = Element("H")
O = Element("O")
C = Element("C")


class TestCombustion(unittest.TestCase):

    def test_molecules(self):
        # Molecules
        O2    = O*2
        H20   = H*2-O
        CO2   = C-O*2
        C8H18 = C*8-H*18

        return O2, H20, CO2, C8H18


    def test_mixture(self):
        O2, H20, CO2, C8H18 = self.test_molecules()

        # Mixtures
        reactants = C8H18 + O2
        products = CO2 + H20

        return reactants, products


    def test_balance(self):
        reactants, products = self.test_mixture()

        # Balance
        balance = reactants >> products

        print(balance.latex())