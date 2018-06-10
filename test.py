from PIL import Image, ImageFont, ImageDraw, ImageColor


circ = Image.open("circ.png")
#circ = Image.open("circ.jpeg").convert('RGBA')
print(circ.mode)
circ.show()


rect = Image.open("rect.png")
#rect = Image.open("rect.jpeg").convert('RGBA')


#rect.show()

both = Image.alpha_composite(circ,rect)

both.show()
