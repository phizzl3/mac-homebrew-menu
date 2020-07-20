import subprocess

def disp_art():
    """Clear console (MacOS) and display ASCII art."""

    art = """                              ___                   
  /\  /\___  _ __ ___   ___  / __\_ __ _____      __
 / /_/ / _ \| '_ ` _ \ / _ \/__\// '__/ _ \ \ /\ / /
/ __  / (_) | | | | | |  __/ \/  \ | |  __/\ V  V / 
\/ /_/ \___/|_| |_| |_|\___\_____/_|  \___| \_/\_/  
                                                    
                                                    
             /\/\   ___ _ __  _   _                 
            /    \ / _ \ '_ \| | | |                
           / /\/\ \  __/ | | | |_| |                
           \/    \/\___|_| |_|\__,_|                
                                                    
                                                    """

    subprocess.run("clear", shell=True)
    print(art)


if __name__ == "__main__":
    disp_art()
    