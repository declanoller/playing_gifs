from PIL import Image, ImageFont, ImageDraw, ImageColor
import numpy as np
from math import floor,ceil,cos,sin,pi,sqrt,exp
import imageio
from copy import copy


images = []
outpath = "/home/declan/Documents/code/gifs/imgfile/"
gifpath = "/home/declan/Documents/code/gifs/"

imgsize = 500
imgRad = imgsize/2
imgCenter = np.array([imgRad,imgRad]).astype(int)
width = int(imgRad/3)


img = Image.new('RGBA', (imgsize,imgsize), (0,0,0,0))


mouthPosPercent = np.array([97,122])/160
#mouthPosPercent = np.array([78,105])/140
#mouthPosPercent = np.array([80,107])/150
#mouthPosPercent = np.array([155,235])/300

willImg = Image.open(gifpath+"bobbyhead1.png").convert('RGBA')
willSize = np.array(willImg.size)

ub = 25
steps = 10
printstep = int(ub/steps)
for i in range(ub):

    copyImg = copy(img)

    if not i%printstep:
        print(i)

    ptSize = .01
    startSize_tiny = .1
    startSize_small = .5
    startSize_big = 2.2
    endSize_big = 92

    speedExp = 1.8
    will_zero = willImg.resize(tuple((willSize*(ptSize+(startSize_tiny-ptSize)*(i/ub)**speedExp)).astype(int)))
    will_tiny = willImg.resize(tuple((willSize*(startSize_tiny+(startSize_small-startSize_tiny)*(i/ub)**speedExp)).astype(int)))
    will_small = willImg.resize(tuple((willSize*(startSize_small+(startSize_big-startSize_small)*(i/ub)**speedExp)).astype(int)))
    will_big = willImg.resize(tuple((willSize*(startSize_big+(endSize_big-startSize_big)*(i/ub)**speedExp)).astype(int)))


    ULcorner = tuple((imgCenter-np.multiply(mouthPosPercent,will_zero.size)).astype(int))
    copyImg.paste(will_zero,ULcorner,will_zero)
    ULcorner = tuple((imgCenter-np.multiply(mouthPosPercent,will_tiny.size)).astype(int))
    copyImg.paste(will_tiny,ULcorner,will_tiny)
    ULcorner = tuple((imgCenter-np.multiply(mouthPosPercent,will_small.size)).astype(int))
    copyImg.paste(will_small,ULcorner,will_small)
    ULcorner = tuple((imgCenter-np.multiply(mouthPosPercent,will_big.size)).astype(int))
    copyImg.paste(will_big,ULcorner,will_big)


    tempfile = outpath+"tempfile.jpeg"
    copyImg.save(tempfile, "JPEG")
    images.append(imageio.imread(tempfile))


kargs = { 'duration': .001 }
imageio.mimsave(outpath+'movie.gif', images, **kargs)

exit(0)



#
