#!/usr/bin/env python3

"""These are just scripts for using Homebrew on my Mac so I don't 
have to remember all the commands. 

Uses a separate "data.py" file containing lists of attributes and installs.

This is the "OOP" version of this script. 
"""


import subprocess

from art import disp_art
from data import ATTRS, CASKS, INSTALLS


class Brew:

    def __init__(self, opt, disp, cmd):
        """Initialize attributes for objects."""

        self.option = opt
        self.display = disp
        self.command = cmd

    def __str__(self):
        """Set up output format for string printing."""

        return f"\t[{self.option:>2}] - {self.display}"

    def run_command(self):
        """Gets passed objects and runs attached commands 
        attributes in the terminal."""

        # Initialize variable for use when there's no string formatting
        install = None

        # Homebrew apps installer
        if self.option in ('4', '12'):
            install = ' '.join(INSTALLS)

       # Cask installer
        if self.option == '6':
            install = input("Which package would you like to install?: ")

        # Cask uninstaller
        if self.option == '8':
            install = input("Which package would you like to remove?: ")

        # Cask list installer & Full install
        if self.option in ('10', '12'):
            install = ' '.join(CASKS)

        # Run command
        subprocess.run(self.command.format(install), shell=True)


class BrewList(list):

    def disp_menu(self):
        """Display 'Menu' of objects, return selection."""

        for item in self:
            print(item)
        return input("\n\tSelection: ")

    def call_method(self, sel):
        """Call method based on returned user input."""

        for item in self:
            if item.option == sel:
                if item.command == 'exit':
                    return False

                # Full install command
                if item.command == 'full':
                    for each in self:
                        if each.option in ('1', '2', '3', '4', '10', '11'):
                            each.run_command()
                    return True

                # Run command for all but 'exit' and 'full'
                item.run_command()
                break

        # Run if selection isn't found
        else:
            print("\nTry again...")

        input("\nENTER to continue...")
        return True

    def compile_list(self):
        """Generate objects and add them to the list."""

        for group in ATTRS:
            self.append(Brew(group[0], group[1], group[2]))


def main():
    """Generate list and objects and call methods."""

    go = True
    brews = BrewList()
    brews.compile_list()

    while go:
        disp_art()
        sel = brews.disp_menu()
        go = brews.call_method(sel)


if __name__ == "__main__":
    main()
