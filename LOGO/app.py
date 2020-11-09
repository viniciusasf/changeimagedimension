from PIL import Image
import zipfile
import os



try:
    im = Image.open("logo.jpg")
except FileNotFoundError:
    print("Altere o nome da imagem para logo.jpg")
else:
    im.thumbnail((173, 114))
    im.save("RAVE\RAVE.jpg")
    im.save("RAVE\RAVE.bmp")

    rave_zip = zipfile.ZipFile("RAVE\RAVE.zip", 'w')
    for folder, subfolders, file in os.walk("\RAVE"):
        for file in files:
            rave_zip.write(os.path.join(folder, file), file, compress_type=zipfile.ZIP_DEFLATED)
    rave_zip.close()

    im.show()
    print("ARQUIVO ZIP GERADO COM SUCESSO \n\n CLIQUE ENTER PARA CONTINUAR: ")