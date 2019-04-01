import lhw
import graphics as gr
from scipy.stats import uniform
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import chi2
from scipy.stats import t


def calculateEmpirCharacts(values, mean, var, distName):
    M = sum(values) / len(values)
    D = 0
    for i in range(len(values)):
        D += (values[i] - M) ** 2
    D /= len(values)

    print(str(distName) + ":")
    print("+---------------------------------------------+")
    print("+ Char |     exp    |    teor    | teor - exp |")
    print("+---------------------------------------------+")
    print("|   M  | %10.4f | %10.4f | %10.4f |" % (M, mean, mean - M))
    print("|   D  | %10.4f | %10.4f | %10.4f |" % (D, var, var - D))
    print("+---------------------------------------------+")
    pass


def plotEmpirFunctions(values):
    gr.plotDensity(values)
    gr.plotProbability(values)
    pass


def startWork(values, mean, var, distName):
    if isinstance(values[0], list) == True:
        for i in range(len(values)):
            calculateEmpirCharacts(values[i], mean, var, distName[i])
            plotEmpirFunctions(values[i])
    else:
        calculateEmpirCharacts(values, mean, var, distName)
        plotEmpirFunctions(values)
        pass


def testUniform(a, b, size):
    values = [lhw.rnuni(a, b) for i in range(size)]
    mean, var = uniform.stats(a, b - 1, moments='mv')
    startWork(values, mean, var, "uniform")
    pass


def testNormal(mu, sigma, N, size):
    values = [[lhw.rnnorm1(mu, sigma) for i in range(size)],
              [lhw.rnnorm2(mu, sigma, N) for i in range(size)]]
    mean, var = norm.stats(mu, sigma, moments='mv')
    distNames = ["rnnrm1", "rnnrm2"]
    startWork(values, mean, var, distNames)
    pass


def testExponential(betta, size):
    values = [lhw.rnexp(betta) for i in range(size)]
    mean, var = expon.stats(0, betta, moments='mv')
    startWork(values, mean, var, "exponential")
    pass


def testChisquare(N, size):
    values = [lhw.rnchsq(N) for i in range(size)]
    mean, var = chi2.stats(N, moments='mv')
    startWork(values, mean, var, "chiSquare")
    pass


def testStudent(N, size):
    values = [lhw.rnstud(N) for i in range(size)]
    mean, var = t.stats(N, moments='mv')
    startWork(values, mean, var, "student")
    pass
