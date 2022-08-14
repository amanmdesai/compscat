import compscat.constants
import random


class CrossSection:
    def __init__(self, costh, w_max):
        self.pi = compscat.constants.pi
        self.alpha = compscat.constants.alpha
        self.m = compscat.constants.m
        self.w = compscat.constants.w
        self.delta = compscat.constants.delta
        self.w_max = w_max
        self.costh = costh

    def dsigma(self):
        pre_fact = 1
        sum_1 = 0
        pre_fact *= self.pi * (self.alpha / self.m) ** 2
        pre_fact *= 1 / (1 + self.w * (1 - self.costh)) ** 2
        sum_1 += 1 / (1 + self.w * (1 - self.costh))
        sum_1 += self.w * (1 - self.costh)
        sum_1 += self.costh**2
        return pre_fact * sum_1

    def xsection(self):
        costh = -1 + random.random() * self.delta
        w_i = CrossSection(costh, self.w_max).dsigma() * self.delta
        if self.w_max < w_i:
            self.w_max = w_i
        return w_i, costh, self.w_max
