#!/usr/bin/env python3

"""These are just scripts for using Homebrew on my Mac so I don't 
have to remember all the commands. 

This is the "OOP" version of this script. 
"""


import subprocess

from art import disp_art
from cask_list import casks


class Brew:

    brews_list = []

    def __init__(self, opt, disp, cmd):
        self.option = opt
        self.display = disp
        self.command = cmd

    def __str__(self):
        return f"\t[{self.option:>2}] - {self.display}"

    def run_command(self):

        c_name = None

        if self.option == '8':
            c_name = input("Which package would you like to install?: ")
        if self.option == '10':
            c_name = input("Which package would you like to remove?: ")
        if self.option == '12':
            c_name = ' '.join(casks)

        subprocess.run(self.command.format(c_name), shell=True)
        input("ENTER to continue...")

    @classmethod
    def generate_list(cls):

        info = (
            ('1', 'Install xCode Tools', 'xcode-select --install'),
            ('2', 'Install Homebrew',
             'ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'),
            ('3', 'Install Cask Package Manager', 'brew install cask'),
            ('4', 'Install Rsync', 'brew install rsync'),
            ('5', 'Install htop', 'brew install htop'),
            ('6', 'Install youtube-dl', 'brew install ffmpeg'),
            ('7', 'List Available Cask Packages', 'brew search --casks'),
            ('8', 'Install from Available Casks', 'brew cask install {}'),
            ('9', 'List Installed Cask Packages', 'brew cask list'),
            ('10', 'Uninstall Cask Package', 'brew cask uninstall {}'),
            ('11', 'Upgrade Installed Cask Packages', 'brew cask upgrade'),
            ('12', 'Install Cask List', 'brew cask install {}'),
            ('13', 'Purge Package Cache (su)',
             'sudo rm -r ~/Library/Caches/Homebrew/downloads/'),
            # ('14', 'Full Install', 'pass'),  # TODO
            ('15', 'Exit', 'exit')
        )

        for each in info:
            Brew.brews_list.append(Brew(each[0], each[1], each[2]))

    @staticmethod
    def brew_main():
        Brew.generate_list()
        while True:

            disp_art()
            for each in Brew.brews_list:
                print(each)
            sel = input("\n\tSelection: ")

            for item in Brew.brews_list:
                if item.option == sel:
                    if item.command == 'exit':
                        return
                    item.run_command()
                    break


if __name__ == "__main__":
    Brew.brew_main()
