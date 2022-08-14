import uproot
from compscat.generate_event import GENEvents


class SaveEvent:
    def __init__(self, Nevent, w_max, E):
        self.Nevent = Nevent
        self.w_max = w_max
        self.E = E

    def to_root(self):
        ph_e, ph_px, ph_py, ph_pz, el_e, el_px, el_py, el_pz = GENEvents(
            self.Nevent, self.w_max, self.E
        ).gen_events()
        file = uproot.recreate("MC_compton.root")
        file["events"] = {
            "Photon_Energy": ph_e * 1e6,
            "Photon_Px": ph_px * 1e6,
            "Photon_Py": ph_py * 1e6,
            "Photon_Pz": ph_pz * 1e6,
            "Electron_E": el_e * 1e6,
            "Electron_Px": el_px * 1e6,
            "Electron_Py": el_py * 1e6,
            "Electron_Pz": el_pz * 1e6,
        }
