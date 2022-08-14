import numpy
import math
import compscat.constants
import compscat.CrossSection


class generate_events:
    def __init__(self, Nevent, w_max, E):

        self.Nevent = Nevent
        self.w_max = w_max
        self.delta = compscat.constants.delta
        self.E = E
        self.m = compscat.constants.m
        self.w_max = w_max
        self.costh = costh

    def gen_events(self):
        i = 0
        prob = 0
        m_costh = np.zeros(Nevent)
        ph_px = np.zeros(Nevent)
        ph_py = np.zeros(Nevent)
        ph_pz = np.zeros(Nevent)
        ph_e = np.zeros(Nevent)
        el_px = np.zeros(Nevent)
        el_py = np.zeros(Nevent)
        el_pz = np.zeros(Nevent)
        el_e = np.zeros(Nevent)
        while i < Nevent:
            costh = -1 + random.random() * self.delta
            phi = 2 * math.pi * random.random() * self.delta
            w_ii = CrossSection(costh, self.w_max).dsigma() * self.delta
            prob = w_ii / self.w_max
            random_point = random.random()
            if random_point < prob:
                m_costh[i] = math.degrees(math.acos(costh))
                sinth = math.sqrt(1 - costh**2)
                ph_e[i] = self.m * self.E / (self.E * (1 - costh) + self.m)
                ph_px[i] = ph_e[i] * sinth * math.cos(phi)
                ph_py[i] = ph_e[i] * sinth * math.sin(phi)
                ph_pz[i] = -ph_e[i] * costh

                el_e[i] = self.E + self.m - ph_e[i]
                el_px[i] = -ph_px[i]
                el_py[i] = -ph_py[i]
                el_pz[i] = -self.E + (ph_e[i] * costh)
                i = i + 1
        return ph_e, ph_px, ph_py, ph_pz, el_e, el_px, el_py, el_pz
