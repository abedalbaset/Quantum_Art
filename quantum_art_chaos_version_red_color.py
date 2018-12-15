#Quantum art
#Created by Eng.Abedalbaset Hamam for the first time in history in 12/12/2018
#Maybe this kind of art will reveal some secrets of quantum state of electron one day :)
import math
try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite
from svgwrite import cm, mm

file_name='result_randon_q'
with open(file_name) as f:
    quantumdatacontent = f.readlines()


number_of_bits=len(quantumdatacontent)
number_of_pixels=int(number_of_bits/8)
loop_size_bits=number_of_pixels*8
lenth_picture=int(math.sqrt(number_of_pixels))
pixels_array_R = []


for c in range(number_of_pixels):
    R7=int(quantumdatacontent[c*8])
    R6=int(quantumdatacontent[c*8+1])
    R5=int(quantumdatacontent[c*8+2])
    R4=int(quantumdatacontent[c*8+3])
    R3=int(quantumdatacontent[c*8+4])
    R2=int(quantumdatacontent[c*8+5])
    R1=int(quantumdatacontent[c*8+6])
    R0=int(quantumdatacontent[c*8+7])
    #pixels_array_R.append((2^0)*R0+(2^1)*R1+(2^2)*R2+(2^3)*R3+(2^4)*R4+(2^5)*R5+(2^6)*R6+(2^7)*R7)
    pixels_array_R.append((1)*R0+(2)*R1+(4)*R2+(8)*R3+(16)*R4+(32)*R5+(64)*R6+(128)*R7)

sizepixelzoom=3
def quantum_art_chaos_version(name):
    dwg = svgwrite.Drawing(filename=name, debug=True)
    hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    for y in range(lenth_picture):
        hlines.add(dwg.line(start=((1*sizepixelzoom)*mm, ((1+y)*sizepixelzoom)*mm), end=(((lenth_picture)*sizepixelzoom)*mm, ((1+y)*sizepixelzoom)*mm)))
    vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
    for x in range(lenth_picture):
        vlines.add(dwg.line(start=(((1+x)*sizepixelzoom)*mm, (1*sizepixelzoom)*mm), end=(((1+x)*sizepixelzoom)*mm, ((lenth_picture)*sizepixelzoom)*mm)))
    shapes = dwg.add(dwg.g(id='shapes', fill='red'))

    for h in range(lenth_picture):
        for v in range(lenth_picture):
            pixelposition=h*lenth_picture+v
            shapes.add(dwg.rect(insert=((h*sizepixelzoom)*mm, (v*sizepixelzoom)*mm), size=((1*sizepixelzoom)*mm, (1*sizepixelzoom)*mm),fill=svgwrite.rgb(pixels_array_R[pixelposition], pixels_array_R[pixelposition]/2, pixels_array_R[pixelposition]/3)))




    dwg.save()


if __name__ == '__main__':
    quantum_art_chaos_version('quantum_art_chaos_version_red_color.svg')
