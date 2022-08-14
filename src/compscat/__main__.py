import argparse

import compscat
from cross_section import CrossSection
from save_events import SaveEvent


def main() -> None:

    parser = argparse.ArgumentParser(
        prog="compscat",
        description="Monte Carlo Simulation of Compton Scattering",
    )
    parser.add_argument(
        "E",
        action="store_true",
        help="Energy of the Photon",
    )
    arguments = parser.parse_args()

    w_sum, w_square, w_max = CrossSection(
        arguments.E / compscat.constants.m
    ).integrate_xsec()

    SaveEvent(10000, w_max, arguments.E).to_root()


if __name__ == "__main__":
    main()
