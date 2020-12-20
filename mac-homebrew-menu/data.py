"""Lists of attributes and packages to install for use with the main script.

Add/Remove/Comment out as needed.
"""


# List of attributes for use in instantiating Brew objects
# (option, display, command)
ATTRS = (
    ('1', 'Install xCode Tools', 'xcode-select --install'),
    ('2', 'Install Homebrew',
     '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"'),
    ('3', 'Install Cask Package Manager', 'brew install cask'),
    ('4', 'Install Homebrew Apps List', 'brew install {}'),
    ('5', 'List Available Cask Packages', 'brew search --casks'),
    ('6', 'Install from Available Casks', 'brew cask install {}'),
    ('7', 'List Installed Cask Packages', 'brew cask list'),
    ('8', 'Uninstall Cask Package', 'brew cask uninstall {}'),
    ('9', 'Upgrade Installed Cask Packages', 'brew upgrade --cask'),
    ('10', 'Install Cask List', 'brew cask install {}'),
    ('11', 'Purge Package Cache (su)',
     'sudo rm -r ~/Library/Caches/Homebrew/downloads/'),
    ('12', 'Full Install', 'full'),
    ('13', 'Exit', 'exit')
)


# List of cask packages to install
CASKS = (
    'appcleaner',
    'applepi-baker',
    'boom',
    'calibre',
    'cloudmounter',
    'cyberduck',
    'fliqlo',
    'google-backup-and-sync',
    'google-chrome',
    'grammarly',
    'handbrake',
    'iina',
    'lastpass',
    'macs-fan-control',
    'megasync',
    'omnidisksweeper',
    'onedrive',
    'sdformatter',
    'simple-comic',
    'spotify',
    'the-unarchiver',
    'transmission',
    'tunnelbear',
    'virtualbox',
    'virtualbox-extension-pack',
    'visual-studio-code',
    'vnc-server',
    'vnc-viewer'
)


# List of homebrew apps to install
INSTALLS = (
    'rsync',
    'htop',
    'youtube-dl',
    'ffmpeg'
)
