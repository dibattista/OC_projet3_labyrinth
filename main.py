#! /usr/bin/env python3
# coding: utf-8

"""This module launch the game"""

import argparse

from Labyrinth import Labyrinth
from GameManager import GameManager
from Gui import Gui

ap = argparse.ArgumentParser()
ap.add_argument('-g', '--gui',
                help="start graphic game", action='store_true')
args = ap.parse_args()


def main():
    """
        The condition will defined if you want start in terminal,
        with the module GameManager or
        with in graphic version with the module Gui.
        To allow you to choose the version in shell,
        a argument "-g" is adding for the graphic version.
    """

    laby = Labyrinth('labyrinth.txt')
    if args.gui:
        gui = Gui(laby)
        gui.launch_game()
    else:
        gamer = GameManager(laby)
        gamer.launch_game()


if __name__ == "__main__":
    main()
