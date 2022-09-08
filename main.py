from pystyle import Write, Colors
from rich.progress import track
import load
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "()[]{},;:.-_/\\?+*#"


def get(message):
    return Write.Input(message + " -> ", Colors.yellow_to_green, interval=0.005, hide_cursor=False)


if __name__ == "__main__":
    load.load()
    all = ""
    if get("Do you want uppercase letters ? (y/n)") == "y":
        all += uppercase_letters
    if get("Do you want lowercase letters ? (y/n)") == "y":
        all += lowercase_letters
    if get("Do you want numbers ? (y/n)") == "y":
        all += numbers
    if get("Do you want symbols ? (y/n)") == "y":
        all += symbols

    lenght = int(get("Enter lenght of passwords"))
    ammount = int(get("Enter the amount of passwords"))

    f = open("passwords.txt", "w")

    for x in track(range(ammount), description=f"Generating {ammount} passwords ..."):
        password = "".join(random.sample(all, lenght))
        f.write(password + "\n")
    
    f.close()
    
    Write.Input(f"Successfully write {ammount} passwords in passwords.txt", Colors.yellow_to_green, interval=0.005, hide_cursor=False)
