from PIL import Image
img = Image.open("assets/3.1_cat.jpg")
img.show()
width, height = img.size
for x in range(width) :
    for y in range(height) :
        p_color = img.getpixel((x,y))
        if type(p_color) == tuple:
            colR = 255 - p_color[0]
            colG = 255 - p_color[1]
            colB = 255 - p_color[2]
            img.putpixel((x,y), (colR, colG, colB))

img.show()
img.save("assets/3.6_cat_rgb_neg.png")