# Stoich: a simple stoichiometry library in Python

![alt text](tests/coverage/coverage.svg ".coverage available in tests/coverage/")

Library to solve stoichiometric balance problems with a concise and familiar syntax.

---

[ 1. Install ](#1-install)

[ 2. Usage and Syntax ](#2-usage-and-syntax)

## 1. Install

Download `/stoich` to your project folder and

    from element import Element

## 2. Usage and Syntax

The best way to appreciate the syntax is to see it in action. The following is an example with the combustion of Octane.

Firstly, create a series of elements:

    H = Element("H")
    O = Element("O")
    C = Element("C")

The necessary molecules can be created straightforwardly from the elements, as follows:

    C8H18 = C*8-H*18
    O2    = O*2
    CO2   = C-O*2
    H20   = H*2-O

The molecule creation syntax works as follows:

- Multiplication
    - By Integer: single-species molecule (do not mistake for monoatomic)
- Subtraction
    - By Element: diatomic molecule
    - By Molecule: composed molecule

Once the molecules have been created, a mixture can be obtained from different molecules:

    reactants = C8H18 + O2
    products  = CO2 + H20

Finally, the stoichiometric balance can be formulated and the coefficients solved for:

    reactants >> products

The balanced stoichiometric equilibrium will be displayed in the terminal as follows:

    1.0*C_8H_18 + 12.5*O_2 -> 8.0*H_2O + 9.0*H_2O

_Note: as an avid chemist might have told, in this equilibrium there is one too many degrees of freedom (ie: there is one more molecule than there are atoms to conduct a balance with): the system is ill determined!_ A solution is found in this case however, as follows:

- If there is 1 molecule more than there are atoms, the stoichiometric coefficient of the first reactant (C8H18 in this case) is set to 1, and the system is solved.
- If there are more than 1 molecules more than there are atoms in the balance, the system cannot be solved and the program will stop.

Lastly, the balance can be output direcly in LaTeX code, by calling

    balance = reactants >> products

    print(balance.latex())

Which will output

    1.0*C_{8}H_{18} + 12.5*O_{2} \longrightarrow 8.0*H_{2}O + 9.0*H_{2}O

Which is to say:

![alt text](demo/octane_stoich_latex.png "Octane combustion stoichiometric equilibrium")
