import numpy as np
from scipy.stats import norm

# S: Spot price
# K: Strike price
# T: Time to expiration in years
# r: risk free interest rate
# sig: annualized volatility
# q: Dividen yield

class BlackScholes:
    def __init__(self, S, K, T, r, sig, q=0):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sig = sig
        self.q = q

    # Print out the parameter used in the instance of the class
    def parameters(self):
        return {
            'S': self.S, 'K': self.K, 'T': round(
                self.T, 3), 'r': round(
                self.r, 3), 'Volatility': round(
                self.sig, 3), 'Dividends': round(
                    self.q, 3)}
                
    # cumulative distribution function of the normal distribution
    @staticmethod
    def N(x):
        return norm.cdf(x)

    # probability distribution function of the normal distribution
    @staticmethod
    def n(x):
        return norm.pdf(x)

    # d1 and d2 in the BS model
    def d1(self):
        return (np.log(self.S / self.K) + (self.r - self.q + self.sig **
                2 / 2) * self.T) / (self.sig * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sig * np.sqrt(self.T)

    def _call(self):
        return self.S * np.exp(-self.q * self.T) * BlackScholes.N(self.d1()) - \
            self.K * np.exp(-self.r * self.T) * BlackScholes.N(self.d2())

    # price the options
    def _put(self):
        return self.K * np.exp(-self.r * self.T) * BlackScholes.N(-self.d2()) - \
            self.S * np.exp(-self.q * self.T) * BlackScholes.N(-self.d1())

    def price_vanilla(self, OptType):
        if OptType == "Call":
            return self._call()
        if OptType == "Put":
            return self._put()
        else:
            raise ValueError("Unrecognized option type")

    def _cash_or_nothing_call(self):
        return np.exp(-self.r * self.T) * BlackScholes.N(self.d2())

    def _cash_or_nothing_put(self):
        return np.exp(-self.r * self.T) * BlackScholes.N(-self.d2())

    def price_cash(self, OptType):
        if OptType == "Call":
            return self._cash_or_nothing_call()
        if OptType == "Put":
            return self._cash_or_nothing_put()
        else:
            raise ValueError("Unrecognized option type")

    def _asset_or_nothing_call(self):
        return self.S * np.exp(-self.q * self.T) * BlackScholes.N(self.d1())

    def _asset_or_nothing_put(self):
        return self.S * np.exp(-self.q * self.T) * BlackScholes.N(-self.d1())

    def price_asset(self, OptType):
        if OptType == "Call":
            return self._asset_or_nothing_call()
        if OptType == "Put":
            return self._asset_or_nothing_put()
        else:
            raise ValueError("Unrecognized option type")
            
    # Determine if the put call parity is satisfied
    def put_call_parity(self):
        return self.price("Call") + self.K * np.exp(-self.r *
                                                    self.T) == self.price("Put") + self.S * np.exp(-self.q * self.T)
    # Calculation of the implied volatility
    def vega(self):
        return np.exp(-self.q * self.T) * self.S * \
            np.sqrt(self.T) * BlackScholes.n(self.d1())

    def implied_volatility(self, Market, tol=1.0e-5):
        sigma_old = self.sig
        max_iter = 100
        self.sig = 0.3

        for i in range(max_iter):
            BS_price = self._call()
            vega = self.vega()
            diff = BS_price - Market

            sigma_new = self.sig - diff / vega

            if abs(sigma_new - self.sig) < tol or abs(diff) < tol:
                print(f"Newton-Raphson took {i} iterations")
                break
            self.sig = sigma_new

        self.sig = sigma_old
        return sigma_new
