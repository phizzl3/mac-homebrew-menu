#!/usr/bin/env python3

"""These are just scripts for using Homebrew on my Mac so I don't 
have to remember all the commands. 

Uses a separate "hb_data.py" file containing lists of attributes and installs.

This is the "OOP" version of this script. 
"""


import subprocess

from art import disp_art
from hb_data import attrs, casks, installs


class Brew:

    # Initialize class variable for the list of objects
    brews_list = []

    # Initialize attributes for objects
    def __init__(self, opt, disp, cmd):
        self.option = opt
        self.display = disp
        self.command = cmd

    # Set up output format for string printing
    def __str__(self):
        return f"\t[{self.option:>2}] - {self.display}"

    def run_command(self):
        """Gets passed objects and runs attached commands 
        attributes in the terminal."""

        # Initialize variable for use when there's no string formatting
        c_name = None

        # Run specifics based on 'option' attribute where needed,
        # then wait for user input
        if self.option in ('4', '12'):
            c_name = ' '.join(installs)

        if self.option == '6':
            c_name = input("Which package would you like to install?: ")

        if self.option == '8':
            c_name = input("Which package would you like to remove?: ")

        if self.option == '12':
            for item in Brew.brews_list:
                if item.option in ('1', '2', '3', '4'):
                    subprocess.run(item.command.format(c_name), shell=True)

        if self.option in ('10', '12'):
            c_name = ' '.join(casks)

        if self.option == '12':
            for item in Brew.brews_list:
                if item.option in ('10', '11'):
                    subprocess.run(item.command.format(c_name), shell=True)

        else:
            subprocess.run(self.command.format(c_name), shell=True)
        input("ENTER to continue...")

    @classmethod
    def generate_list(cls):
        """Use list of attributes to generate list of objects."""

        # Generate objects and add them to the list
        for group in attrs:
            Brew.brews_list.append(Brew(group[0], group[1], group[2]))

    @staticmethod
    def brew_main():
        """Main-Generate list and call menu and methods on a loop."""

        Brew.generate_list()

        # Display menu options and get user selection
        while True:
            
            disp_art()
            for item in Brew.brews_list:
                print(item)
            sel = input("\n\tSelection: ")

            # Call method based on returned user input
            for item in Brew.brews_list:
                if item.option == sel:
                    if item.command == 'exit':
                        return
                    item.run_command()
                    break


if __name__ == "__main__":
    Brew.brew_main()
