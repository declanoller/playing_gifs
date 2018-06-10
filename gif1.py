#import os, sys
from PIL import Image, ImageFont, ImageDraw, ImageColor
import numpy as np
#import scipy.io
#import scipy.misc as smp
#import matplotlib.pyplot as plt
from math import floor,ceil,cos,sin,pi,sqrt
import imageio
from copy import copy




images = []
path = "/home/declan/Documents/code/gifs/imgfile/"
dogpath = "/home/declan/Documents/code/gifs/"

imgsize = 150
imgRad = imgsize/2
imgCenter = np.array([imgRad,imgRad])
revs = 3
width = int(imgRad/3)







ub = 100
steps = 10
printstep = int(ub/steps)

will_1 = Image.open(dogpath+"willhead3.png").convert('RGBA')




will_2 = Image.open(dogpath+"willhead3.png").convert('RGBA')
origWillSize = will_1.size
print(origWillSize)
imgCenter = np.array([origWillSize[0]/2,origWillSize[0]/2])

img = Image.new('RGBA', origWillSize, (255,255,255,255))
#img = Image.new('RGBA', origWillSize, (0,0,0,0))
#img.thumbnail((imgsize,imgsize), Image.ANTIALIAS)
#draw = ImageDraw.Draw(img)


#print(will_1.size)
newWillSize = (50,50)
will_1.thumbnail(newWillSize,Image.ANTIALIAS)


coord = int(imgCenter[0]-newWillSize[0]/2)
ULcorner = (coord,coord)
print(ULcorner)

img.paste(will_1,ULcorner,will_1)


#mouth pos is (155,230)/300

#print(will_1.size)
newWillSize = (600,600)
print(newWillSize)
will_2.thumbnail(newWillSize,Image.ANTIALIAS)


coord = int(imgCenter[0]-newWillSize[0]/2)
ULcorner = (coord+30,coord-50)
print(ULcorner)

#img = Image.alpha_composite(img,will_2)
img.paste(will_2,ULcorner,will_2)


img.show()

exit(0)


kargs = { 'duration': .07 }
imageio.mimsave(path+'movie.gif', images, **kargs)

exit(0)






####################################################################


img = Image.new('RGBA', (imgsize,imgsize), (255,255,255,0))
img.thumbnail((imgsize,imgsize), Image.ANTIALIAS)
draw = ImageDraw.Draw(img)


ub = 100
steps = 10
printstep = int(ub/steps)

img = Image.open(dogpath+"dawg1.jpg").convert('HSV')
imgDat = np.array(img)


imgw = len(imgDat)
imgh = len(imgDat[0])


centerCoords = np.array([imgw/2,imgh/2])


offsets = np.zeros([imgw,imgh])

for x in range(imgw):
    for y in range(imgh):
        dist = np.linalg.norm(centerCoords-[x,y])
        offsets[x,y] = (2*dist)

for i in range(ub):

    if not i%printstep:
        print(i)


    shiftedImgDat = copy(imgDat)


    centerCoords = np.array([imgw/2,imgh/2])

    for x in range(imgw):
        for y in range(imgh):

            dist = np.linalg.norm(centerCoords-[x,y])

            colorShift = (360)*(i/ub)

            shiftedImgDat[x,y][0] = (imgDat[x,y][0] + offsets[x,y] - colorShift)%360

    img2 = Image.fromarray(shiftedImgDat, mode='HSV')
    img2 = img2.convert('RGB')
    tempfile = path+"tempfile.jpeg"
    img2.save(tempfile, "JPEG")
    images.append(imageio.imread(tempfile))



###############################################################


for i in range(ub):

    if not i%printstep:
        print(i)

    colorOffset = int(360*(i/ub))

    layersUb = 100
    for j in range(layersUb):
        width = (1 - (j/ub))*imgsize*sqrt(2)
        corner1 = imgCenter - width/2
        corner2 = imgCenter + width/2
        hueString = str(int(360*revs*(j/ub)) + colorOffset)
        colString = "hsl("+hueString+",100%,50%)"

        draw.ellipse([tuple(corner1),tuple(corner2)],fill = colString,outline=None)

    tempfile = path+"tempfile.jpeg"
    img.save(tempfile, "JPEG")
    images.append(imageio.imread(tempfile))


################################################################

for i in range(ub):

    if not i%printstep:
        print(i)

    radius = 1.5*imgRad*(i/ub)
    angle = 2*pi*(i/ub)*revs

    objCenter = imgCenter + radius*np.array([cos(angle),sin(angle)])


    corner1 = objCenter - width/2
    corner2 = objCenter + width/2

    hueString = str(int(360*revs*(i/ub)))
    colString = "hsl("+hueString+",100%,50%)"

    draw.ellipse([tuple(corner1),tuple(corner2)],fill = colString,outline=None)

    tempfile = path+"tempfile.jpeg"
    img.save(tempfile, "JPEG")
    images.append(imageio.imread(tempfile))
