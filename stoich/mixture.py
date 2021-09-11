# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

"""
Stoich mixture model
--------------------
"""


from stoich.balance import Balance

from stoich.helpers import array


class Mixture:

    def __init__(self, *args):
        """
        :param molecules: Create a mixture composed of n molecules
        """
        self.components = array(args)

    def __rshift__(self, other):
        """
        :param other: Product mixture
        :return: Balanced reaction
        """
        return Balance(self, other)
