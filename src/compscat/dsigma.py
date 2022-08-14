import compscat.constants


def dsigma(costh):
    pre_fact = 1
    sum_1 = 0
    pre_fact *= (
        compscat.constants.pi * (compscat.constants.alpha / compscat.constants.m) ** 2
    )
    pre_fact *= 1 / (1 + compscat.constants.w * (1 - costh)) ** 2
    sum_1 += 1 / (1 + compscat.constants.w * (1 - costh))
    sum_1 += compscat.constants.w * (1 - costh)
    sum_1 += costh**2
    return pre_fact * sum_1
