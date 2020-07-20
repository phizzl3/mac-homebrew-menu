#!/usr/bin/env python3

"""These are just scripts for using Homebrew on my Mac so I don't 
have to remember all the commands. 

This is the "Functions" version of this script. 
"""

import subprocess

from art import disp_art
from cask_list import casks


def run_command(opt, cmd):
    subprocess.run(cmd, shell=True)


def disp_menu(opts):
    
    while True:
        disp_art()
        for opt, disp in opts.items():
            print(f"     [{opt:>2}] - {disp[0]}")

        selection = input("\n     Selection: ")
        if selection in opts:
            return selection


def homebrew_main():
    
    options = {
        '1': ('Install xCode Tools', 'xcode-select --install'),
        '2': ('Install Homebrew',
        'ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'),
        '3': ('Install Cask Package Manager', 'brew install cask'),
        '4': ('Install Rsync', 'brew install rsync'),
        '5': ('Install htop', 'brew install htop'),
        '6': ('Install youtube-dl', 'brew install ffmpeg'),
        '7': ('List Available Cask Packages', 'brew search --casks'),
        '8': ('Install from Available Casks', 'pass'),  # TODO
        '9': ('List Installed Cask Packages', 'brew cask list'),
        '10': ('Uninstall Cask Package', 'pass'),   # TODO 
        '11': ('Upgrade Installed Cask Packages', 'brew cask upgrade'),
        '12': ('Install Cask List', 'pass'),    # TODO 
        '13': ('Purge Package Cache', 'sudo rm -r ~/Library/Caches/Homebrew/downloads/'),
        '14': ('Full Install', 'pass'), # TODO 
        '15': ('Exit', 'exit')
    }

    while True:
        opt = disp_menu(options)
        if options[opt][1] == 'exit':
            break
        run_command(opt, options[opt][1])
        input("ENTER to continue...")



if __name__ == "__main__":
    homebrew_main()
