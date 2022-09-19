from __future__ import annotations

import random

import compscat.constants


class CrossSection:
    def __init__(self, w):
        self.pi = compscat.constants.pi
        self.alpha = compscat.constants.alpha
        self.delta = compscat.constants.delta
        self.m = compscat.constants.m
        self.w = w

    def dsigma(self, costh):
        pre_fact = 1
        sum_1 = 0
        pre_fact *= self.pi * (self.alpha / self.m) ** 2
        pre_fact *= 1 / (1 + self.w * (1 - costh)) ** 2
        sum_1 += 1 / (1 + self.w * (1 - costh))
        sum_1 += self.w * (1 - costh)
        sum_1 += costh**2
        return pre_fact * sum_1

    def xsection(self, w_max):
        costh = -1 + random.random() * self.delta
        w_i = CrossSection(self.w).dsigma(costh) * self.delta
        if w_max < w_i:
            w_max = w_i
        return w_i, w_max

    def integrate_xsec(self, N=10000):
        w_sum = 0
        w_max = 0
        w_square = 0
        for _i in range(N):
            w_i, w_max = CrossSection(self.w).xsection(w_max)
            w_sum += w_i
            w_square += w_i * w_i
        return w_sum, w_square, w_max
