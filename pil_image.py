from PIL import Image
import os

filename = "image_file/01.jpg"
pil_image = Image.open(filename).convert("L")
# pil_image.show()
infile = os.listdir("image_file")
print (infile)
outfile = os.path.splitext(infile[0])[0]+".png"
print (outfile)
if outfile != infile[0]:
    try:
        Image.open(filename).save(outfile)
    except IOError:
	    print("can not convert")