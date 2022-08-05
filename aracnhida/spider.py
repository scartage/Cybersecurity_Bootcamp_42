#!/usr/bin/env python3

import requests                 #sacamos el html de la url
from bs4 import BeautifulSoup   #ponemos los datos en un formato mas "legible"
from selenium import webdriver  # ?
import io                       #convertimos las imagenes en data binaria
from PIL import Image           
import os                       #tener funciones del sistema operativo
import sys                      #tomar argumentos por terminal
from tld import get_fld         #nos permite sacar el dominio
import re                       #buscar la extension de la url, filtrar url
import time

data = "./data"
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
            image_to_down_RE.append(img)         #estas son las imagenes que se descargan por recursividad
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
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    make_path(path)

    for item in soup.find_all('a'):
        links_to_look.append(item['href'])
    
    dominio = get_fld(url)
    for link in links_to_look:
        if dominio in link:
            recursive_links.append(link)        #links para recursividad (basado en dominio)
        else:
            continue

    if parametro == True:                       #aqui enviamos a recursividad
        if cantidad == 0:
            i = 1
            for link in recursive_links:
                get_url_img(link, path)
                if i == 6:
                    break
                i += 1
        else:
            i = 1
            for link in recursive_links:
                if i == cantidad + 1:
                    break
                get_url_img(link, path)
                i += 1
    else:
        for item in soup.find_all('img'):
            image_url.append(item['src'])          #esto solo lo hacen el la URL, sin recursividad

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


    
if __name__ == "__main__":
    args = sys.argv[1:]
    len_p = len(args)
    print(len_p)
    if len_p == 1:
        url_to_look = args[0]
        principal("./data", url_to_look, False, 0)
    elif len_p == 2:
        if "-r" in args:
            url_to_look = args[1]
            principal ("./data", url_to_look, True, 0)
    elif len_p == 3:
        if "-p" in args:
            path = args[1]
            url = args[2]
            print(f"path: {path}, url: {url}")
            principal(path, url, False, 0)
    elif len_p == 4:
        if "-r" in args and "-l" in args:
            cantidad = int(args[2])
            url = args[3]
            principal("./data", url, True, cantidad)
        elif "-r" in args and "-p" in args:
            path = args[2]
            url = args[3]
            print(f"este es el path {path} y la url {url}")
            principal(path, url, True, 0)
    elif len_p == 6:
        if "-r" in args and "-l" in args and "-p" in args:
            cantidad = int(args[2])
            path = args[4]
            url = args[5]
            print(f"cantidad :{cantidad}, ubi: {path}, url: {url}")
            principal(path, url, True, cantidad)
    else:
        print("Error: Parametros incorrectos")
    
