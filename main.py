#! /usr/bin/env pyhton3
# coding: utf-8

import argparse

# pourquoi en ./main.py ne trouve pas le python 3
from Labyrinth import Labyrinth
from GameManager import GameManager
from Gui import Gui

ap = argparse.ArgumentParser()
ap.add_argument('-g', '--gui',
                help="start graphic game", action='store_true')
args = ap.parse_args()


def main():
    laby = Labyrinth('labyrinth.txt')
    if args.gui:
        gui = Gui(laby)
        gui.launch_game()
    else:
        print('In else')
        gamer = GameManager(laby)
        gamer.lauch_game()


if __name__ == "__main__":
    main()
