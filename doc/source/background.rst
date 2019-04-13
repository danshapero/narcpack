Background
==========

NARCPACK is designed to solve a set of common problems in numerical analysis.
This page gives some background on these numerical problems.

Approximation
-------------

Suppose we are given a function :math:`f` defined in a domain :math:`\Omega` in Euclidean space.
We want to find another function that is close to :math:`f` in some sense and easy to compute.
To do this, we choose a set of basis functions :math:`\{\phi_k\}` defined in :math:`\Omega` and some norm :math:`\|\cdot\|`.
The approximation problem is to find a set of coefficients :math:`\hat f_k` such that the error

.. math::

   J(\hat f) = \left\|f - \sum_k\hat{f_k}\phi_k\right\|^2

is minimized.
For example, on the unit interval :math:`[-1, 1]` with the usual :math:`L^2` norm, Legendre polynomials are especially convenient approximating polynomials.


Interpolation
-------------

Given a set of points :math:`\{x_k\}` in :math:`\mathbb{R}^n` and the set of values :math:`y_k` at each point of some function :math:`f`, the interpolant of :math:`f` at these points with the basis functions :math:`\{\phi_k\}` is the function

.. math::

   \hat f(x) = \sum_l\hat{f_l}\phi_l(x)

such that, for each of the interpolation points :math:`x_k`,

.. math::

   \hat f(x_k) = y_k.

Finding the coefficients amounts to solving a linear system with the generalized Vandermonde matrix.
