import numpy as np
from black_scholes_pricing import BlackScholes

# Class to calculate the greeks for BS model:
# Delta
# Gamma
# Vega
# Rho
# Theta
# 1. European options
# 2. Binary cash options
# 3. Binary asset options

class BlackScholesGreek(BlackScholes):
    def delta(self, OptType):
        if OptType == "Call":
            return np.exp(-self.q * self.T) * BlackScholes.N(self.d1())
        if OptType == "Put":
            return np.exp(-self.q * self.T) * (BlackScholes.N(self.d1()) - 1)
        else:
            raise ValueError("Unrecognized option type")

    def gamma(self):
        return (np.exp(-self.q * self.T) * BlackScholes.n(self.d1())
                ) / (self.S * self.sig * np.sqrt(self.T))

    def vega(self, OptType):
        return np.exp(-self.q * self.T) * self.S * \
            np.sqrt(self.T) * BlackScholes.n(self.d1())

    def rho(self, OptType):
        if OptType == "Call":
            return self.K * self.T * \
                np.exp(-self.r * self.T) * BlackScholes.N(self.d2())
        if OptType == "Put":
            return -self.K * self.T * \
                np.exp(-self.r * self.T) * BlackScholes.N(-self.d2())
        else:
            raise ValueError("Unrecognized option type")

    def theta(self, OptType):
        if OptType == "Call":
            return -(self.S * BlackScholes.n(self.d1()) * self.sig * np.exp(-self.q * self.T)) / (2 * np.sqrt(self.T)) + self.q * self.S * \
                np.exp(-self.q * self.T) * BlackScholes.N(self.d1()) - self.r * self.K * np.exp(-self.r * self.T) * BlackScholes.N(self.d2())
        if OptType == "Put":
            return -(self.S * BlackScholes.n(self.d1()) * self.sig * np.exp(-self.q * self.T)) / (2 * np.sqrt(self.T)) - self.q * self.S * \
                np.exp(-self.q * self.T) * BlackScholes.N(-self.d1()) + self.r * self.K * np.exp(-self.r * self.T) * BlackScholes.N(-self.d2())
        else:
            raise ValueError("Unrecognized option type")


# compute greeks analytically for binary cash options


    def delta_cash(self, OptType):
        if OptType == "Call":
            return np.exp(-self.r * self.T) * BlackScholes.n(self.d2()
                                                             ) / (self.S * self.sig * np.sqrt(self.T))
        if OptType == "Put":
            return -np.exp(-self.r * self.T) * BlackScholes.n(self.d2()
                                                              ) / (self.S * self.sig * np.sqrt(self.T))
        else:
            raise ValueError("Unrecognized option type")

    def gamma_cash(self, OptType):
        if OptType == "Call":
            return -np.exp(-self.r * self.T) * BlackScholes.n(self.d2()) * \
                self.d1() / (self.S**2 * self.sig**2 * self.T)
        if OptType == "Put":
            return np.exp(-self.r * self.T) * BlackScholes.n(self.d2()) * \
                self.d1() / (self.S**2 * self.sig**2 * self.T)
        else:
            raise ValueError("Unrecognized option type")

    def vega_cash(self, OptType):
        if OptType == "Call":
            return -np.exp(-self.r * self.T) * \
                BlackScholes.n(self.d2()) * self.d1() / self.sig
        if OptType == "Put":
            return np.exp(-self.r * self.T) * \
                BlackScholes.n(self.d2()) * self.d1() / self.sig
        else:
            raise ValueError("Unrecognized option type")

    def rho_cash(self, OptType):
        if OptType == "Call":
            return np.exp(-self.r * self.T) * (np.sqrt(self. T) * BlackScholes.n(
                self.d2()) / self.sig - self.T * BlackScholes.n(self.d2()))
        if OptType == "Put":
            return np.exp(-self.r * self.T) * (-np.sqrt(self. T) * BlackScholes.n(
                self.d2()) / self.sig - self.T * BlackScholes.n(-self.d2()))
        else:
            raise ValueError("Unrecognized option type")

    def theta_cash(self, OptType):
        if OptType == "Call":
            return np.exp(-self.r * self.T) * (self.r * BlackScholes.N(self.d2()) + (BlackScholes.n(self.d2()) / (
                2 * self.T**(3 / 2) * self.sig)) * (np.log(self.S / self.K) - (self.r - self.q - self.sig**2 / 2) * self.T))
        if OptType == "Put":
            return np.exp(-self.r * self.T) * (self.r * BlackScholes.N(-self.d2()) - (BlackScholes.n(self.d2()) / (
                2 * self.T**(3 / 2) * self.sig)) * (np.log(self.S / self.K) - (self.r - self.q - self.sig**2 / 2) * self.T))
        else:
            raise ValueError("Unrecognized option type")


# compute greeks analytically for binary asset options


    def delta_asset(self, OptType):
        if OptType == "Call":
            return np.exp(-self.q * self.T) * BlackScholes.n(self.d1()) / (self.sig * \
                          np.sqrt(self.T)) + np.exp(-self.q * self.T) * BlackScholes.N(self.d1())
        if OptType == "Put":
            return -np.exp(-self.q * self.T) * BlackScholes.n(self.d1()) / (self.sig * \
                           np.sqrt(self.T)) + np.exp(-self.q * self.T) * BlackScholes.N(-self.d1())
        else:
            raise ValueError("Unrecognized option type")

    def gamma_asset(self, OptType):
        if OptType == "Call":
            return -np.exp(-self.q * self.T) * BlackScholes.n(self.d1()
                                                              ) * self.d2() / (self.sig**2 * self.S * self.T)
        if OptType == "Put":
            return np.exp(-self.q * self.T) * BlackScholes.n(self.d1()
                                                             ) * self.d2() / (self.sig**2 * self.S * self.T)
        else:
            raise ValueError("Unrecognized option type")

    def vega_asset(self, OptType):
        if OptType == "Call":
            return -np.exp(-self.q * self.T) * self.S * \
                BlackScholes.n(self.d1()) * self.d2() / (self.sig)
        if OptType == "Put":
            return np.exp(-self.q * self.T) * self.S * \
                BlackScholes.n(self.d1()) * self.d2() / (self.sig)
        else:
            raise ValueError("Unrecognized option type")

    def rho_asset(self, OptType):
        if OptType == "Call":
            return -np.exp(-self.q * self.T) * (np.sqrt(self. T)
                                                * BlackScholes.n(self.d1()) / self.sig)
        if OptType == "Put":
            return np.exp(-self.q * self.T) * (np.sqrt(self. T)
                                               * BlackScholes.n(self.d1()) / self.sig)
        else:
            raise ValueError("Unrecognized option type")

    def theta_asset(self, OptType):
        if OptType == "Call":
            return self.S * np.exp(-self.q * self.T) * (self.q * BlackScholes.N(self.d1()) + (BlackScholes.n(self.d1()) / (
                2 * self.T**(3 / 2) * self.sig)) * (np.log(self.S / self.K) - (self.r - self.q - self.sig**2 / 2) * self.T))
        if OptType == "Put":
            return self.S * np.exp(-self.q * self.T) * (self.q * BlackScholes.N(-self.d1()) - (BlackScholes.n(self.d1()) / (
                2 * self.T**(3 / 2) * self.sig)) * (np.log(self.S / self.K) - (self.r - self.q - self.sig**2 / 2) * self.T))
        else:
            raise ValueError("Unrecognized option type")
