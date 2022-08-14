import math

# def constants():
pi = math.pi
m = 0.000511  # mass of electron in gev
alpha = 1 / 132.507  # alpha QED
delta = 2.0  # delta theta (radian)
convert = 3.894e8  # GeV^-2 to pb
E = 100  # 1.17 # initial photon energy in MeV, default 100 MeV
E = E * 1e-3  # initial photon energy in Gev
w = E / m  # ratio of Energy by mass, useful representation in equations
