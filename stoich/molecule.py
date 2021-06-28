import numpy as np

from stoich.mixture import Mixture
from stoich.helpers import array


class Molecule:

    def __init__(self, *args):
        """
        :param components: Elements or molecules
        :param quantities: Integer - quantity of each composing element
        """
        self.elements      = array([array(component.elements).flatten() for component in array(args)])
        self.quantities    = array([array(component.quantities).flatten() for component in array(args)])
        self.molecule      = self.formula(np.dstack((self.elements, self.quantities)).squeeze())

    def __sub__(self, other):
        """
        :param other: Another molecule to be composed into a larger molecule
        :return: Composed molecule
        """
        return Molecule(self, other)

    def __mul__(self, other):
        """
        :param other: Real number
        :return: Sets stoichiometric coefficient of molecule, reducing one stoichiometric DOF
        """
        return Molecule(self, other)

    def __rmul__(self, other):
        """
        :param other: Real number
        :return: Sets stoichiometric coefficient of molecule, reducing one stoichiometric DOF
        """
        return Molecule(self, other)

    def __add__(self, other):
        """
        :param other: Another molecule
        :return: Mixture of both molecules
        """
        return Mixture(self, other)

    def formula(self, e_q):
        """
        :param e_q: Elements and their quantities in the molecule
        :return:    Formula of the molecule
        """

        # Element naming formula
        #   Avoid numerical label for n=1 elements: O_1 -> O
        formula_e = lambda element: f"{element[0]}" + "_{" + f"{element[1]}" + "}" \
                                    if int(element[1]) > 1 else \
                                    f"{element[0]}"

        if e_q.ndim == 1:
            # 1 elements, n times
            formula_m = formula_e
        else:
            # m elements, n times
            formula_m = lambda components: "".join([formula_e(element) for element in components])

        return formula_m(e_q)

    def extract_quantity(self, element):
        idx = array(np.where(self.elements == element))
        idx = idx[0] if idx.size > 0 else None
        qty = self.quantities[idx] if not isinstance(idx, type(None)) else 0
        return qty

    def __repr__(self):
        return self.molecule
