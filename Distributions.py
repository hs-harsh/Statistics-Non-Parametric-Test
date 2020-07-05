from statistics import NormalDist
from scipy.stats import poisson
val = NormalDist(mu=0, sigma=1).cdf(1.96)
print(val)

x = 12
mu = 4
cdf = poisson.cdf(x, mu)
print(cdf)
