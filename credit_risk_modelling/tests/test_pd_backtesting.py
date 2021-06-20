"""Tests corresponding to the module pd_backtesting."""

import pytest
import credit_risk_modelling.pd_backtesting as back
import numpy as np


class TestDummy:
    """Dummy."""

    def test1(self):
        """Test dummy."""
        a = 2
        b = 2.0
        np.testing.assert_almost_equal(a, b)

