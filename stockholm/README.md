             ,d                             88         88                        88
             88                             88         88                        88
             88                             88         88                        88
,adPPYba,  MM88MMM  ,adPPYba,    ,adPPYba,  88   ,d8   88,dPPYba,    ,adPPYba,   88  88,dPYba,,adPYba,
I8[    ""    88    a8"     "8a  a8"     ""  88 ,a8"    88P'    "8a  a8"     "8a  88  88P'   "88"    "8a
 `"Y8ba,     88    8b       d8  8b          8888[      88       88  8b       d8  88  88      88      88
aa    ]8I    88,   "8a,   ,a8"  "8a,   ,aa  88`"Yba,   88       88  "8a,   ,a8"  88  88      88      88
`"YbbdP"'    "Y888  `"YbbdP"'    `"Ybbd8"'  88   `Y8a  88       88   `"YbbdP"'   88  88      88      88
											     by scartage

listado de extensiones que este programa encripta:
['.der','.pfx','.crt','csr','p12','.pem','.odt','.ott','.sxw','.uot','.3ds','.max', 
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


Este programa un ransomware que se encarga de encriptar todos los archivos
que esten en: ./HOME/User/infection y que ademas tengan una extension igual a
los afectados por WANNACRY.

No encripta archivos con extension ".ft" ni archivos que esten en subcarpetas
(en el caso de que quiera encriptar este tipo de archivos, pongalos en la carpteta
principal (que deberia estar en ./HOME/User/infection)).

Para ejecutar el programa ponga en la terminal: python3 stockholm.py
	Esto debera mostar por pantalla los archivos que fueron encriptados y ademas se les ha agregado
	la extension ".ft", ademas de darle una key para desencriptar los archivos.
	Adicional a esto, se creara un archivo thekey.key en la misma ubicacion donde ejecute stockholm.py
	en ese archivo tambien puede encontrar la key de desencriptcion.

	Si desea hacer esto mismo, pero sin tener ningun output por pantalla use el parametro -silence o -s.

Tambien puede usar el programa con los siguientes parametros/argumentos:
	-v or -version		Ver la version actual del programa
	-h or -help			Para mostar la ayuda

Para desencriptar use el parametro -reverse o -r mas la key dada.
	OJO! para usar esta opcion debe dejar un espacio entre el parmetro y la key
	ejemplo: python3 stockholm.py -reverse [key...]

Este programa usa Fernet para la encriptacion.
	Que es Fernet? Fernet es un metodo de encriptacion simetrica que se asegura de que el mensaje
		encriptado no pueda ser manipulado/leido sin la key correspondiente.
