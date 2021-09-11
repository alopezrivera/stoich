# SPDX-FileCopyrightText: © 2021 Antonio López Rivera <antonlopezr99@gmail.com>
# SPDX-License-Identifier: GPL-3.0-only

"""
Stoich helper methods
---------------------
"""

import numpy as np


def array(x, **kwargs):
    return np.array(x, **kwargs).flatten()
