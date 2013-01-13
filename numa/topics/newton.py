# -*- coding: utf-8 -*-

"""
Newton method.
"""

from sympy import diff
from sympy.functions import Abs

from numa.utils import int_input, float_input, expr_input, eval_expr


def newton(a, b, fn, accuracy, digits):
    """
    Calculates the root of a function for a given
    interval using Newton method.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'

    fn_d1 = diff(fn)
    fn_d2 = diff(fn_d1)

    if eval_expr(fn, x=a) * eval_expr(fn_d2, x=a) > 0:
        x = a
    else:
        x = b

    while True:
        x1 = x - (eval_expr(fn, x=x) / eval_expr(fn_d1, x=x))
        x1 = x1.evalf(digits)

        if Abs(x1 - x) <= accuracy:
            return x1


if __name__ == '__main__':

    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu')
    accuracy = float_input('Zadajte presnost', default=0.01)
    digits = int_input('Zadajte pocet desatinnych miest', default=5)

    print newton(a, b, fn, accuracy, digits)