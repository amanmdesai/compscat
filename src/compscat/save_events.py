import uproot
import compscat.GENEvents


class SaveEvent(Nevent, w_max):
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
            "Photon Energy (keV)": ph_e * 1e6,
            "Photon Px (keV)": ph_px * 1e6,
            "Photon Py (keV)": ph_py * 1e6,
            "Photon Pz (keV)": ph_pz * 1e6,
            "Electron E (keV)": el_e * 1e6,
            "Electron Px (keV)": el_px * 1e6,
            "Electron Py (keV)": el_py * 1e6,
            "Electron Pz (keV)": el_pz * 1e6,
        }
