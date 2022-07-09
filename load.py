from pystyle import Colors, Colorate, Center, System, Anime

banner = '''
▀█████████▄     ▄████████    ▄████████     ███      ▄█   ▄██████▄  ███▄▄▄▄   
  ███    ███   ███    ███   ███    ███ ▀█████████▄ ███  ███    ███ ███▀▀▀██▄ 
  ███    ███   ███    ███   ███    █▀     ▀███▀▀██ ███▌ ███    ███ ███   ███ 
 ▄███▄▄▄██▀    ███    ███   ███            ███   ▀ ███▌ ███    ███ ███   ███ 
▀▀███▀▀▀██▄  ▀███████████ ▀███████████     ███     ███▌ ███    ███ ███   ███ 
  ███    ██▄   ███    ███          ███     ███     ███  ███    ███ ███   ███ 
  ███    ███   ███    ███    ▄█    ███     ███     ███  ███    ███ ███   ███ 
▄█████████▀    ███    █▀   ▄████████▀     ▄████▀   █▀    ▀██████▀   ▀█   █▀  
                                                                             
'''

def load():

    System.Title("Bastion")
    System.Clear()

    Anime.Fade(Center.XCenter(banner), Colors.yellow_to_green, Colorate.Vertical, time=3, interval=0.025)

    print(Colorate.Vertical(Colors.yellow_to_green, Center.XCenter(banner), 1))
    print(Colorate.Vertical(Colors.yellow_to_green, Center.XCenter("by MecPerspicace | v1.0"), 1))
    print(Colorate.Vertical(Colors.yellow_to_green, Center.XCenter("For $EGLD donation : erd19jcvvj7v7re6pnmypjds2yvlzrwdvp0l8lxr5qn2mdlns7jt8xrqtccly5"), 1))

    print("\n")