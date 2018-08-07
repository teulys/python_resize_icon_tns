from PIL import Image
from resizeimage import resizeimage
import sys
import os

org_dir = sys.argv[1]
des_dir = sys.argv[2]

# org_dir = "/Users/Teulys/Documents/NativeScriptDoc/TutorEnLinea/Tutor en Linea/ImagenesWeb"
# des_dir = "/Users/Teulys/Documents/workspace/nativescript/tutorenlinea"

files = os.listdir(org_dir)

android_name = ["xxxhdpi","xxhdpi","xhdpi","hdpi","mdpi"]
android_size = [640, 480, 320, 240, 160]

for f in files:
    filename = org_dir + "/" + f
    print("Converting file:"+filename)
    
    if filename[-4:] != '.png':
        continue

    i = 0
    for name in android_name:
        with open(filename, 'r+b') as f2:
            with Image.open(f2) as image:
                cover = resizeimage.resize_cover(image, [android_size[i], android_size[i]])
                cover.save(des_dir+"/platforms/android/app/src/main/res/drawable-" + name + "/" + f, image.format)
        i += 1



