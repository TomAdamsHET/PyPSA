# -*- coding: utf-8 -*-
"""
Python for Power Systems Analysis (PyPSA)

Energy system modelling library.
"""

from pypsa import (
    clustering,
    components,
    contingency,
    descriptors,
    examples,
    geo,
    io,
    linopf,
    linopt,
    opf,
    opt,
    optimization,
    pf,
    plot,
    statistics,
)
from pypsa.components import Network, SubNetwork

__version__ = "0.26.0"

__author__ = (
    "PyPSA Developers, see https://pypsa.readthedocs.io/en/latest/developers.html"
)
__copyright__ = (
    "Copyright 2015-2023 PyPSA Developers, see https://pypsa.readthedocs.io/en/latest/developers.html, "
    "MIT License"
)
