import numpy as np

class OrthoPoly:
    """
    Orthogonal Polynomial approximation
    on given data, interval

    Implements Gram-Schmidt orthogonalization
    to construct the polynomial basis
    """
    def __init__(self, func, interval=[-1,1], n=3):
        """
        Gram-Schmidt to construct orthogonal polynomial basis

        Returns the `m` approximated points using `n`-degree polynomial

        Parameters
        ----------
        func: function
            the real function to approximate
        interval: tuple of float
            the start and end-point
        n: int
            number of polynomials to use as basis
        m: int
            number of points to evaluate the function at
        """
        self.func = func
        self.interval = interval
        self.n = n

    def __call__(self, x):
        m = len(x)
        data = self.func(x)

        # gram-schmidt
        poly = [np.ones(m)]
        if self.n > 1:
            for i in range(1,self.n):
                tempx = x**i
                for j in range(len(poly)):
                    tempx -= (tempx @ poly[j] / (poly[j] @ poly[j])) * poly[j]
                poly.append(tempx.copy())

        # calculate coefficients
        ck = []
        ak = []
        for polys in poly:
            ck.append(np.trapz(polys**2, x))
            ak.append(np.trapz(polys * data, x) / ck[-1])

        # output
        out = np.zeros(m)
        for i, polys in enumerate(poly):
            out += ak[i] * polys
        return(out)
        

