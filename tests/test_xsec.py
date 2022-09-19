from compscat import *

E = .1

w_sum, w_square, w_max = compscat.CrossSection(E / compscat.constants.m).integrate_xsec(10000)

#print(constants.convert)

sigma_x = w_sum*constants.convert/(10000*1E12)

print(sigma_x)

assert sigma_x < .0095
assert sigma_x > .0076
#    print("test_passed")
#else:
#    raise(Error)
