#!/usr/bin/env python3

import argparse                 #obtenemos argumentos
import requests                 #sacamos el html de la url
from bs4 import BeautifulSoup   #ponemos los datos en un formato mas "legible"
import io                       #convertimos las imagenes en data binaria
from PIL import Image           
import os                       #tener funciones del sistema operativo
from tld import get_fld         #nos permite sacar el dominio
#import re                       #buscar la extension de la url, filtrar url
import time

links_to_look = []
recursive_links = []
image_url = []
image_to_down = []
ext_to_download = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

def getdata(url):
    r = requests.get(url)
    print(r)
    return r.text

def download_image(download_path, img, file_name):
    ts = time.time()
    try:
        image_content = requests.get(img).content    #con request sacamos de la url en contenido de la image
        image_file = io.BytesIO(image_content)       #almecenamos la imagen en formato de bytes 
        image = Image.open(image_file)               #abrimos la imagen en bytes desde memoria
        name, ext = os.path.splitext(img)
        if ext == ".jpg":
           path_to_down = download_path + "/jpg-jpeg/"
           file_path = path_to_down + file_name + str(ts) + ".jpg"
           with open(file_path, "wb") as f:
               f.write(image_content)
        elif ext == ".jpeg":
            path_to_down = download_path + "/jpg-jpeg/"
            file_path = path_to_down + file_name + str(ts) + ".jpeg"
            with open(file_path, "wb") as f:
                f.write(image_content)
        elif ext == ".png":
            path_to_down = download_path + "/png/"
            file_path = path_to_down + file_name + str(ts) + ".png"
            with open(file_path, "wb") as f:
                f.write(image_content)
        elif ext == ".gif":
            path_to_down = download_path + "/gif/"
            file_path = path_to_down + file_name + str(ts) + ".gif"
            with open(file_path, "wb") as f:
                 f.write(image_content)
        elif ext == ".bmp":
            path_to_down = download_path + "/bmp/"
            file_path = path_to_down + file_name + str(ts) + ".bmp"
            with open(file_path, "wb") as f:
               f.write(image_content)
        print(f"Imagen: {img} descargada con exito")
    except Exception as e:
        print(f"FAILED: for this reason {e} - ")


def get_url_img(url, path):
    image_url_RE = []
    image_to_down_RE = []
   

    get_html_data = getdata(url)
    sopa = BeautifulSoup(get_html_data, 'html.parser')

    for item in sopa.find_all('img'):
        image_url_RE.append(item['src'])

    for img in image_url_RE:
        name, ext = os.path.splitext(img)
        if ext in ext_to_download:
            image_to_down_RE.append(img)
        else:
            continue
    if path == "./data":
        for img in image_to_down_RE:
            download_image("./data", img, "spiderRE")
    else:
        for img in image_to_down_RE:
            download_image(path, img, "spiderRE")

def make_path(path):
    if path == "./data":
        if not os.path.exists(path):
            os.mkdir(path)
            os.mkdir("data/jpg-jpeg/")
            os.mkdir("data/png/")
            os.mkdir("data/gif/")
            os.mkdir("data/bmp/")
    else:
        if not os.path.exists(path):
            os.mkdir(path)
            os.mkdir(path + "/jpg-jpeg/")
            os.mkdir(path + "/png/")
            os.mkdir(path + "/gif/")
            os.mkdir(path + "/bmp/")


    
def principal(path, url, parametro, cantidad):
    try:
        htmldata = getdata(url)
        soup = BeautifulSoup(htmldata, 'html.parser')
        make_path(path)
    except Exception as e:
        print(f"Error: {e}")
        exit()

    if parametro == True:
        try:
            for item in soup.find_all('a'):
                links_to_look.append(item['href'])
        except Exception as e:
            print(f"FAILED: {e}")
            exit()
        
        dominio = get_fld(url)
        for link in links_to_look:
            if dominio in link:
                recursive_links.append(link)
            else:
                continue

        if cantidad == 5:
            print("recursividad")
            i = 1
            for link in recursive_links:
                get_url_img(link, path)
                if i == 5:
                    break
                i += 1
        else:
            print("recursividad")
            i = 1
            for link in recursive_links:
                if i == cantidad + 1:
                    break
                get_url_img(link, path)
                i += 1
    else:
        for item in soup.find_all('img'):
            image_url.append(item['src'])

        for img in image_url:
            name, ext = os.path.splitext(img) 
            if ext in ext_to_download:
                image_to_down.append(img)           
            else:
                continue
        if path == "./data":
            for img in image_to_down:
                download_image("./data/", img, "spider")
        else:
            for img in image_to_down:
                download_image(path, img, "spider")

def parametros():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action = 'store_true', help = "recursively downloads the images in different links with the same domain", required = False)
    parser.add_argument('-l', type = int, action = 'store', help = "how many times do you want to do -r (you must use -r with this parameter). If it's not defined it will be 5", default = 5)
    parser.add_argument('-p', type = str, help = "path where you would like to save your images (same directory)", required = False)
    parser.add_argument('url', type = str, action = 'store', help = "<required> link to the website.")
    args = parser.parse_args()

    if args.url:
        if args.url and args.r:
            if args.p and args.l:
                principal(args.p, args.url, True, args.l)
            elif args.p:
                principal(args.p, args.url, True, 0)
            elif args.l:
                principal("./data", args.url, True, args.l)
            else:
                principal("./data", args.url, True, args.l)
        elif args.p:
            principal(args.p, args.url, False, 0)
        else:
            principal("./data", args.url, False, 0)

if __name__ == "__main__":
    parametros() 
