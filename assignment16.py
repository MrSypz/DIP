from PIL import Image
import numpy as np
import math
MAXCOLORCOUNT = 16777216 #24 bites or 16.7 million
with Image.open("assets/2.1_cat.jpg") as im:
    colsbefore = im.getcolors(maxcolors=MAXCOLORCOUNT)
    colsbefore = len(colsbefore) if colsbefore is not None else f"{MAXCOLORCOUNT}"
    im1 = im.quantize(colors=256)
    colsafter1 = len(im1.getcolors(maxcolors=MAXCOLORCOUNT))
    bit1 = int(math.log2(colsafter1))
    print(f"{colsbefore} --> {colsafter1} color tones or "+str(bit1)+"bites")
    im1.save("assets/2.35_cat_256.png")
    im2 = im.quantize(colors=16)
    colsafter2 = len(im2.getcolors(maxcolors=MAXCOLORCOUNT))
    bit2 = int(math.log2(colsafter2))
    print(f"{colsbefore} --> {colsafter2} color tones or "+str(bit2)+"bites")
    im1.save("assets/2.36_cat_16.png")