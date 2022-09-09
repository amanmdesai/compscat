from __future__ import annotations

import argparse

from cross_section import CrossSection
from save_events import SaveEvent

import compscat


def main():

    parser = argparse.ArgumentParser(
        prog="compscat",
        description="Monte Carlo Simulation of Compton Scattering",
    )
    parser.add_argument(
        "--energy",
        type=float,
        required=True,
        help="Energy of the Photon in MeV",
    )
    arguments = parser.parse_args()

    if arguments.energy <= 0.1:
        raise Exception("Energy Cannot be less than 1 MeV")

    E = arguments.energy * 1e-3

    w_sum, w_square, w_max = CrossSection(E / compscat.constants.m).integrate_xsec()

    SaveEvent(10000, w_max, E).to_root()


if __name__ == "__main__":
    main()
