# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

"""
Stoich element model
--------------------
"""


from stoich.molecule import Molecule


class Element:

    def __init__(self, name):
        self.elements   = name
        self.quantities = 1

    def __mul__(self, other):
        """
        :param other: Integer number
        :return: Molecule composed of n elements
        """
        aux = Element(self.elements)
        aux.quantities = other
        return Molecule(aux)

    def __rmul__(self, other):
        """
        :param other: Integer number
        :return: Molecule composed of n elements
        """
        aux = Element(self.elements)
        aux.quantities = other
        return Molecule(aux)

    def __sub__(self, other):
        """
        :param other: Element or molecule
        :return: Molecule
        """
        return Molecule(self, other)

    def __repr__(self):
        return self.elements
