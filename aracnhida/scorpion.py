#!/usr/bin/env python3

import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import os
from colorama import Fore

banner = """ 

   ██████  ▄████▄   ▒█████   ██▀███   ██▓███   ██▓ ▒█████   ███▄    █ 
▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▓██░  ██▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▓██░ ██▓▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒██▄█▓▒ ▒░██░▒██   ██░▓██▒  ▐▌██▒
▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒▒██▒ ░  ░░██░░ ████▓▒░▒██░   ▓██░
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░░▒ ░      ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░ ░░        ▒ ░░ ░ ░ ▒     ░   ░ ░ 
      ░  ░ ░          ░ ░     ░               ░      ░ ░           ░ 
         ░                                                           
                                                            by scartage
"""

def get_data(img):
    image = Image.open(img)
    exifdata = image.getexif()
    if not exifdata:
        print(Fore.YELLOW + "No se han encotrado metadatos en la imagen" + Fore.RESET)
    try:
        for tagid in exifdata:
            tagname= TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            print(f"{tagname:25}: {value}")
    except Exception as e:
        print(Fore.RED + f"FAILED: for this reason {e} " + Fore.RESET)

def parametros():
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', help="the image that you would like to get the metadata (you should put the image path)")
    parser.add_argument('-img2', help="second image to get metadata (you must put -img2 and the path of the second img)")
    args = parser.parse_args()

    if args.image_path:
        if args.img2:
            get_data(args.image_path)
            print()
            print(Fore.GREEN + "---- second img ----" + Fore.RESET)
            print()
            get_data(args.img2)
        else:
            get_data(args.image_path)
    else:
        print(Fore.RED + "fail" + Fore.RESET)


if __name__ == "__main__":
    print(Fore.LIGHTBLUE_EX + banner + Fore.RESET)
    parametros()
