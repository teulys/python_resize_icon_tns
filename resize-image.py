from PIL import Image
from resizeimage import resizeimage
import sys
import os

# org_dir = sys.argv[1]
# des_dir = sys.argv[2]

org_dir = "/Users/Teulys/Documents/NativeScriptDoc/TutorEnLinea/Tutor en Linea/ImagenesWeb"
des_dir = "/Users/Teulys/Documents/workspace/nativescript/tutorenlinea"

# org_dir = "/Users/Teulys/Documents/SubastaRD"
# des_dir = "/Users/Teulys/Documents/workspace/nativescript/subastasrd"

files = os.listdir(org_dir)

android_name = ["xxxhdpi","xxhdpi","xhdpi","hdpi","mdpi"]
android_size = [640, 480, 320, 240, 160]

ios_name = ["-Small","-Small@2x","-Small@2x","-40","-40@2x","-40@3x","-60@2x","-60@3x","-76","-76@2x","-120"]
ios_size = [29,58,87,40,80,120,120,180,76,152,120]

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
                cover.save(des_dir+"/app/App_Resources/Android/src/main/res/drawable-" + name + "/" + f, image.format)
        i += 1

    i = 0
    for name in ios_name:
        with open(filename, 'r+b') as f2:
            with Image.open(f2) as image:
                cover = resizeimage.resize_cover(image, [ios_size[i], ios_size[i]])
                cover.save(des_dir+"/app/App_Resources/iOS/" + f[:-4] + name + ".png", image.format)
        i += 1




