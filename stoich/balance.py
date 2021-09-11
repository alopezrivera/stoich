# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

"""
Stoich balance method
---------------------
"""


import sys
import numpy as np

from stoich.helpers import array


class Balance:

    def __init__(self, r, p):
        self.r = r
        self.p = p

        self.molecules   = array([r.components, p.components])

        self.elements    = np.unique(array([molecule.elements.flatten()[0] for molecule in self.molecules]))

        self.n_elements  = self.elements.size
        self.m_molecules = self.molecules.size

        self.results     = self.balance()

        print(self)

    def __repr__(self):
        return self.latex().replace("\longrightarrow", "->").replace("{", "").replace("}", "")

    def latex(self):
        equilibrium = ""

        # Reactants
        for i in range(self.r.components.size):
            equilibrium += f"{self.results[i]}*{self.r.components[i].__repr__()}" \
            + (" + " if self.r.components.size-1 > i else "")

        equilibrium += " \longrightarrow "

        # Products
        print(self.results)
        for j in range(self.p.components.size):
            equilibrium += f"{self.results[self.r.components.size + j]}*{self.p.components[i].__repr__()}" \
            + (" + " if self.r.components.size-1 > j else "")

        return equilibrium

    def balance(self):
        """
        :return: Solution to the stoichiometric equilibrium in the form Ma = b

        If the system is ill determined (there are more intervening molecules than atoms in the reaction),
        the following happens:

            - If there is 1 more molecule than there are atoms, the quantity of the first reactant is
              set to 1. The system is then solved.
            - If there are more than 1 molecules than there are atoms, the system is ill determined
              and cannot be solved.

        """

        # Balance matrix
        M = np.zeros((self.n_elements, self.m_molecules))
        i = 0
        for mixture in [self.r, self.p]:
            for j in range(mixture.components.size):
                # Molecule
                m = mixture.components[j]
                # Element quantities per molecule in the mixture
                e_qts = array([m.extract_quantity(element) for element in self.elements])\
                        * (1 if mixture == self.r else -1)  # Account for difference between reactants and products
                # Set matrix column
                M[:, i] = array([e_qts[i] for i in range(e_qts.size)])
                i += 1

        # Solution of the linear system
        b       = np.zeros(M.shape[1])
        results = np.zeros(M.shape[1])

        if M.shape[1] - M.shape[0] == 1:
            print("The system is ill determined: there is 1 too many degree of freedom.\n"
                  "The quantity of the first reactant will be automatically set to 1 to remove the inconsistency.")
            b          = -M[:, 0]
            M          = np.delete(M, 0, 1)
            results[0] = 1

        elif M.shape[1] - M.shape[0] > 1:
            sys.exit(f"The system is ill determined: there are {M.shape[1]-M.shape[0]} too many degrees of freedom.")

        results[np.where(results == 0)[0][0]:] = np.linalg.solve(M, b)

        return results
