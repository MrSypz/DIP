from PIL import Image, ImageEnhance
im = Image.open("assets/2.6_cat_g.png")
enhancer = ImageEnhance.Brightness(im)
factor = 1 #give original image
im_output = enhancer.enhance(factor)
im_output.save("assets/2.37_original-cat.png")
factor = 0.5 #darkens the image
im_output = enhancer.enhance(factor)
im_output.save("assets/2.38_darkens-cat.png")
factor = 1.5 #brightens the image
im_output = enhancer.enhance(factor)
im_output.save("assets/2.39_brightens-cat.png")