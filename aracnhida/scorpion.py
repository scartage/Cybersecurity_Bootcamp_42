#!/usr/bin/env python3

import argparse
from PIL import Image
from PIL.ExifTags import TAGS
import os

def get_data(img):
    image = Image.open(img)
    exifdata = image.getexif()
    print(exifdata)
    try:
        for tagid in exifdata:
            tagname= TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            print(f"{tagname:25}: {value}")
    except Exception as e:
        print(f"FAILED: for this reason {e} ")

def parametros():
    parser = argparse.ArgumentParser()
    parser.add_argument('img', help="la imagen a la cual se le sacaran los metadatos")
    args = parser.parse_args()

    if args.img:
        get_data(args.img)
    else:
        print("fail")


if __name__ == "__main__":
    parametros()
